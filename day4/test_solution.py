import pytest

from solution import (Assignment, AssignmentPair,
                      assignment_contians_or_contained_in, main)

example_input = [
    ("2-4", "6-8"),
    ("2-3", "4-5"),
    ("5-7", "7-9"),
    ("2-8", "3-7"),
    ("6-6", "4-6"),
    ("2-6", "4-8"),
]


def test_main_example() -> None:
    assert main(example_input) == 2


@pytest.mark.parametrize(
    "assignment_pair, expected",
    [
        (example_input[0], False),
        (example_input[1], False),
        (example_input[2], False),
        (example_input[3], True),
        (example_input[4], True),
        (example_input[5], False),
        (("51-51", "52-68"), False),
        (("66-66", "9-65"), False),
    ],
)
def test_assignment_contains_or_contained_in_assignment(
    assignment_pair: AssignmentPair, expected: bool
) -> None:
    assert (
        assignment_contians_or_contained_in(
            Assignment(assignment_pair[0]), Assignment(assignment_pair[1])
        )
        == expected
    )


@pytest.mark.parametrize(
    "assignment_pair, expected",
    [
        (example_input[0], False),
        (example_input[1], False),
        (example_input[2], True),
        (example_input[3], True),
        (example_input[4], True),
        (example_input[5], True),
        (("51-51", "52-68"), False),
        (("66-66", "9-65"), False),
    ],
)
def test_assignment_overlaps(assignment_pair: AssignmentPair, expected: bool) -> None:
    assert (
        Assignment(assignment_pair[0]).overlaps(Assignment(assignment_pair[1]))
        == expected
    )
