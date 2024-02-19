from PySide2.QtCore import QThread, Signal, QThreadPool

from ncmpy.gui.droplistwidget import DropListWidget
from ncmpy.unlocker.unlockrunner import UnlockRunner


class Unlocker(QThread):
    sig_unlocked = Signal(int, int)
    sig_error_msg = Signal(str)

    def __init__(self, parent=None, list_widget: DropListWidget = None, out_dir: str = ""):
        super(Unlocker, self).__init__(parent)
        self.setParent(parent)

        self.list_widget = list_widget
        self.out_dir = out_dir
        self.unlocked_count = 0
        self.count = 0
        self.thread_pool = QThreadPool(self)

    def run(self):
        self.count = self.list_widget.get_file_count()
        for i in range(self.count):
            input_file = self.list_widget.get_next_file()
            runner = UnlockRunner(input_file, self.out_dir)
            runner.sig_runner_finished.connect(self.on_runner_finished)
            runner.sig_error_msg.connect(self.on_error_msg)

            ok = False
            while not ok:
                ok = self.thread_pool.tryStart(runner)

        self.thread_pool.waitForDone()
        self.exit()

    def on_runner_finished(self):
        self.unlocked_count += 1
        self.sig_unlocked.emit(self.unlocked_count, count)

    def on_error_msg(self, msg: str):
        self.sig_error_msg.emit(msg)
