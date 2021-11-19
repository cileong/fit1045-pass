"""
Insertion sort

Algorithm:
  1. Shift the current item to left until the item to left
     is at least as small as the current item.
     This extends the sorted part of the list.
     The size of the sorted part has grown by 1, or,
     the size of the unsorted part has decreased by 1.
  2. Repeat step 1 until the list is sorted.
     This happens when the sorted part has grown to the entire list,
     and the unsorted part has shrinked to nothing.
"""


def insert(k, arr):
    """ Insert item at index k into arr.
    arr: A list of comparable items.
    
    Time complexity:
    Best case : O(1), when arr[k-1] <= arr[k],
    Worst case: O(N), when arr[k] is the smallest item in arr,
    where N == len(arr).
    """
    while k>0 and arr[k-1]>arr[k]:
        arr[k-1], arr[k] = arr[k], arr[k-1]
        k -= 1
    return arr


def insertion_sort(arr):
    """ Sort the input array in non-decreasing order.
    arr: A list of comparable items.
    
    Time complexity:
    Best case : O(N), when arr is sorted in non-decreasing order,
    Worst case: O(N^2), when arr is sorted in non-increasing order,
    where N == len(arr).
    """
    N = len(arr)

    # O(N) * O(insert)
    # Best case : O(N) * O(1) = O(N)
    # Worst case: O(N) * O(N) = O(N^2)
    for i in range(1, N):
        arr = insert(i, arr)


if __name__ == '__main__':
    # The original list is modified.
    arr = [4, 7, 9, 2, 8]
    insertion_sort(arr)
    print(arr)

    # O(N^2) time
    arr = [5, 4, 3, 2, 1]
    insertion_sort(arr)
    print(arr)

    # O(1) time
    arr = [1, 2, 3, 4, 5]
    insertion_sort(arr)
    print(arr)
