import pytest

from solution import Move, Result, check_result, main

example_input = [
    ("A", "Y"),
    ("B", "X"),
    ("C", "Z"),
]


def test_example_input():
    assert main(example_input) == 12


@pytest.mark.parametrize(
    "in_, out",
    (
        ((Move.rock, Result.win), Move.paper),
        ((Move.rock, Result.draw), Move.rock),
        ((Move.rock, Result.lose), Move.scissors),
        ((Move.paper, Result.win), Move.scissors),
        ((Move.paper, Result.draw), Move.paper),
        ((Move.paper, Result.lose), Move.rock),
        ((Move.scissors, Result.win), Move.rock),
        ((Move.scissors, Result.draw), Move.scissors),
        ((Move.scissors, Result.lose), Move.paper),
    ),
)
def test_check_result(in_, out):
    assert check_result(*in_) == out
