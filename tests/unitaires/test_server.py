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
        self.listOfClubs = [{'name': 'club_1', 'email': 'email_club_1', 'points': 30},
                    {'name': 'club_2', 'email': 'email_club_2', 'points': 5}]
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



#non working part


"""def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<h1>Welcome to the GUDLFT Registration Portal!</h1>' in response.data"""


"""class UserModelTestCase(unittest.TestCase):
    def setUp(self):

        self.client = self.app.test_client(use_cookies=True)
        self.listOfClubs = [{'name': 'club_1', 'email': 'email_club_1', 'points': 30},
                   {'name': 'club_2', 'email': 'email_club_2', 'points': 5}]
        self.listOfCompetitions = [{"name": "competition_1","date": "2020-03-27 10:00:00","numberOfPlaces": "25"},
                              {"name": "Fall Classic","date": "2020-10-22 13:30:00","numberOfPlaces": "13"}]
        self.login_email = "email_club_1"
        self.unknown_email = "email_club_3"
        self.places_required = 4
        self.too_much_places_required = 13
        self.not_enough_points = 6
     
    def tearDown(self):
        self.app_ctx.pop()

    def test_1(self, client):
        r = self.client.get('/purchasePlaces')
        self.assertEqual(r.status_code, 200)
        self.assertTrue('How many places?' in r.get_data(as_text=True))
        r = self.client.post('/purchasePlaces',
                             data=dict(places=self.places_required,
                                       competition=self.listOfCompetitions[0],
                                       club=self.listOfClubs[1]),
                             follow_redirects=True
                             )
        self.assertEqual(r.status_code, 200)
        self.assertTrue('<h2>Welcome,' in r.get_data(as_text=True))
        self.assertEqual(r.status_code, 200)"""



"""@pytest.fixture
def client():
    client = app.test_client()
    yield client


class testEssai:

    @patch('url_for')
    def test(self, client):
        client.post('/showSummary',
                    data={},
                    follow_redirects=True)

        self.assert_called_once_with('bp.submit', success=1, id=1)"""



"""@pytest.fixture
def app(mocker):
    mocker.patch("flask_sqlalchemy.SQLAlchemy.init_app", return_value=True)
    mocker.patch("flask_sqlalchemy.SQLAlchemy.create_all", return_value=True)
    mocker.patch("example.database.get_all", return_value={})
    return app.app"""


"""def test_example(client):
    response = client.get("/")
    assert response.status_code == 200"""


"""@pytest.fixture
def appli():
    app = Flask(__name__)
    app.logger.setLevel(logging.CRITICAL)
    ctx = app.test_request_context()
    ctx.push()

    app.config["TESTING"] = True
    app.testing = True

    yield app
    ctx.pop()"""



"""@pytest.fixture
def captured_templates(appli):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, appli)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, appli)"""

"""class TestLoginEmail:

    listOfClubs = [{'name': 'club_1', 'email': 'email_club_1', 'points': 30},
                   {'name': 'club_2', 'email': 'email_club_2', 'points': 5}]
    listOfCompetitions = [{"name": "competition_1","date": "2020-03-27 10:00:00","numberOfPlaces": "25"},
                          {"name": "Fall Classic","date": "2020-10-22 13:30:00","numberOfPlaces": "13"}]
    login_email = "email_club_1"
    unknown_email = "email_club_3"

    def test_login_mail_exist(self, client):
        rajouter captured_template
        response = client.get('/showSummary')

        # Sanity checks - it would be a total surprise if this would not hold true
        assert response.status_code == 200
        
        assert len(captured_templates) == 1
        template, context = captured_templates[0]
        assert template.name == "welcome.html"
        assert "error" not in context
        request = client.post('/showSummary',
                              data=dict(email=self.login_email,
                                        clubs=self.listOfClubs,
                                        competitions=self.listOfCompetitions),
                              follow_redirects=True
                              )
        data = request.data.decode()
        assert request.status_code == 200
        assert data.find("error") == -1


    def test_login_email_unknown(self, client):
        response = client.get('/showSummary')
        #assert len(captured_templates) == 1
        template, context = captured_templates[0]
        assert template.name == "/index.html"
        assert "error" in context
        assert context["error"] == "Unknown email"
        request = client.post('/showSummary',
                              data=dict(email=self.unknown_email,
                                        clubs=self.listOfClubs,
                                        competitions=self.listOfCompetitions),
                              follow_redirects=True
                              )
        data = request.data.decode()
        assert request.status_code == 200
        print(data)
        assert data.find("error") == "Unknown email"""

"""if __name__ == '__main__':
    unittest.main()"""