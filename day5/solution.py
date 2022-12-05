import dataclasses
import pprint
import re
import typing


class Stack:
    """A stack of crates, top crate is 1st."""

    def __init__(self, *raw_crates: str) -> None:
        crates = tuple(crate for crate in raw_crates if crate != " ")
        self.crates = crates

    def __repr__(self) -> str:
        return f"Stack: {self.crates}"

    def __eq__(self, other: "Stack") -> bool:
        return isinstance(other, self.__class__) and self.crates == other.crates


Stacks = list[Stack]


@dataclasses.dataclass
class Instruction:
    """An instruction to perform."""

    num_to_move: int
    source_stack: int
    target_stack: int


def main(grid_and_instructions: list[str]) -> str:
    stacks, instructions = parse_input(grid_and_instructions)
    for instruction in instructions:
        pprint.pprint(stacks)
        print(instruction)
        stacks = perform_instruction(stacks, instruction)
    return "".join(stack.crates[0] for stack in stacks)


def parse_input(grid_and_instructions: list[str]) -> tuple[Stacks, list[Instruction]]:
    stacks_hoz: list[list[str]] = []
    instructions = []

    is_stacks = True
    for line in grid_and_instructions:
        if not line:
            transposed = zip(*stacks_hoz)
            stacks = [Stack(*crates) for crates in transposed]
            continue
        if is_stacks:
            if re.match(r"(\s\d\s\s)+", line):
                is_stacks = False
                continue
            stacks_hoz.append(parse_stacks_line(line))
        else:
            maybe_instruction = parse_instruction_line(line)
            if maybe_instruction:
                instructions.append(maybe_instruction)
    return stacks, instructions


def parse_stacks_line(stacks_str: str) -> list[str]:
    return [stacks_str[idx + 1] for idx in range(0, len(stacks_str), 4)]


def parse_instruction_line(instruction_str: str) -> typing.Optional[Instruction]:
    match = re.match(r"move (\d+) from (\d) to (\d)", instruction_str)
    if match:
        return Instruction(
            int(match.group(1)),
            int(match.group(2)) - 1,
            int(match.group(3)) - 1,
        )
    return None


def perform_instruction(stacks: Stacks, instruction: Instruction) -> Stacks:
    source_crates = stacks[instruction.source_stack].crates
    mover, new_source_crates = (
        source_crates[0 : instruction.num_to_move],
        source_crates[instruction.num_to_move :],
    )
    new_target_crates = [*mover, *stacks[instruction.target_stack].crates]
    stacks[instruction.source_stack] = Stack(*new_source_crates)
    stacks[instruction.target_stack] = Stack(*new_target_crates)
    return stacks


def input_lines() -> list[str]:
    with open("input") as input_file:
        return list(input_file.readlines())


if __name__ == "__main__":
    inputs = input_lines()
    inputs = [line[:-1] for line in inputs if line[0]]
    answer = main(inputs)
    print(f"Answer: {answer}")
