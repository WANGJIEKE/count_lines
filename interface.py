#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created with PyCharm
# @Time    : 11/14/17 5:07 PM
# @Author  : Tongjie Wang

import count


def user_interface():
    try:
        path = count.get_path()
        if path is None:
            return
        result_dict = count.count_path(path)
        count.print_result(result_dict)
    except OSError:
        print('An error occurred when processing files.')


if __name__ == '__main__':
    user_interface()
