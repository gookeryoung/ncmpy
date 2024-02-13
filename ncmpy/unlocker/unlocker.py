from PySide2.QtCore import QThread, Signal, QThreadPool

from gui.droplistwidget import DropListWidget
from unlocker.unlockrunner import UnlockRunner


class Unlocker(QThread):
    unlocked = Signal(int, int)

    def __init__(self, parent=None, list_widget: DropListWidget = None, out_dir: str = ""):
        super(Unlocker, self).__init__(parent)
        self.setParent(parent)

        self.list_widget: DropListWidget = list_widget
        self.out_dir = out_dir
        self.unlocked_count = 0
        self.count = 0
        self.thread_pool = QThreadPool(self)

    def run(self):
        self.count = self.list_widget.get_file_count()
        for i in range(self.count):
            input_file = self.list_widget.get_next_file()
            runner = UnlockRunner(input_file, self.out_dir)
            runner.runner_finished.connect(self.runner_finished)

            ok = False
            while not ok:
                ok = self.thread_pool.tryStart(runner)

        self.thread_pool.waitForDone()
        self.exit()

    def runner_finished(self):
        self.unlocked_count += 1
        self.unlocked.emit(self.unlocked_count, count)
