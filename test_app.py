import app


def test_hello():
    client = app.app.test_client()
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, World!"}


def test_echo():
    client = app.app.test_client()
    payload = {"msg": "ping"}
    response = client.post('/echo', json=payload)
    assert response.status_code == 201
    assert response.get_json() == payload


def test_put_item():
    client = app.app.test_client()
    payload = {"name": "test_item", "value": 123}
    response = client.put('/item/1', json=payload)
    assert response.status_code == 200
    assert response.get_json() == {"1": payload}


def test_delete_item():
    client = app.app.test_client()
    # Add an item first
    client.put('/item/2', json={"name": "to_delete"})
    response = client.delete('/item/2')
    assert response.status_code == 204
    # Ensure deleting a non-existent item returns 404
    response = client.delete('/item/999')
    assert response.status_code == 404
    assert response.get_json() == {"error": "Not found"}
