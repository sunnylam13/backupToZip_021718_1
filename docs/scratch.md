# Scratch File

## Saturday, February 17, 2018 3:08 PM

about os.path.basename() (vs. os.path.dirname())

Both functions use the os.path.split(path) function to split the pathname path into a pair; (head, tail).

The os.path.dirname(path) function returns the head of the path.

	E.g.: The dirname of '/foo/bar/item' is '/foo/bar'.

The os.path.basename(path) function returns the tail of the path.

	E.g.: The basename of '/foo/bar/item' returns 'item'

[Source](https://stackoverflow.com/questions/22272003/what-is-the-difference-between-os-path-basename-and-os-path-dirname)

