import client
import json


def main():
    # Sets address for the localhost server
    address = "http://127.0.0.1:5000"

    with open("files/test.json", "r") as file:
        file1content = json.load(file)
        file1content = file1content["file1content"]

    # Creates a test directory to store files in, and then sends them to the server
    createdir = client.create_dir_args("testdir")
    print(client.send(address, createdir))

    # Creates file in the new test directory
    createfile = client.create_add_args("testdir/file_1.json")
    print(client.send(address, createfile, json.dumps(file1content)))

    # returns the existing files in a directory
    readdirectory = client.create_read_dir_args("testdir")
    print(client.send(address, readdirectory))

    # reads file from server
    readfile = client.create_read_args("testdir/file_1.json")
    print(client.send(address, readfile))


if __name__ == '__main__':
    main()
