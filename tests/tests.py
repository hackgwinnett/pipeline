import client

arr = []
field1 = ["field1", "value1"]
field2 = ["field2", "value2"]
field3 = ["field3", "value3"]
arr.append(field1)
arr.append(field2)
arr.append(field3)

address = "http://127.0.0.1:5000"
args = client.create_add_args(arr, "temppass", "tempfilename")
client.send(address, args)
