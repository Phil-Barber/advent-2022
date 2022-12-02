import collections
import enum


class Move(enum.Enum):
    rock = 1
    paper = 2
    scissors = 3


class Opponent(enum.Enum):
    A = Move.rock
    B = Move.paper
    C = Move.scissors


class Player(enum.Enum):
    X = Move.rock
    Y = Move.paper
    Z = Move.scissors


class Result(enum.Enum):
    win = 6
    draw = 3
    lose = 0


def check_result(opp: Move, play: Move) -> Result:
    if opp == play:
        return Result.draw
    return (
        Result.win
        if (
            (play is Move.rock and opp is Move.scissors)
            or (play is Move.paper and opp is Move.rock)
            or (play is Move.scissors and opp is Move.paper)
        )
        else Result.lose
    )


def main(rounds: list[tuple[str, str]]) -> int:
    opp_play_rounds = [
        (getattr(Opponent, a).value, getattr(Player, b).value) for a, b in rounds
    ]
    result_total = sum(check_result(*round).value for round in opp_play_rounds)
    move_total = sum(play.value for opp, play in opp_play_rounds)
    return result_total + move_total


def input_lines() -> list[str]:
    with open("input") as input_file:
        return list(input_file.readlines())


if __name__ == "__main__":
    inputs = input_lines()
    inputs = [tuple(line[:-1].split(" ")) for line in inputs if line[0]]
    answer = main(inputs)
    print(f"Answer: {answer}")
