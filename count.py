# -*- coding: utf-8 -*-
# Created with PyCharm on MacBook.
# @Time    : 11/7/17 11:53 PM
# @Author  : Tongjie Wang

from pathlib import Path


def get_path() -> Path or None:
    """Get path
    :returns a Path object or None (when the user wants to quit the program)"""
    while True:
        print('Please enter a file path for counting single file;')
        print('or enter a directory path for counting all .py files in that directory;')
        print('an input containing only a dot "." would be considered as current work directory;')
        print('an empty input would make the program exit;')
        path_str = input('Your input: ')
        if path_str == '':
            return None
        path = Path(path_str)
        if path.exists():
            return path
        else:
            print('Invalid file path; please retry.')
            print()


def count_path(path: Path) -> dict:
    """Count files' lines in a given dir path
    or Count file's lines for a given file path
    :param path: dir path or file path
    :return dictionary containing file's name and its count"""
    result_dict = dict()
    if path.is_file():
        result_dict[str(path)] = count_single_file(path)
    elif path.is_dir():
        for py_file_path in list(path.glob('**/*.py')):
            result_dict[str(py_file_path)] = count_single_file(py_file_path)
    return result_dict


def print_result(result_dict: dict) -> None:
    """Print out the count from a given dictionary
    :param result_dict: data dictionary"""
    for file in result_dict:
        print('--------------------')
        print(file)
        for count in result_dict[file]:
            print('The number of lines of {} is {}.'.format(count.split(sep='_')[0], result_dict[file][count]))


def count_single_file(file_path: Path) -> dict:
    """Counting useful lines
    :param file_path: user-input file path
    :return count of different types of lines as a dictionary"""
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
    file.close()
    return {
        'useful_line_sum': useful_line_sum,
        'comment_line_sum': comment_line_sum,
        'blank_line_sum': blank_line_sum,
        'docstring_line_sum': docstring_line_sum
        }
