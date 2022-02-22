import ipywidgets as w
from IPython.display import clear_output, display
import threading
import time

class ThreadApp:
    def __init__(self):
        # state
        self.RUNNING_PROCESS = False

        # widgets
        self._output = w.Output()
        self._l_welcome = w.Label("Welcome!")
        self._l_status = w.Label("Idle")
        self._b_run = w.Button(description = "START")

        self._b_run.on_click(self.handle_run)

    def run(self):
        with self._output:
            clear_output()
            display(w.VBox([
                self._l_welcome,
                self._l_status,
                self._b_run
            ]))
        return self._output

    def update_status(self):
        _pips = "__________"
        _t_pip = "-"
        _tick = 0
        self._b_run.disabled = True

        while self.RUNNING_PROCESS:
            _pos_r = _tick % len(_pips)

            _right = f"{_pips[0:_pos_r]}{_t_pip}{_pips[_pos_r: -1]}"
            self._b_run.description = _right

            _tick += 1

            time.sleep(.2)

        self._b_run.disabled = False
        self._b_run.description = "START"

    def run_process(self):
        for x in range(100):
            self._l_status.value = f"PROGRESS MESSAGE {x}"
            time.sleep(.1)
        self.RUNNING_PROCESS = False

    def handle_run(self, _):
        self.RUNNING_PROCESS = True
        th1 = threading.Thread(target = self.update_status)
        th2 = threading.Thread(target = self.run_process)
        th1.start()
        th2.start()
