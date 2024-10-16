from filtertree import __version__, filtertree
# import os
# from pathlib import Path
import subprocess
import argparse


def main():
    args = parse_arguments()
    filtertree(echo, args.src_dir, args.dest_dir)


def echo(src_file_path, dest_file_path):
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
