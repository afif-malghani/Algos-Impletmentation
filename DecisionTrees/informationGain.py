from entropy import getEntropy


def infoGain(y, y_left, y_right):
    return getEntropy(y)- getEntropy(y_left) -getEntropy(y_right)


