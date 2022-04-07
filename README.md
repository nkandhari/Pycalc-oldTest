# Pycalc
Python calculator for github workshop

7 Apr 2022: Within ATOM, I've accessed Pycalc after cloning it in the terminal.

Edit pycalc.py

`git status`

Before adding/committing anything, do:

`git diff`

This shows difference in latest file and the previous version of the file.

To check file specific changes in case you have changed multiple files:

`git diff README.md`

`git diff pycalc.py`

Check all previous versions of file:
`git log`

gives you hashes, you can switch a previous version:

git checkout 708eca8ee7af5a9a17a326484855ef92f0ff154f

and switch back to main version with latest changes:

git switch main

To find which branch I am at:

`git branch`

# I have a detached head branch: https://www.cloudbees.com/blog/git-detached-head
```
git branch
* (HEAD detached at ddc03b9)
  master
```

If you are in detached head branch, to get back to master (attached state):

`git switch master`
