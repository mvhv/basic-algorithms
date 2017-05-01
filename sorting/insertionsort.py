"""
Naive Insertion Sort
Python 3.5
In-place - Low Memory Usage
Quadratic Time Complexity: O(n^2)

Jesse Wyatt
April 2017
"""

def isort(arr):
    """Sort list in place"""
    for key in range(1, len(arr)):
        i = key
        while i > 0:
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
