from PySide2.QtCore import QThread, QThreadPool, Signal
from ncmpy.gui.droplistwidget import DropListWidget
from ncmpy.unlocker.unlockrunner import UnlockRunner


class Unlocker(QThread):
    sig_unlocked = Signal(int, int)
    sig_msg_updated = Signal(str)

    def __init__(self, list_widget: DropListWidget, out_dir: str):
        super().__init__()

        self.list_widget = list_widget
        self.out_dir = out_dir

        self.unlocked_count = 0
        self.total_count = 0
        self.threadpool = QThreadPool()
        self.threadpool.setMaxThreadCount(5)

    def run(self) -> None:
        self.sig_msg_updated.emit(f"启动解锁线程: id={QThread.currentThread()}")

        self.total_count = self.list_widget.get_file_count()
        for i in range(self.total_count):
            file = self.list_widget.get_next_file()
            runner = UnlockRunner(file, out_dir=self.out_dir)
            self.sig_msg_updated.emit(f"解锁文件: {file}")
            self.threadpool.start(runner)

        self.sig_msg_updated.emit(f"结束解锁线程: id={QThread.currentThread()}")

    def on_runner_finished(self):
        self.unlocked_count += 1
        self.sig_unlocked.emit(self.unlocked_count, self.total_count)
