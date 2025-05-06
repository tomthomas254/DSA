def merge_sort(list):
    """
    Sorts a list in ascending order.
    Returns a new sorted list.

    Divide : Find the midpoint of the list and divide into sublist.
    Conquer : Recursively sort the sublist created in previous step
    Combine : Merge the sorted sublists created in the previous list
    Runs in O(kn log n) time
    without slice operation actual run time = O(n log n)
    space complexity -> O(n)
    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)

def split(list):
    """
    Runs in O(k log n) time
    k- for slice operation:O(k), k-> sliced size
    """
    mid = len(list)//2
    left = list[:mid] #mid not included
    right = list[mid:]

    return left, right

def merge(left, right):
     """
    Runs in O(n) time
    
    """
    l = []
    i = 0 
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1


    while i < len(left):
        l.append(left[i])
        i+=1

    while j < len(right):
        l.append(right[j])
        j+=1

    return l

def verify_sorted(list):
    n = len(list)
     
    if n == 0 or n==1:
        return True

    return list[0] <= list[1] and verify_sorted(list[1:])

alist = [7,43,72,3,4,7,1,8,9]

print(verify_sorted(alist))
print(merge_sort(alist))
print(verify_sorted(merge_sort(alist)))