Wct is a Wizard for the Computer Tree, in other words, it is an alternative to `fd` or `find`, but less powerful. Despite its inferiority to its two competitors, wct is easier to learn because of its simple commands. With wct, you can moderate and search your computer tree.

#### Installation
At the moment, *wct* is not on PyPi, so you can't do `pip install wct`. Instead, you have to clone the project and use it as such. Clone it as follows:
```
git clone https://github.com/b4-b4/wct.git
```

#### Usage
The WCT commands are as follows:
```
python /path/to/wct.py <path> (<pattern> | <regex>) [-d | --delete]
```
All you really need to remember is this part:
```
... <path> (<pattern> | <regex>) [-d | --delete]
```
Let's see what this means:
- the `<path>` argument must be the path from which you want Wct to explore. In other words, it is the starting point or entry point of Wct.
- `<pattern>` can be a string that you want to find, for example "*a*". Note that *string* does not mean the string in the first degree that will be searched, but a word or letter that will be searched in a folder or file name. You may note that `<pattern>` can be `~` (`/home/you/` or `C:\Users\you\`), or `.` (current folder) or `/` (`/home/` or `C:\`).
- `<regex>` is as its name suggests, a [regex](https://en.wikipedia.org/wiki/Regular_expression). You can find out how to use it [here](https://docs.python.org/3/library/re.html).
- `-d` and `--delete` allow to delete the paths who was found. The program will offer you either to delete everything or to list with comma separated indexes the paths you don't want to lose. The indexes are provided next to the paths.
