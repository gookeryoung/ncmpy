from pathlib import Path

from PySide2.QtCore import QRunnable, Signal, QObject
from ncmpy.libncmdump import ncmdump


class UnlockRunner(QRunnable, QObject):
    sig_runner_finished = Signal()
    sig_error_msg = Signal(str)

    def __init__(self, input_path: str, out_dir: str):
        super().__init__()

        self.input_path = input_path
        self.out_dir = out_dir

    def run(self):
        src_file = Path(self.input_path)
        out_file = src_file.with_suffix('.flac')
        if not out_file.exists():
            ncmdump(src_file.as_posix(), out_file.as_posix())
        else:
            self.sig_error_msg.emit(f'文件已存在{out_file.name}')
        self.sig_runner_finished.emit()
