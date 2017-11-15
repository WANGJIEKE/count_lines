# Count_Lines
A simple Python program counting "useful" lines in .py files.

The definition of "useful" line is that the line is **NOT** a comment, a docstring, or blank.

**Notice: the blank new line at the end of each file would not be counted (because actually there is no line there)**

Example:

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

Upcoming features:
- Multiple directories support
- Add exceptions handling