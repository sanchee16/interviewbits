"""Follow thw directions below.

You are in an infinite 2D grid where you can move in any of the 8
directions.

(x,y) to
(x+1, y),
(x - 1, y),
(x, y+1),
(x, y-1),
(x-1, y-1),
(x+1,y+1),
(x-1,y+1),
(x+1,y-1)

You are given a sequence of points and the order in which you need
to cover the points. Give the minimum number of steps in which you
can achieve it. You start from the first point.

Example :

Input : [(0, 0), (1, 1), (1, 2)]
Output : 2
It takes 1 step to move from (0, 0) to (1, 1).
It takes one more step to move from (1, 1) to (1, 2).
"""


def coverpoints(X, Y):
    """Return the minimum number of steps that one needs to take.

    Inputs: X, Y - lists which contain x and y coordinates respectively.
    """
    length = len(X) if X > Y else len(Y)
    arr = 0
    if length == 1:
        return 0
    else:
        for i in range(1, length):
            if ((
                (X[i] < 0 and X[i - 1] < 0) or (X[i] > 0 and X[i - 1] > 0)) and
                ((Y[i] < 0 and Y[i - 1] < 0) or (Y[i] > 0 and Y[i - 1] > 0))):
                arr += max(abs(X[i] - X[i - 1]), abs(Y[i] - Y[i - 1]))
            else:
                if ((Y[i] < 0 and Y[i - 1] < 0) or (Y[i] > 0 and Y[i - 1] > 0)):
                    arr += max(abs(abs(X[i]) + abs(X[i - 1])),
                               abs(Y[i] - Y[i - 1]))
                elif ((X[i] < 0 and X[i - 1] < 0) or
                      (X[i] > 0 and X[i - 1] > 0)):
                    arr += max(abs(X[i] - X[i - 1]),
                               abs(abs(Y[i]) + abs(Y[i - 1])))
                else:
                    arr += max(abs(abs(X[i]) + abs(X[i - 1])),
                               abs(abs(Y[i]) + abs(Y[i - 1])))
        return abs(arr)

if __name__ == "__main__":
    val_x = raw_input("Enter list of numbers containing X coordinates.")
    val_y = raw_input("Enter list of numbers containing Y coordinates.")
    print coverpoints(map(int, val_x.split()), map(int, val_y.split()))
