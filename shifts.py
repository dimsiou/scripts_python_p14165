
def shifts(array):
    """print all array shifts"""
    if len(array) is 1:
        return [array]
    array_list = []
    for item in array:
        copy_array = array[:]
        copy_array.remove(item)
        new_lists = shifts(copy_array)
        for list in new_lists:
            list.insert(0, item)
            array_list.append(list)
    return array_list


print(len(shifts([3, 4, 5])), shifts([3, 4, 5]))
print(len(shifts([1, 2])), shifts([1, 2]))
