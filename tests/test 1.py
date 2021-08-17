import client
import json


def main():
    # set address (localhost address shown here for debugging server):
    address = "http://127.0.0.1:5000"

    # set file contents in a 2D array by appending 1D arrays to a list:
    with open("files/test.json", "r") as file:
        content = json.load(file)

    # create the files on the server side:
    createfile1 = client.create_add_args("file_1.json", "test_password_1")
    createfile2 = client.create_add_args("file_2.json", "test_password_2")
    client.send(address, createfile1, json.dumps(content["file1content"]))
    client.send(address, createfile2, json.dumps(content["file2content"]))

    # test server side password verification:
    correct_args = client.create_read_args("file_1.json", "test_password_1")
    faulty_args = client.create_read_args("file_1.json", "wrong_pass")
    print(client.send(address, correct_args))
    print(client.send(address, faulty_args))

    # get raw content and read specific fields:
    content = client.send(address, correct_args)
    print(client.parse(content, "field1"))
    print(client.parse(content, "field2"))
    print(client.parse(content, "field3"))


if __name__ == '__main__':
    main()
