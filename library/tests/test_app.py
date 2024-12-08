import pytest
from api import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_books(client):
    response = client.get('/api/books/')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_get_book_by_id(client):
    response = client.get('/api/books/1/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == 1

def test_add_book(client):
    response = client.post('/api/book/add/', json={
        'id': 2,
        'title': 'New Book',
        'category': 'Fiction',
        'price': '$15',
        'author': 'Author Name'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['title'] == 'New Book'

    # Check the book was added
    response = client.get('/api/books/2/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == 2
 