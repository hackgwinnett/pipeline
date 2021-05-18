from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "api error: no args passed"

@app.route("/<raw>")
def parse(raw):
    args = str(raw).split("_")

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

if __name__ == "__main__":
    app.run()
