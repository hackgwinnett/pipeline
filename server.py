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
        
        format (if add directory):
        args[0] = add_dir
        args[1] = directory name
        args[2] = password (if no password is None)
        ...creates empty directory unless there is a password

        format (if read):
        args[0] = read
        args[1] = filename
        args[2] = password
        ...returns data in the file
        
        format (if read directory):
        args[0] = read_dir
        args[1] = directory name
        args[2] = password (Also None if there is no password)
        ...returns a list of the files in a directory
    '''

    # debugging (server-side):
    output = ""
    for element in args:
        output += element + " "

    print(output)

    # add command:
    if args[0] == "add":
        filename = args[1].split(".")[0]
        filename = filename.replace(">", "/")
        if os.path.exists(filename):
            return "file: " + filename + " already exists"

        f = open(filename, "a")
        filecontent = ""
        i = 2
        while i < len(args):
            filecontent += args[i]
            if i < len(args) - 1:
                filecontent += ","
            i += 1
        f.write(filecontent)
        f.close()

        # send message back to the client (flask handles errors if file creation is not successful)
        return "data successfully stored"

    # add directory command:
    elif args[0] == "add_dir":
        dirname, password = args[1], args[2]
        dirname = dirname.replace(">", "/")
        if os.path.exists(dirname):
            return f"Directory: {dirname} already exists!"

        os.makedirs(dirname)

        if "None" not in str(password):
            with open(f"{dirname}/password.txt", "w") as file:
                file.write(f"password:{password}")
            return f"Locked Directory {dirname} Created with Password {password}"
        else:
            return f"Directory {dirname} created!"

    # read command:
    elif args[0] == "read":

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

    # read directory command:
    elif args[0] == "read_dir":
        password, filename = args[2], args[1]
        user_password = password.split(":")[1]
        filename = filename.replace(">", "/")
        print(filename)
        print(password)
        if os.path.exists(filename):
            try:
                with open("password.txt", "r") as password:
                    if user_password in password.read():
                        files = os.listdir(filename)
                        return str(files)
                    else:
                        return "Incorrect password"
            except FileNotFoundError:
                files = os.listdir(filename)
                return str(files)
        else:
            return f"Directory {filename} does not exist"
    else:
        return 'Unknown Command: "' + args[0] + '"'


if __name__ == "__main__":
    app.run()
