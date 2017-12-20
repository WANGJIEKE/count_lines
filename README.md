# Count_Lines
## 0x0 Introduction
A simple Python program counting "useful" lines in .py files.

The definition of "useful" line is that the line is **NOT** a comment, a docstring, or blank.
## 0x1 How to use
You can enter either a file path or a directory path;

(if you enter a directory path, the program will **recursively** count all .py files in that directory and all of its sub-directories)

**Notice: the blank new line at the end of each file would not be counted**
## 0x2 Example
For following file whose path is `/foo/bar.py`
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