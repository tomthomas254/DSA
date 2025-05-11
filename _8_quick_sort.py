def quick_sort(list):
    """
    best case : O(n logn)- depends on pivot chosed
    worst case : O(n2)
    """
    if len(list) <=1:
        return list
    
    less_than_pivot = []
    greater_than_pivot = []

    pivot = list[0]

    for item in list[1:]:
        if item <= pivot:
            less_than_pivot.append(item)
        else:
            greater_than_pivot.append(item)
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

list = [5,2,3,6,8,2,9,2,32,54]
print(quick_sort(list))