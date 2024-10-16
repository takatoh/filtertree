from filtertree import __version__
import os
from pathlib import Path
import subprocess
import argparse


def main():
    args = parse_arguments()

    src_dir = args.src_dir
    dest_dir = Path(args.dest_dir)
    for cur_dir, _, files in os.walk(src_dir):
        current = Path(cur_dir)
        for file in files:
            src_file_path = current / file
            dest_file_path = dest_dir.joinpath(src_file_path.relative_to(src_dir))
            dest_file_path.parent.mkdir(parents=True, exist_ok=True)
            cmd = f"echo {str(src_file_path)} {str(dest_file_path)}"
            subprocess.call(cmd, shell=True)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Apply filter to directory tree."
    )
    parser.add_argument(
        "src_dir",
        metavar="SRCDIR",
        action="store",
        help="source directory"
    )
    parser.add_argument(
        "dest_dir",
        metavar="DESTDIR",
        action="store",
        help="destination directory"
    )
    parser.add_argument(
        "-V", "--version",
        action="version",
        version=f"v{__version__}",
        help="show version and exit"
    )
    args = parser.parse_args()
    return args
