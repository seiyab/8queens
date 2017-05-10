import operator as op
from functools import reduce
from itertools import chain

def main():
    for ans in solve():
        show(ans)
        break

def solve(length=8):
    def valid(x, y, queens):
        return reduce(op.and_, (not(xq==x or yq==y or xq-yq==x-y or xq+yq==x+y) for xq, yq in queens), True)

    def solve_row(i_row, queens):
        if i_row==length:
            yield queens
        else:
            for y in range(length):
                yield from chain(*(solve_row(i_row+1, queens + [(i_row, y)]) for y in range(length) if valid(i_row, y, queens)))
    yield from solve_row(0, [])


def show(queens):
    sorted_queens = sorted(queens, key=lambda x: x[1])
    for queen in sorted_queens:
        x, _ = queen
        row = '.'*x + '*' + '.'*(len(sorted_queens)-x-1)
        print(row)

if __name__ == '__main__':
    main()
