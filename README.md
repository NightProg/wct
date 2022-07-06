# wct
### Presentation
*Smwct*, for "*Search and Moderation Wizard for the Computer Tree*",
is, as its name indicates, a program whose mission is to help man in the search and moderation of his computer tree. More
exactly, *Smwct* allows two things: to search from one of the pre-suggested places a sequence of characters in all the folders, sub-folders and 
from the initial directory, chosen by the user, **or**, search and delete after confirmation all the folders, subfolders and
from the initial directory (always chosen by the user). It is a software coded only in Python and only dedicated to
Linux users.
### Cause
*Smwct* was designed to make it easier to find an item in a pre-suggested directory such as `/` or `/home/username/`, especially to
to get rid of all the files/folders left after uninstalling a program. It is also intended to replace `grep` which is a tool that I find
tool in my opinion.
## Technical
### Setting up Smwct on Linux
Before doing the following, make sure you have Python and Git installed correctly.

Once you have Python on your Linux distribution, run the following command at the "root" (`/home/username/`) to avoid 
complications when using *smwct*:
```
git clone https://github.com/b4-b4/smwct.git
```
The installation of the software is finished.
### Search
Theoretically, if you have *smwct* installed at the root of your tree (`/home/username/`), the procedure should be as follows:
```
cd
python smwct/run.py -s --starting your_character_string
```
By entering `python smwct/run.py` you tell the python interpreter to run the `run.py` program which is in the `smwct/` directory. Then, 
the first `-s` flag means that you want to run a search. The second flag `--starting` **must** be replaced by either of the following
following flags:
- `--root`: informs that you want to search at the absolute root of your computer, namely `/`.
- `--session`: informs that you want to search at the root of your "session", i.e. `/home/username/`.
- `--anywhere`: searches the absolute root and the root of your session (`--root` + `--session`). This command can take a long time, really.

Then `your_character_string` **must** be replaced by the element you want to search for in the second flag (`--session`, `--root` or `--anywhere`). Note that `your_character_string` is not the actual item being searched for, it is the item being searched for in the various folders, subfolders and files in the second flag. For example, this command line
```
python smwct/run.py -s --root a
```
might return
```
/etc/gra.o
/var/
/var/test/allocation/
```
because `etc/gra.o` contains an `a` in `gra.o`, `/var/` because `var` contains `a`, etc.
