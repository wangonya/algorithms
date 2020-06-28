def binary_search(data, target, low, high):
    if low > high:
        return False  # interval is empty - no match
    else:
        mid = (low+high) // 2
        if target == data[mid]:  # found match
            return True
        elif target < data[mid]:
            # recur to the portion left of the middle
            return binary_search(data, target, low, mid-1)
        else:
            # recur to the portion right of the middle
            return binary_search(data, target, mid+1, high)

