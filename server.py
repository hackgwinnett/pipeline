from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "api error - no args passed"

@app.route("/<raw>")
def parse(raw):
    args = str(raw).split(",")

    '''
        format (if add):
        args[0] = add
        args[1] = filename
        args[2] = password (first data field)
        args[3] = field:data
        args[4] = field:data
        args[5] = field:data
        etc...

        format (if read):
        args[0] = read
        args[1] = filename
        args[2] = password
        ...returns data in the file
    '''

    # debugging (server-side):
    output = ""
    for element in args:
        output += element + " "
        
    print(output)

    # add command:
    if args[0] == "add":

        filename = args[1].split(".")[0]
        if os.path.exists(filename):
            return "file: " + filename + " already exists"
        
        f = open(filename, "a")
        filecontent = ""
        i = 2
        while i < len(args):
            filecontent += args[i]
            if i < len(args) - 1:
                filecontent += ","
            i+=1
        f.write(filecontent)
        f.close()

        # send message back to the client (flask handles errors if file creation is not successful)
        return "data successfully stored"


    # read command:
    if args[0] == "read":
        
        filename = args[1].split(".")[0]
        user_password = args[2].split(":")[1]
        file_password = ""
        
        if os.path.exists(filename):
            f = open(filename, "r")
            content = f.read()
            raw_add = content.split(",")
            for field in raw_add:
                if "password:" in field:
                    file_password = field.split(":")[1]
            if user_password == file_password:
                return content
            else:
                return "password is invalid: " + user_password

        else:
            return "file does not exist: " + filename


if __name__ == "__main__":
    app.run()
