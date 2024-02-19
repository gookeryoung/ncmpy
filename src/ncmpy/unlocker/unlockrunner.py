from pathlib import Path

from PySide2.QtCore import QRunnable, Signal, QObject
from ncmpy.libncmdump import ncmdump


class UnlockRunner(QRunnable, QObject):
    runner_finished = Signal()

    def __init__(self, input_path: str, out_dir: str):
        super().__init__()

        self.input_path = input_path
        self.out_dir = out_dir

    def run(self):
        src_file = Path(self.input_path)
        out_file = src_file.with_suffix('.flac')
        ncmdump(src_file.as_posix(), out_file.as_posix())
        self.runner_finished.emit()
