from app import app

def test_home_route():
    response = app.test_client().get('/')
    assert response.status_code == 200
    # assert response.data.decode('utf-8') == "Welcome to my Flask App."

def test_other_page_route():
    response = app.test_client().get('/<page_name>')
    assert response.status_code == 204
    # assert response.data.decode('utf-8') == "This page named <page_name> does not exist."