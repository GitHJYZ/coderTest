from flask import Flask,request
app = Flask(__name__)

@app.route("/",methods = ["get"])
def index():
    id = request.args.get("id")
    #return str(id)
    # return "<h2>Hello World</h2>"
    return request.json
if __name__ == "__main__":
    app.run(debug = True,port = 8000)