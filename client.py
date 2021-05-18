'''
    raw_arr = 2d array of size [n][2]
    arr[0][0] = field 1, arr[0][1] = value 1
    arr[1][0] = field 2, arr[1][1] = value 2
    arr[2][0] = field 3, arr[2][1] = value 3
'''
def create_add_args(raw_arr, password):
    storage = "password:" + str(password)
    for i in range(len(raw_arr)):
        if (i < (len(raw_arr))):
            storage += "_"
        storage += str(raw_arr[i][0]) + ":" + str(raw_arr[i][1])
    return storage
