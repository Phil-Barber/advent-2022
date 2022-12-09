import copy
import dataclasses
import itertools
import typing


class Object(typing.Protocol):
    name: str
    size: int


@dataclasses.dataclass
class Dir:
    name: str
    children: list[Object] = dataclasses.field(default_factory=list)

    @property
    def size(self) -> int:
        return sum(child.size for child in self.children)

    def __repr__(self) -> str:
        return f"(Dir {self.name})"


@dataclasses.dataclass
class File:
    name: str
    size: int


Index = list[Dir]


@dataclasses.dataclass
class Cd:
    arg: str

    def perform(self, index_: Index) -> Index:
        index = copy.deepcopy(index_)
        if self.arg == "..":
            index.pop()
            return index
        if self.arg == "/":
            return [index[0]]
        current_dir = index[-1]
        try:
            new_dir = next(
                dir
                for dir in current_dir.children
                if isinstance(dir, Dir) and dir.name == self.arg
            )
        except StopIteration:
            new_dir = Dir(self.arg)
            new_dir.children.append(new_dir)
        index.append(new_dir)
        return index


@dataclasses.dataclass
class Ls:
    objects: list[Object] = dataclasses.field(default_factory=list)


Cmd = typing.Union[Cd, Ls]


def main(terminal_lines: list[str]) -> int:
    parsed_lines = map(parse_line, terminal_lines)
    root_dir = build_dir_tree(parsed_lines)
    all_dirs = get_all_dirs(root_dir)
    total_space = 70000000
    required_space = 30000000
    used_space = sum(dir.size for dir in all_dirs if dir.name == "/")
    unused_space = total_space - used_space
    required_space = required_space - unused_space
    return min(
        dir.size for dir in all_dirs if dir.name != "/" and dir.size >= required_space
    )


def build_dir_tree(parsed_lines: list[typing.Union[Cmd, Object]]) -> Dir:
    index: Index = [Dir("/")]
    for line in parsed_lines:
        current_dir = index[-1]
        if isinstance(line, Cd):
            index = line.perform(index)
        elif isinstance(line, (File, Dir)):
            current_dir.children.append(line)
    return index[0]


def parse_line(line: str) -> typing.Union[Cmd, Object]:
    parts = line.split(" ")
    if parts[0] == "$":
        if parts[1] == "cd":
            return Cd(parts[2])
        if parts[1] == "ls":
            return Ls()
    elif parts[0] == "dir":
        return Dir(parts[1])
    return File(parts[1], int(parts[0]))


def get_all_dirs(root: Dir) -> list[Dir]:
    return_dirs = [root]
    child_dirs = [child for child in root.children if isinstance(child, Dir)]
    if child_dirs:
        return_dirs += list(
            itertools.chain.from_iterable(get_all_dirs(child) for child in child_dirs)
        )
    return return_dirs


def input_lines() -> list[str]:
    with open("input") as input_file:
        return list(input_file.readlines())


if __name__ == "__main__":
    inputs = input_lines()
    inputs = [line[:-1] for line in inputs if line[0]]
    answer = main(inputs)
    print(f"Answer: {answer}")
