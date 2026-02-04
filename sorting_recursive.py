import random


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: O(n + m) because every element in both arrays is visited only one and there are no nested loops
    TODO: Memory usage: O(n + m) because a new lsit is created to store the merged result
    """
    # create empty result array and two pointers
    sorted_items = []
    i = j = 0

    # while loop that iterates until one of the two lists are empty
    while i < len(items1) and j < len(items2):
        # if the item in the left array is less then or equal to the right
        if items1[i] <= items2[j]:
            # add the left item to result array and increase the iteration on the left array
            sorted_items.append(items1[i])
            i += 1
        else:
            # if the right item is bigger, add the item to the list and increase the iteration on the right side
            sorted_items.append(items2[j])
            j += 1

    # add any remain items
    sorted_items.extend(items1[i:])
    sorted_items.extend(items2[j:])

    # return sorted array
    return sorted_items


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: O(n log n) because using the python sort method is O((n/2) log (n/2)) and we use it twice
    TODO: Memory usage: O(n) because any additional list is O(n)"""
    # split the list into two smaller lists
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    # use the built in python method to sort the lists
    left.sort()
    right.sort()

    # use the helper function to merge the left and right sorted lists
    return merge(left, right)


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: O(n log n) because on every recursive call splits the list roughly in half
    TODO: Memory usage: O(n) because merge sort is not in place and create many arrays
    """

    # base case, if the list has zero or 1 items, return
    if len(items) <= 1:
        return items

    # create a midpoint and split the inputted list
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    # recursively call the function on itself on both the left and right side
    left = merge_sort(left)
    right = merge_sort(right)

    # use merge helper function to combine sorted lists
    return merge(left, right)


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: O(n) as every item is searched once and it is linear
    TODO: Memory usage: O(1) as all the work is done in place.
    """
    # get a random index to use as our pivot
    r = random.randint(low, high)

    # move pivot to the end
    items[r], items[high] = items[high], items[r]

    # make the pivot the last item in the list for easy partioning
    pivot = items[high]
    # start our tracker at the first index and is eventually going to indicate where our pivot will be
    p = low

    # begin looping the list
    for current in range(low, high):
        # if the the current item is less than our pivot
        if items[current] < pivot:
            # swap the current item where our pivot tracker is and increase the tracker by one
            items[p], items[current] = items[current], items[p]
            p += 1

    # move pivot into final position and return it
    items[p], items[high] = items[high], items[p]
    return p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: O(n log n) as this is a standard recursive call stack as the array is being split
    TODO: Worst case running time: O(n^2) if pivot is largest or smallest element
    TODO: Memory usage: O(log n) as normal recursive depth is logarithmic
    """

    # base case if the list has length of 0 or 1
    if low >= high:
        return

    # partition the list with the helper method to get our pivot
    p = partition(items, low, high)

    # recursively sort the sublists to the left and right of the pivot
    quick_sort(items, low, p - 1)
    quick_sort(items, p + 1, high)
