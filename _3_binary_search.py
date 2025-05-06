"""
Time Complexity : O(log n)
"""
def binary_search(arr, key):
    left = 0 
    right = len(arr) - 1

    while left < right:
        mid=(left + right) // 2

        if arr[mid] == key:
            return mid

        if arr[mid] < key:
            left=mid + 1
        else:
            right = mid -1
    return False
    

arr = [1,2,3,4,5,6,7,8,9,10]
key = 8

result = binary_search(arr, key)

if result:
    print('Value', key, 'fount at index', result)

else:
    print('Value', key, 'not found')