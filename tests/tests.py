import client

# set address (localhost address shown here for debugging server):
address = "http://127.0.0.1:5000"

# set file contents in a 2D array by appending 1D arrays to a list:
file1content = []
field1 = ["field1", "file 1 content 1"]
field2 = ["field2", "file 1 content 2"]
field3 = ["field3", "file 1 content 3"]
file1content.append(field1)
file1content.append(field2)
file1content.append(field3)

file2content = []
_field1 = ["field1", "file 2_content 1"]
_field2 = ["field2", "file 2 content 2"]
_field3 = ["field3", "file 2 content 3"]
file2content.append(_field1)
file2content.append(_field2)
file2content.append(_field3)

# create the files on the server side:
args1 = client.create_add_args(file1content, "test_password_1", "file_1")
args2 = client.create_add_args(file2content, "test_password_2", "file_2")
client.send(address, args1)
client.send(address, args2)

# test server side password verification:
correct_args = client.create_read_args("file_1", "test_password_1")
faulty_args = client.create_read_args("file_1", "wrong_pass")
print(client.send(address, correct_args))
print(client.send(address, faulty_args))

# get raw content and read specific fields:
content = client.send(address, correct_args)
print(client.parse(content, "field1"))
print(client.parse(content, "field2"))
print(client.parse(content, "field3"))
