import requests

'''
    raw_arr = 2d array of size [n][2]
    arr[0][0] = field 1, arr[0][1] = value 1
    arr[1][0] = field 2, arr[1][1] = value 2
    arr[2][0] = field 3, arr[2][1] = value 3
    .....
    arr[n][0] = field n, arr[n][1] = value n
'''


def create_add_args(filename, password=None):
    headers = {"command": "add",
               "filename": str(filename),
               "password": str(password),
               "Accept": "text/plain"}
    return headers


def create_dir_args(dirname, password=None):
    headers = {"command": "add_dir",
               "filename": dirname,
               "password": str(password)}
    return headers


def create_read_args(filename, password=None):
    return {"command": "read",
            "filename": str(filename),
            "password": str(password)}


def create_read_dir_args(dirname, password=None):
    return {"command": "read_dir",
            "filename": str(dirname),
            "password": str(password)}


def send(address, args, data=None):
    r = requests.post(address, headers=args, json=data)
    return r.text


def parse(raw, field):
    arr = raw.split(",")
    for term in arr:
        if field + ":" in term:
            return term.split(":")[1]
    return "client error - field not found: " + field
