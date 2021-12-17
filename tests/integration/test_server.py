import flask
import pytest
import server
from server import showSummary, clubs, app, book, getClubsList, purchasePlaces
from flask import Flask, template_rendered, url_for, request, current_app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SERVER_NAME'] = 'TEST.sample'
    client = app.test_client()
    with app.app_context():
        pass
    app.app_context().push()
    yield client


class TestLogoutRoute:
    def setup(self):
        self.login_email = "admin@irontemple.com"
        self.unknown_email = "email_club_3"

    def test_logout_route(self,client):
        login = client.post('/showSummary',
                               data=dict(email=self.login_email),
                               follow_redirects=True)
        assert login.status_code == 200
        data = login.data.decode()
        print(data)
        assert "Logout" in data
        response = client.get('/logout', follow_redirects=True)
        assert login.status_code == 200
        data = response.data.decode()
        print(data)
        assert 'Welcome' in data

    def test_logout_wrong(self, client):
        login = client.post('/showSummary',
                               data=dict(email=self.unknown_email),
                               follow_redirects=True)
        data = login.data.decode()
        print(data)
        assert login.status_code == 200
        assert "Unknown email" in data
        assert "Logout" not in data