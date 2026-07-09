from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

try:
    import pulp
except ImportError as exc:
    raise SystemExit(
        "Missing dependency 'pulp'. Install with: pip install pulp"
    ) from exc


@dataclass
class PuzzleLine:
    manual: str
    buttons: List[Tuple[int, ...]]
    target: Tuple[int, ...]


def parse_line(line: str) -> PuzzleLine:
    parts = line.split(" ")
    manual = parts[0].replace("[", "").replace("]", "")

    buttons: List[Tuple[int, ...]] = []
    for token in parts[1:-1]:
        indices = token.replace("(", "").replace(")", "")
        if not indices:
            buttons.append(tuple())
            continue
        buttons.append(tuple(int(x) for x in indices.split(",")))

    target = tuple(int(x) for x in parts[-1].replace("{", "").replace("}", "").split(","))
    return PuzzleLine(manual=manual, buttons=buttons, target=target)


def load_data(path: Path) -> List[PuzzleLine]:
    return [parse_line(line.strip()) for line in path.read_text().splitlines() if line.strip()]


def build_matrix(buttons: List[Tuple[int, ...]], dim: int) -> List[List[int]]:
    matrix = [[0 for _ in range(len(buttons))] for _ in range(dim)]
    for j, idxs in enumerate(buttons):
        for i in idxs:
            matrix[i][j] = 1
    return matrix


def quick_infeasible_checks(matrix: List[List[int]], target: Tuple[int, ...]) -> bool:
    # If a target coordinate needs >0 but no button can ever touch it, impossible.
    for i, value in enumerate(target):
        if value > 0 and sum(matrix[i]) == 0:
            return True
    return False


def solve_min_presses(line: PuzzleLine) -> int:
    dim = len(line.target)
    matrix = build_matrix(line.buttons, dim)

    if quick_infeasible_checks(matrix, line.target):
        raise ValueError(f"Infeasible target: {line.target}")

    prob = pulp.LpProblem("day10_part2", pulp.LpMinimize)

    vars_x = [
        pulp.LpVariable(
            f"x_{j}",
            lowBound=0,
            upBound=max(line.target),
            cat=pulp.LpInteger,
        )
        for j in range(len(line.buttons))
    ]

    # Objective: minimize total presses.
    prob += pulp.lpSum(vars_x)

    # Coordinate-wise exact joltage constraints.
    for i, rhs in enumerate(line.target):
        prob += pulp.lpSum(matrix[i][j] * vars_x[j] for j in range(len(vars_x))) == rhs

    status = prob.solve(pulp.PULP_CBC_CMD(msg=False))
    if pulp.LpStatus[status] != "Optimal":
        raise ValueError(f"No optimal solution for target {line.target}, status={pulp.LpStatus[status]}")

    return int(pulp.value(prob.objective))


def part2_total(lines: List[PuzzleLine]) -> int:
    total = 0
    for idx, line in enumerate(lines, start=1):
        presses = solve_min_presses(line)
        total += presses
        print(f"Line {idx}: {presses}")
    return total


def main() -> None:
    base = Path(__file__).parent
    input_path = base / "input.txt"
    test_path = base / "testInput.txt"

    test_lines = load_data(test_path)
    input_lines = load_data(input_path)

    #print("Test total:", part2_total(test_lines))
    print("Input total:", part2_total(input_lines))


if __name__ == "__main__":
    main()
