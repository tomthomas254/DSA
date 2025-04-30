def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i 

    return False

arr = [3,5,6,2,8,9,1]
key = 8

result = linear_search(arr, key)

if result:
    print('Value', key, 'fount at index', result)

else:
    print('Value', key, 'not found')