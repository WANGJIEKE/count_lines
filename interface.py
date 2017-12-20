#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created with PyCharm
# @Time    : 11/14/17 5:07 PM
# @Author  : Tongjie Wang

import count


def user_interface():
    path = count.get_path()
    result_dict = None
    if path is None:
        return
    try:
        result_dict = count.count_path(path)
    except count.UnableToCountError as e:
        print('--------------------')
        print(f'Unable to count file at path {e.path}')
    finally:
        count.print_result(result_dict)


if __name__ == '__main__':
    user_interface()
