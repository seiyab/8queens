from itertools import chain, islice
from time import time

def main():
    num_solution = None
    t = time()
    for i, ans in enumerate(islice(solve(8), num_solution)):
        show(ans)
        print('total {0:.6f}s'.format(time() - t))
        print('average {0:.6f}s'.format((time() - t) / (i+1)))


def solve(length):
    """length: int -> iter<[(int, int)]>
    solves "length" x "length" queen problem.
    each element of return: a solution for the problem.
    each element of a solution: a coordinate of a queen.
    """
    def valid(x, y, queens):
        """x: int -> y: int -> queens: [(int, int)] -> bool
        whether we can put a queen at ("x", "y") when "queens" are already put.
        """
        return all(xq!=x and yq!=y and xq-yq!=x-y and xq+yq!=x+y for xq, yq in queens)

    def solve_col(x, queens):
        """x: int -> queens: [(int, int)] -> iter<[(int, int)]>
        solves the problem assuming column i is already filled by "queens" for all i<"x".
        """
        if x==length:
            yield queens
        else:
            valid_ys = (y for y in range(length) if valid(x, y, queens))
            answers = (solve_col(x+1, queens + [(x, y)]) for y in valid_ys)
            yield from chain.from_iterable(answers)
    yield from solve_col(0, [])


def show(queens):
    sorted_queens = sorted(queens, key=lambda x: x[1])
    for queen in sorted_queens:
        x, _ = queen
        row = '. '*x + '* ' + '. '*(len(sorted_queens)-x-1)
        print(row)

if __name__ == '__main__':
    main()
