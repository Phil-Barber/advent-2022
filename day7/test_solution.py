import typing

import pytest

from solution import (Cd, Cmd, Dir, File, Ls, Object, build_dir_tree,
                      get_all_dirs, main, parse_line)

example_input = [
    "$ cd /",
    "$ ls",
    "dir a",
    "14848514 b.txt",
    "8504156 c.dat",
    "dir d",
    "$ cd a",
    "$ ls",
    "dir e",
    "29116 f",
    "2557 g",
    "62596 h.lst",
    "$ cd e",
    "$ ls",
    "584 i",
    "$ cd ..",
    "$ cd ..",
    "$ cd d",
    "$ ls",
    "4060174 j",
    "8033020 d.log",
    "5626152 d.ext",
    "7214296 k",
]


def test_main_example_input() -> None:
    assert main(example_input) == 24933642


@pytest.mark.parametrize(
    "line, command",
    (
        ("$ cd /", Cd("/")),
        ("$ ls", Ls()),
        ("dir a", Dir("a")),
        ("14848514 b.txt", File("b.txt", 14848514)),
    ),
)
def test_parse_line(line: str, command: typing.Union[Cmd, Object]) -> None:
    assert parse_line(line) == command


def test_build_dir_tree_ls_block() -> None:
    """
    Example input produces:
    - / (dir)
      - a (dir)
        - e (dir)
          - i (file, size=584)
        - f (file, size=29116)
        - g (file, size=2557)
        - h.lst (file, size=62596)
      - b.txt (file, size=14848514)
      - c.dat (file, size=8504156)
      - d (dir)
        - j (file, size=4060174)
        - d.log (file, size=8033020)
        - d.ext (file, size=5626152)
        - k (file, size=7214296)
    """
    expected = Dir(
        "/",
        [
            Dir(
                "a",
                [
                    Dir("e", [File("i", 584)]),
                    File("f", 29116),
                    File("g", 2557),
                    File("h.lst", 62596),
                ],
            ),
            File("b.txt", 14848514),
            File("c.dat", 8504156),
            Dir(
                "d",
                [
                    File("j", 4060174),
                    File("d.log", 8033020),
                    File("d.ext", 5626152),
                    File("k", 7214296),
                ],
            ),
        ],
    )
    assert build_dir_tree(map(parse_line, example_input)) == expected


def test_get_all_dirs() -> None:
    root = Dir(
        "/",
        [
            Dir(
                "a",
                [
                    Dir("e", [File("i", 584)]),
                    File("f", 29116),
                    File("g", 2557),
                    File("h.lst", 62596),
                ],
            ),
            File("b.txt", 14848514),
            File("c.dat", 8504156),
            Dir(
                "d",
                [
                    File("j", 4060174),
                    File("d.log", 8033020),
                    File("d.ext", 5626152),
                    File("k", 7214296),
                ],
            ),
        ],
    )
    expected = [
        Dir(
            "/",
            [
                Dir(
                    "a",
                    [
                        Dir("e", [File("i", 584)]),
                        File("f", 29116),
                        File("g", 2557),
                        File("h.lst", 62596),
                    ],
                ),
                File("b.txt", 14848514),
                File("c.dat", 8504156),
                Dir(
                    "d",
                    [
                        File("j", 4060174),
                        File("d.log", 8033020),
                        File("d.ext", 5626152),
                        File("k", 7214296),
                    ],
                ),
            ],
        ),
        Dir(
            "a",
            [
                Dir("e", [File("i", 584)]),
                File("f", 29116),
                File("g", 2557),
                File("h.lst", 62596),
            ],
        ),
        Dir("e", [File("i", 584)]),
        Dir(
            "d",
            [
                File("j", 4060174),
                File("d.log", 8033020),
                File("d.ext", 5626152),
                File("k", 7214296),
            ],
        ),
    ]
    all_dirs = list(get_all_dirs(root))
    assert all_dirs == expected


@pytest.mark.parametrize(
    "dir_, size",
    (
        (
            Dir(
                "a",
                [
                    Dir("e", [File("i", 584)]),
                    File("f", 29116),
                    File("g", 2557),
                    File("h.lst", 62596),
                ],
            ),
            94853,
        ),
        (Dir("e", [File("i", 584)]), 584),
        (
            Dir(
                "d",
                [
                    File("j", 4060174),
                    File("d.log", 8033020),
                    File("d.ext", 5626152),
                    File("k", 7214296),
                ],
            ),
            24933642,
        ),
    ),
)
def test_dir_size(dir_: Dir, size: int) -> None:
    assert dir_.size == size
