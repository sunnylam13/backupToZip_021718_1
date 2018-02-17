# Scratch File

## Saturday, February 17, 2018 3:08 PM

about os.path.basename() (vs. os.path.dirname())

Both functions use the os.path.split(path) function to split the pathname path into a pair; (head, tail).

The os.path.dirname(path) function returns the head of the path.

	E.g.: The dirname of '/foo/bar/item' is '/foo/bar'.

The os.path.basename(path) function returns the tail of the path.

	E.g.: The basename of '/foo/bar/item' returns 'item'

[Source](https://stackoverflow.com/questions/22272003/what-is-the-difference-between-os-path-basename-and-os-path-dirname)

## Saturday, February 17, 2018 3:40 PM

Future variants

* walk a directory tree and zip only files with certain extensions

* walk a directory tree and zip every file except certain extensions

* find the folder in a directory tree that has the greatest number of files or the folder that uses the most disk space

to do this simply requires more conditional checks during the loops



