"""
Sorting Algorithm Testing
"""

import random
import insertionsort
import mergesort

def randarray(leng):
    arr = []
    for i in range(leng):
        arr.append(random.randint(0, 100))
    return arr


def test_insertion(arr):
    print(arr)
    insertionsort.isort(arr)
    print(arr)


def test_merge(leng):
    arr = randarray(leng)
    print(arr)
    print(mergesort.msort(arr))


if __name__ == '__main__':
    test_merge(20)
