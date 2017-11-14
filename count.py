# -*- coding: utf-8 -*-
# Created with PyCharm on MacBook.
# @Time    : 11/7/17 11:53 PM
# @Author  : Tongjie Wang

from pathlib import Path


def get_path() -> Path or None:
    """Get path
    :returns a Path object or None (when the user wants to quit the program)"""
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
            print()


def count_lines(file_path: Path) -> None:
    """Counting useful lines
    :param file_path: user-input file path"""
    file = None
    try:
        useful_line_sum, comment_line_sum, blank_line_sum, docstring_line_sum = 0, 0, 0, 0
        docstring_continuing = False
        file = file_path.open()
        for line in file:
            if line.strip().startswith('#'):
                comment_line_sum += 1
            elif line.strip() in '\r\n':
                blank_line_sum += 1
            elif line.strip().startswith('"""'):
                docstring_line_sum += 1
                if not line.strip().endswith('"""'):
                    docstring_continuing = True
            elif line.strip().endswith('"""') and docstring_continuing:
                docstring_line_sum += 1
                docstring_continuing = False
            elif docstring_continuing:
                docstring_line_sum += 1
            else:
                useful_line_sum += 1
    except OSError:
        print('Cannot open the file!')
    else:
        print('The sum of useful lines is {}.'.format(useful_line_sum))
        print('The sum of comment lines is {}.'.format(comment_line_sum))
        print('The sum of blank lines is {}.'.format(blank_line_sum))
        print('The sum of docstring lines is {}.'.format(docstring_line_sum))
        print('Total lines: {}'.format(useful_line_sum + comment_line_sum + blank_line_sum + docstring_line_sum))
    finally:
        if file is not None:
            file.close()


if __name__ == '__main__':
    path = get_path()
    if path is not None:
        count_lines(path)
