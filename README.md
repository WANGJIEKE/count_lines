# count_lines
## 0 Introduction / 简介
A simple Python program counting "useful" lines in .py files.
一个简单的计算.py文件中“有用”行数的小程序

The definition of "useful" line is that the line is **NOT** a comment, a docstring, or blank.
关于“有用”的定义如下：该行**不是**注释、文档字符串或空白
## 1 How to use / 如何使用
You can enter either a file path or a directory path;
你可以输入文件路径或者目录路径

(if you enter a directory path, the program will **recursively** count all .py files in that directory and all of its sub-directories)
（如果你输入的是目录，这个程序将会**递归地**将这个目录及其子目录的所有.py文件进行行数统计）

**Notice: the blank new line at the end of each file would not be counted**
**注意：文件最后的空白行不会被计入**
## 2 Example / 范例
For following file whose path is `/foo/bar.py`
对于路径为`/foo/bar.py`的文件
```python
#this is a comment

def some_function(par1: int) -> None:
    """This is docstring
    still docstring
    docstring ends here"""
    print('hello{}'.format(par1))  # print something

if __name__ == '__main__':
    some_function(5)
```
The output will be like
输出为
```text
Please enter a file path for counting single file;
or enter a directory path for counting all .py files in that directory;
an input containing only a dot "." would be considered as current work directory;
an empty input would make the program exit;
Your input: /foo/bar.py
--------------------
/foo/bar.py
The number of lines of useful is 4.
The number of lines of comment is 1.
The number of lines of blank is 2.
The number of lines of docstring is 3.
```
