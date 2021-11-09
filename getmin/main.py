
def get_minimum(array):
    if len(array) == 0:
        raise ValueError("The array can not be empty")
    i_max = len(array) - 1
    i_min = 0
    while i_min != i_max:
        i_mid = (i_min + i_max) // 2
        if array[i_mid] < array[i_mid + 1]:
            i_max = i_mid
        else:
            i_min = i_mid + 1
    return array[i_min]
