# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        
        return self.quickSortHelper(pairs, 0, len(pairs) - 1)



    def quickSortHelper(self, arr, s, e):
        if e - s + 1 <= 1:
            return arr
        
        left = s
        pivot = arr[e]

        for i in range(s, e):
            if arr[i].key < pivot.key:
                temp = arr[left]
                arr[left] = arr[i]
                arr[i] = temp
                left += 1
        temp = arr[left]
        arr[left] = pivot
        arr[e] = temp


        self.quickSortHelper(arr, s, left - 1)
        self.quickSortHelper(arr, left + 1, e)

        return arr