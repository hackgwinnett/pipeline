from flask import Flask, request
import os

app = Flask(__name__)


@app.route("/", methods=("POST",))
def parse():
    headers = request.headers
    command, filename, password = headers.get("command"), headers.get("filename"), headers.get("password")
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

    # add command:
    if command == "add":
        data = request.get_json()
        data = data.split("{")[1]
        if os.path.exists(filename):
            return "file: " + filename + " already exists"

        if password != "None":
            with open(filename, "w") as f:
                f.write(f'{{"password": "{password}", {data}')
        else:
            with open(filename, "w") as f:
                f.write(data)

        # send message back to the client (flask handles errors if file creation is not successful)
        return "data successfully stored"

    # add directory command:
    elif command == "add_dir":
        filename = filename.replace(">", "/")
        if os.path.exists(filename):
            return f"Directory: {filename} already exists!"

        os.makedirs(filename)

        if "None" not in str(password):
            with open(f"{filename}/password.txt", "w") as file:
                file.write(f"password:{password}")
            return f"Locked Directory {filename} Created with Password {password}"
        else:
            return f"Directory {filename} created!"

    # read command:
    elif command == "read":

        file_password = ""

        if os.path.exists(filename):
            with open(filename, "r") as f:
                content = f.read()
            raw_add = content.split(",")
            for field in raw_add:
                if '"password":' in field:
                    file_password = field.split(":")[1]
                    file_password = file_password.split('"')[1]
            if password != "None":
                if password == file_password:
                    return content
                else:
                    return "password is invalid: " + password
            else:
                return content

        else:
            return "file does not exist: " + filename

    # read directory command:
    elif command == "read_dir":
        if os.path.exists(filename):
            try:
                with open("password.txt", "r") as password:
                    if str(password) in password.read():
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
        return 'Unknown Command: "' + command + '"'


if __name__ == "__main__":
    app.run()
