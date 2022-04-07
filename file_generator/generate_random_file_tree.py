import os
import itertools
import pathlib
import randomfiletree


def generate_random_files(target_dir: pathlib.Path) -> pathlib.Path:
    sourcedir = pathlib.Path(f"{os.path.abspath(os.path.dirname(__file__))}/templates")
    sources = []
    for srcfile in sourcedir.iterdir():
        with open(srcfile, "rb") as f:
            content = f.read()
        sources.append((srcfile.suffix, content))

    for srcfile in itertools.cycle(sources):
        random_string = randomfiletree.core.random_string()
        path = target_dir / (random_string + srcfile[0])
        with path.open("wb") as f:
            f.write(srcfile[1] + random_string.encode())
        yield path


# nfiles: file creation probability
# nfolders: directory creation probability
# payload: customize file name and content
# Usage example:
# randomfiletree.core.iterative_gaussian_tree(
#     "./test_folder",
#     nfiles=10,
#     nfolders=10,
#     maxdepth=5,
#     repeat=4,
#     payload=callback
# )
