import argparse
import pathlib
import typing
from concurrent.futures import ThreadPoolExecutor, as_completed, Future

from libncmdump import ncmdump

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-d", dest="directory", required=True)

    args = arg_parser.parse_args()
    directory = args.directory
    src_files = pathlib.Path(directory).rglob("*.ncm")

    futures: typing.List[Future] = []
    with ThreadPoolExecutor(max_workers=12) as t:
        for src_file in src_files:
            futures.append(
                t.submit(
                    ncmdump,
                    src_file.as_posix(),
                    src_file.with_suffix(".flac").as_posix(),
                )
            )

        for future in as_completed(futures):
            ret = future.result()
            print(f"{ret=}")
