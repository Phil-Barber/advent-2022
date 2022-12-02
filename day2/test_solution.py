import pytest

from solution import Move, Result, check_result, main

example_input = [
    ("A", "Y"),
    ("B", "X"),
    ("C", "Z"),
]


def test_example_input():
    assert main(example_input) == 15


@pytest.mark.parametrize(
    "in_, out",
    (
        ((Move.rock, Move.paper), Result.win),
        ((Move.paper, Move.scissors), Result.win),
        ((Move.scissors, Move.rock), Result.win),
        ((Move.rock, Move.rock), Result.draw),
        ((Move.paper, Move.paper), Result.draw),
        ((Move.scissors, Move.scissors), Result.draw),
        ((Move.rock, Move.scissors), Result.lose),
        ((Move.scissors, Move.paper), Result.lose),
        ((Move.paper, Move.rock), Result.lose),
    ),
)
def test_check_result(in_, out):
    assert check_result(*in_) == out
