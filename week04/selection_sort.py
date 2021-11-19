"""
Selection sort

Algorithm:
  1. Find the smallest item in unsorted part of list.
  2. Swap it with the 1st item in unsorted part.
  3. Now, the 1st slot is sorted.
     The size of the sorted part has grown by 1, or,
     the size of the unsorted part has decreased by 1.
  4. Repeat steps 1-3 until the list is sorted.
     The list is sorted when the sorted part has grown to the entire list,
     and the unsorted part has shrinked to nothing.
"""


def selection_sort(arr):
    """ Sort the input array in non-decreasing order.
    arr: A list of comparable items.
    
    Time complexity: O(N), where N == len(arr).
    """
    N = len(arr)

    # Before the i-th iteration of this loop:
    # arr[0:i] is sorted
    # Note: i starts from 0, arr[0:0] = [] is sorted.
    for i in range(N):

        # Find the index of the smallest item in
        # unsorted part.
        min_idx = i
        for j in range(i+1, N):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the 1st item in unsorted part with
        # the smallest item in unsorted part.
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    # After the i-th iteration of this loop:
    # arr[0:i+1] is sorted.

    # At the last iteration, i = N-1, so at termination,
    # arr[0:(N-1)+1] = arr[0:N] = arr is sorted.


if __name__ == '__main__':
    # The original list is modified.
    arr = [4, 7, 9, 2, 8]
    selection_sort(arr)
    print(arr)

    arr = [5, 4, 3, 2, 1]
    selection_sort(arr)
    print(arr)

    arr = [1, 2, 3, 4, 5]
    selection_sort(arr)
    print(arr)