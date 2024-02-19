from pathlib import Path

from PySide2.QtCore import QRunnable, QThread
from ncmpy.libncmdump import ncmdump


class UnlockRunner(QRunnable):
    def __init__(self, input_path: str, out_dir: str):
        super().__init__()

        self.input_path = input_path
        self.out_dir = out_dir

    def run(self):
        print(f"线程已启动: id={QThread.currentThread()}")

        src_file = Path(self.input_path)
        out_file = src_file.with_suffix(".flac")
        if not out_file.exists():
            ncmdump(src_file.as_posix(), out_file.as_posix())
        else:
            print(f"文件已存在{out_file.name}")
        print(f"线程已结束: {QThread.currentThread()}")
