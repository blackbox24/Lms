from flask import Flask, jsonify, request
import json
from validations import validate_book_data, is_valid,is_exist

# create app 
app = Flask(__name__)

# Fake book data
books = [{"id": 1, "title": "John", "category": "action", "price": "$100", "author": "John Doe"}]

# Routes
@app.route("/api/books/", methods=["GET"])
def get_books():
    return jsonify(books)

@app.route("/api/books/<int:id>/", methods=["GET"])
def get_book_by_id(id: int):
    book = next((b for b in books if b["id"] == id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Book does not exist"}), 404

@app.route("/api/book/add/", methods=["POST"])
def add_book():
    try:
        data = json.loads(request.data)
    except json.JSONDecodeError as e:
        return jsonify({"error": "Invalid JSON data", "message": str(e)}), 400

    validated_data, status_code = validate_book_data(data, books)
    if status_code != 200:
        return jsonify({"error": validated_data}), status_code

    books.append(data)
    return jsonify(data), 200

# delete book
@app.route("/api/book/remove/<int:id>/", methods=["DELETE"])
def delete_book(id: int):
        global books
        if not is_exist("id",id,books):
            return jsonify("book not found"),400
        
        books = [x for x in books if x["id"] != id]
        return jsonify(books),200

# update book
@app.route("/api/book/update/<int:id>/", methods=["PUT"])
def update_book(id: int):
    try:
        data = json.loads(request.data) 
    except json.JSONDecodeError as e:
        return jsonify({"error": "Invalid JSON data", "message": str(e)}), 400
            
    for i in books:
        if i["id"] == id:
            _index = books.index(i)
            books[_index] = data

            return jsonify(books), 200
    return "book not found"
        


if __name__ == "__main__":
    app.run(debug=True)