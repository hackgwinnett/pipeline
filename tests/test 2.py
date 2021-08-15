import client


def main():
    # Sets address for the localhost server
    address = "http://127.0.0.1:5000"

    # Set file contents in a 2D array by appending 1D arrays to a list:
    file1content = []
    field1 = ["field1", "file 1 content 1"]
    field2 = ["field2", "file 1 content 2"]
    field3 = ["field3", "file 1 content 3"]
    file1content.append(field1)
    file1content.append(field2)
    file1content.append(field3)

    # Creates a test directory to store files in, and then sends them to the server
    createdir = client.create_dir_args("testdir")
    print(client.send(address, createdir))

    # Creates file in the new test directory
    createfile = client.create_add_args(file1content, "testdir/file_1")
    print(client.send(address, createfile))

    # reads file from the test directory
    readdirectory = client.create_read_dir_args("testdir")
    print(client.send(address, readdirectory))


if __name__ == '__main__':
    main()
