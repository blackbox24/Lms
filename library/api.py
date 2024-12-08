from flask import Flask, jsonify

# create app 
app = Flask(__name__)

#  create data
data = [
    {'id': 546, 'username': 'John'},
    {'id': 894, 'username': 'Mary'},
    {'id': 326, 'username': 'Jane'}
]
# create routers for library

# retrieve list of all libraries
@app.route("/library",methods=["GET"])
def get_library():
    return jsonify(data)

#  retrieve library by id
@app.route("/library/<int:id>/",methods=["GET"])
def get_library_id(id: int):
    for i in data:
        if i["id"] == id:
            return jsonify(i)
    return jsonify({ 'error': 'Library does not exist'}), 404
    

# add library
@app.route("/library",methods=["POST"])
def add_library():
    return "added"

#  delete library
@app.route("/library",methods=["DELETE"])
def delete_library():
    return "deleted"

# update library
@app.route("/library",methods=["PATC"])
def update_library():
    return "updated"

app.run()