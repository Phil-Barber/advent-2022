import collections
import enum


class Move(enum.Enum):
    rock = 1
    paper = 2
    scissors = 3


Beats = {
    Move.rock: Move.scissors,
    Move.scissors: Move.paper,
    Move.paper: Move.rock,
}
Loses = {winning: losing for losing, winning in Beats.items()}


class Opponent(enum.Enum):
    A = Move.rock
    B = Move.paper
    C = Move.scissors


class Result(enum.Enum):
    win = 6
    draw = 3
    lose = 0


class Player(enum.Enum):
    X = Result.lose
    Y = Result.draw
    Z = Result.win


def check_result(opp: Move, play: Result) -> Move:
    if play is Result.draw:
        return opp
    if play is Result.win:
        return Loses[opp]
    return Beats[opp]


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
