"""
Merge Sort
Python 3.5
Auxillary Arrays - High Memory Usage
Moderate Time Complexity: O(n * lg n)

Jesse Wyatt
April 2017
"""

def msort(arr):
    """Returns a sorted array."""
    # Recurrance base-case
    if len(arr) <= 1:
        return arr
    else:
        # Split
        key = len(arr) // 2
        lwr = arr[:key]
        upr = arr[key:]
        # Recurrance
        lwr = msort(lwr)
        upr = msort(upr)
        # Greedy merge with 2-finger indexing
        merged = []
        i, j = 0, 0
        while i < len(lwr) and j < len(upr):
            if lwr[i] <= upr[j]:
                merged.append(lwr[i])
                i += 1
            else:
                merged.append(upr[j])
                j += 1
        if i < len(lwr):
            merged.extend(lwr[i:])
        elif j < len(upr):
            merged.extend(upr[j:])
        return merged

if __name__ == '__main__':
    print(msort([5,6,4,8,9,3,4,6,7]))