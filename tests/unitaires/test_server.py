import flask
import pytest
import server
from server import showSummary, clubs, app
from flask import Flask, template_rendered, url_for, request, current_app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

class TestLoginEmail:

    def setup(self):
        self.listOfClubs = [{'name': 'club_1', 'email': 'email_club_1', 'points': "30"},
                    {'name': 'club_2', 'email': 'email_club_2', 'points': "5"}]
        self.listOfCompetitions = [{"name": "competition_1","date": "2020-03-27 10:00:00","numberOfPlaces": "25"},
                            {"name": "Fall Classic","date": "2020-10-22 13:30:00","numberOfPlaces": "13"}]
        self.login_email = "email_club_1"
        self.unknown_email = "email_club_3"

    def test_login_mail_exist(self, client, mocker):        
        mocker.patch.object(server, 'clubs', self.listOfClubs)

        response = client.post('/showSummary',
                              data=dict(email=self.login_email),
                              follow_redirects=True
                              )
        data = response.data.decode()
        assert response.status_code == 200
        assert "Welcome" in data

    def test_login_email_unknown(self, client, mocker):
        mocker.patch.object(server, 'clubs', self.listOfClubs)
        response = client.post('/showSummary',
                              data=dict(email=self.unknown_email),
                              follow_redirects=True
                              )
        data = response.data.decode()
        assert response.status_code == 200
        assert "Unknown email" in data


class TestUseClubPoints:

    def setup(self):
        self.listOfClubs = [{'name': 'club_1', 'email': 'email_club_1', 'points': "30"},
                    {'name': 'club_2', 'email': 'email_club_2', 'points': "5"}]
        self.listOfCompetitions = [{"name": "competition_1","date": "2020-03-27 10:00:00","numberOfPlaces": "25"},
                            {"name": "Fall Classic","date": "2020-10-22 13:30:00","numberOfPlaces": "13"}]
        self.less_than_club_points = "3"
        self.more_than_club_points = "8"

    def test_book_less_places_than_their_points(self, client, mocker):        
        mocker.patch.object(server, 'clubs', self.listOfClubs)
        mocker.patch.object(server, 'competitions', self.listOfCompetitions)

        response = client.post('/purchasePlaces',
                              data=dict(places=self.less_than_club_points,
                                        club=self.listOfClubs[1]['name'],
                                        competition=self.listOfCompetitions[1]['name']),
                              follow_redirects=True
                              )
        data = response.data.decode()
        assert response.status_code == 200
        assert "Welcome" in data

    def test_book_more_places_than_their_points(self, client, mocker):
        mocker.patch.object(server, 'clubs', self.listOfClubs)
        mocker.patch.object(server, 'competitions', self.listOfCompetitions)

        response = client.post('/purchasePlaces',
                              data=dict(places=self.more_than_club_points,
                                        club=self.listOfClubs[1]['name'],
                                        competition=self.listOfCompetitions[1]['name']),
                              follow_redirects=True
                              )
        data = response.data.decode()
        assert response.status_code == 200
        print (data)
        expected_error_message = "You cannot book more places than your club current number of points !"
        assert expected_error_message in data

class TestMaxBookingPlaces:
    def setup(self):
        self.listOfClubs = [{'name': 'club_1', 'email': 'email_club_1', 'points': "30"},
                    {'name': 'club_2', 'email': 'email_club_2', 'points': "5"}]
        self.listOfCompetitions = [{"name": "competition_1","date": "2020-03-27 10:00:00","numberOfPlaces": "25"},
                            {"name": "Fall Classic","date": "2020-10-22 13:30:00","numberOfPlaces": "13"}]
        self.less_than_max_places = "3"
        self.more_than_max_places = "15"


    def test_book_less_places_than_max_authorized(self, client, mocker):        
        mocker.patch.object(server, 'clubs', self.listOfClubs)
        mocker.patch.object(server, 'competitions', self.listOfCompetitions)

        response = client.post('/purchasePlaces',
                              data=dict(places=self.less_than_max_places,
                                        club=self.listOfClubs[0]['name'],
                                        competition=self.listOfCompetitions[0]['name']),
                              follow_redirects=True
                              )
        data = response.data.decode()
        assert response.status_code == 200
        expected_error_message = "You cannot book more than 12 places for each competition"
        assert expected_error_message not in data

    def test_book_more_places_than_max_authorized(self, client, mocker):        
        mocker.patch.object(server, 'clubs', self.listOfClubs)
        mocker.patch.object(server, 'competitions', self.listOfCompetitions)

        response = client.post('/purchasePlaces',
                              data=dict(places=self.more_than_max_places,
                                        club=self.listOfClubs[0]['name'],
                                        competition=self.listOfCompetitions[0]['name']),
                              follow_redirects=True
                              )
        data = response.data.decode()
        assert response.status_code == 200
        expected_error_message = "You cannot book more than 12 places for each competition"
        assert expected_error_message in data
