def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) — checks each adjacent pair once.
    Memory usage: O(1) — constant extra space.
    """
    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            return False
    return True
