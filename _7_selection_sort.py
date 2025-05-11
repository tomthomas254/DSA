numbers = [8,4,6,2,1,9,2,4]

def selection_sort(list):
    """
    Takes O(n2)
    """
    sorted_list = []
    print("%-25s %-25s" %(list, sorted_list))

    for i in range(0, len(list)):
        index_to_move = index_of_min(list)
        sorted_list.append(list.pop(index_to_move))
        print("%-25s %-25s" %(list, sorted_list))

    return sorted_list

def index_of_min(list):
    min_index = 0
    for i in range(1, len(list)):
        if list[i] < list[min_index]:
            min_index = i
    return min_index

print(selection_sort(numbers))