def binary_search(data, target, low, high):
    """uses recursive binary search algorithm to find
    and return the target in entered data

    assumes data is sorted"""

    if low > high:  # empty list - no match (base case)
        print("target not in list")
    else:
        mid = (low+high)//2
        print(f"mid = {mid}")
        if target == data[mid]:  # found target
            print(f"data == {data}")
            print(f"target == {target}")
            print(f"found! {data[mid]}")
        elif data[mid] > target:  # recurse on left side
            high = mid-1
            binary_search(data, target, low, high)
        elif data[mid] < target:  # recurse on right side
            low = mid+1
            binary_search(data, target, low, high)

if __name__ == '__main__':
    data = list(map(int, input().strip().split(' ')))
    target = int(input().strip())
    low = 0
    high = len(data)-1

    binary_search(data, target, low, high)
