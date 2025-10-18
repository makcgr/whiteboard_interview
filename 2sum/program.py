from typing import List
from collections import defaultdict

def two_sum(arr: List[int], k: int) -> bool:
    dict = defaultdict(bool)
    for n in arr:
        if dict[k-n]:
            return True
        dict[n] = True
    return False


arr = [4, 7, 1, -3, 2]
print(two_sum(arr, 5))

arr = [3, 1, -2]
print(two_sum(arr, 5))
