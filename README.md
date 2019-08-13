# te

Short for touch-enumerate (as in GNU coreutils' `touch`).

## Description

`te` creates an enumeration of files in a directory from an ordered
(newline-separated) list of names passed as input.

## Installation

```bash
$ git clone https://github.com/monoflo/te
$ cd te && pip3 install .  # or add the `-e` flag to symlink
```

## Usage Examples

### Standard input

```bash
$ echo -e "a\nb\nc" | te
$ tree .
.
├── 0_a.txt
├── 1_b.txt
└── 2_c.txt

0 directories, 3 files
```

### File input specifying directory and extension

Example file `fruits.txt`:

```
apple
blueberry
cherry
dragonfruit
elderberry
fig
grapefruit
honeyberry
jackfruit
kumquat
lemon
mango
```

Invocation:

```bash
$ te fruits.txt -d fruits/ -e fruit
$ tree fruits/
fruits/
├── 00_apple.fruit
├── 01_blueberry.fruit
├── 02_cherry.fruit
├── 03_dragonfruit.fruit
├── 04_elderberry.fruit
├── 05_fig.fruit
├── 06_grapefruit.fruit
├── 07_honeyberry.fruit
├── 08_jackfruit.fruit
├── 09_kumquat.fruit
├── 10_lemon.fruit
└── 11_mango.fruit

0 directories, 12 files
```

## Motivation

I wrote this script on a whim, then wanted to learn how to create a package.

This is the result!

## Contributing

Should you find this script useful and make some edits of your own, feel free to
fork the project and send a pull request. I'll be happy to review and merge new
features.

There are plenty of ways that it could be customized and extended, and this is a
very beginner-friendly codebase.
