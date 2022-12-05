import typing

import pytest

from solution import (Instruction, Stack, Stacks, main, parse_input,
                      parse_instruction_line, parse_stacks_line,
                      perform_instruction)

example_input = [
    "    [D]    ",
    "[N] [C]    ",
    "[Z] [M] [P]",
    " 1   2   3",
    "",
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2",
]
example_stacks = [
    Stack("N", "Z"),
    Stack("D", "C", "M"),
    Stack("P"),
]
example_instructions = [
    Instruction(1, 1, 0),
    Instruction(3, 0, 2),
    Instruction(2, 1, 0),
    Instruction(1, 0, 1),
]


def test_main_example_input() -> None:
    assert main(example_input) == "CMZ"


def test_parse_input_example_input() -> None:
    result_stacks, result_instructions = parse_input(example_input)
    assert result_stacks == example_stacks
    assert result_instructions == example_instructions


@pytest.mark.parametrize(
    "line, crates",
    (
        ("    [D]    ", [" ", "D", " "]),
        ("[N] [C]    ", ["N", "C", " "]),
        ("[Z] [M] [P]", ["Z", "M", "P"]),
    ),
)
def test_parse_stacks_line(line: str, crates: list[str]) -> None:
    assert parse_stacks_line(line) == crates


@pytest.mark.parametrize(
    "line, instruction",
    (
        ("move 1 from 2 to 1", Instruction(1, 1, 0)),
        ("move 3 from 1 to 3", Instruction(3, 0, 2)),
        ("move 2 from 2 to 1", Instruction(2, 1, 0)),
        ("move 1 from 1 to 2", Instruction(1, 0, 1)),
        ("move 11 from 1 to 2", Instruction(11, 0, 1)),
        ("move from 1 ", None),
    ),
)
def test_parse_instruction_line(
    line: str, instruction: typing.Optional[Instruction]
) -> None:
    assert parse_instruction_line(line) == instruction


stack_2 = [Stack("D", "N", "Z"), Stack("C", "M"), Stack("P")]
stack_3 = [Stack(), Stack("C", "M"), Stack("Z", "N", "D", "P")]
stack_4 = [Stack("M", "C"), Stack(), Stack("Z", "N", "D", "P")]
stack_5 = [Stack("C"), Stack("M"), Stack("Z", "N", "D", "P")]


@pytest.mark.parametrize(
    "stacks, instruction, out_stacks",
    (
        (example_stacks, example_instructions[0], stack_2),
        (stack_2, example_instructions[1], stack_3),
        (stack_3, example_instructions[2], stack_4),
        (stack_4, example_instructions[3], stack_5),
    ),
)
def test_perform_instruction(
    stacks: Stacks, instruction: Instruction, out_stacks: Stacks
) -> None:
    assert perform_instruction(stacks, instruction) == out_stacks
