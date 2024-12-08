def is_exist(key, value, db):
    return any(i[key] == value for i in db)

def validate_book_data(data, db_data):
    required_fields = ['id', 'title', 'category', 'price', 'author']

    for field in required_fields:
        if field not in data or not data[field]:
            return f"{field} is required", 400

    if not isinstance(data['id'], int):
        return "invalid id value", 400

    if is_exist("id", data["id"], db_data):
        return "id already exists", 400

    if is_exist("title", data["title"], db_data):
        return "title already exists", 400

    if not isinstance(data["title"], str):
        return "invalid title value", 400

    if not isinstance(data["category"], str):
        return "invalid value for category", 400

    if not isinstance(data["price"], str):
        return "invalid value for price", 400

    if not isinstance(data["author"], str):
        return "invalid value for author", 400

    return data, 200

def is_valid(response):
    return {"response": response[0], "valid": response[1] == 200}
