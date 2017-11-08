# -*- coding: utf-8 -*-
# Created with PyCharm on MacBook.
# @Time    : 11/7/17 11:53 PM
# @Author  : Tongjie Wang

from pathlib import Path


def get_path() -> Path or None:
    while True:
        print('Please enter a file path; an empty input would make the program exit;')
        path_str = input('Your input: ')
        if path_str == '':
            return None
        file_path = Path(path_str)
        if file_path.exists() and file_path.is_file():
            return file_path
        else:
            print('Invalid file path; Please retry.')


def count_lines(file_path: Path) -> None:
    file = None
    try:
        useful_line_sum = 0
        file = file_path.open()
        for line in file:
            if line.startswith('#'):
                continue
            elif line in '\r\n':
                continue
            else:
                useful_line_sum += 1
    except OSError:
        print('Cannot open the file!')
    else:
        print('The sum of useful lines is {}.'.format(useful_line_sum))
    finally:
        if file is not None:
            file.close()


if __name__ == '__main__':
    count_lines(get_path())
