from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "api error: no args passed"

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
        f = open(filename, "a")
        filecontent = ""
        i = 2
        while i < len(args):
            filecontent += args[i] + " "
            i+=1
        f.write(filecontent)
        f.close()

    # send message back to the client (flask throws errors if file creation is not successful)
    return "data successfully stored"

if __name__ == "__main__":
    app.run()
