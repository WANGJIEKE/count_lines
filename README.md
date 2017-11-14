# Count_Lines
A simple Python program counting "useful" lines in .py file.

The definition of "useful" line is that the line is **NOT** a comment, a docstring, or blank.

**Notice: the blank new line at the end of each file would not be counted (because actually there is no line there)**

Example:

For following codes,
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
Please enter a file path; an empty input would make the program exit;
Your input: <File Path>
The sum of useful lines is 4.
The sum of comment lines is 1.
The sum of blank lines is 2.
The sum of docstring lines is 3.
Total lines: 10
```
