import pyperclip


def copy_contents(file_path: str) -> None:
    contents = open(file_path, 'r').read()
    pyperclip.copy(contents)
