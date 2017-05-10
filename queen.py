import operator as op
from itertools import chain, islice
from time import time

def main():
    num_solution = 100
    t = time()
    for i, ans in enumerate(islice(solve(8), num_solution)):
        show(ans)
        print('total {}s'.format(time() - t))
        print('aberage {}s'.format((time() - t) / (i+1)))


def solve(length=8):
    def valid(x, y, queens):
        return all(not(xq==x or yq==y or xq-yq==x-y or xq+yq==x+y) for xq, yq in queens)

    def solve_row(i_row, queens):
        if i_row==length:
            yield queens
        else:
            valid_ys = (y for y in range(length) if valid(i_row, y, queens))
            answers = (solve_row(i_row+1, queens + [(i_row, y)]) for y in valid_ys)
            yield from chain.from_iterable(answers)
    yield from solve_row(0, [])


def show(queens):
    sorted_queens = sorted(queens, key=lambda x: x[1])
    for queen in sorted_queens:
        x, _ = queen
        row = '. '*x + '* ' + '. '*(len(sorted_queens)-x-1)
        print(row)

if __name__ == '__main__':
    main()
