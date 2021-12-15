import json
import time
from datetime import datetime
from flask import Flask,render_template,request,redirect,flash,url_for


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def showSummary():
    if len([club for club in clubs if club['email'] == request.form['email']]) != 0:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html',club=club,competitions=competitions)
    else:
        error = "Unknown email"
        flash("Unknown email")
        time.sleep(2)
        return render_template('index.html', error=error)


@app.route('/book/<competition>/<club>')
def book(competition,club):
    try:
        foundClub = [c for c in clubs if c['name'] == club][0]
        foundCompetition = [c for c in competitions if c['name'] == competition][0]
        today = datetime.now()
        competition_date = foundCompetition['date']
        competition_date = datetime.strptime(competition_date, "%Y-%m-%d %H:%M:%S")
        competition_period = None
        if competition_date > today:
            competition_period = 'futur'
            with app.app_context():
                return render_template('booking.html',club=foundClub,competition=foundCompetition,period=competition_period)
        else:
            competition_period = 'past'
            with app.app_context():
                return render_template('booking.html',club=foundClub,competition=foundCompetition,period=competition_period)
    except IndexError:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)

@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    places_required = int(request.form['places'])
    club_points = int(club["points"])
    competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-places_required
    club['points'] = club_points - places_required
    if places_required < 12:
        if places_required > club_points:
                error = "You cannot book more places than your club current number of points"
                return render_template('booking.html', club=club, competition=competition, error=error)
        else:
            flash('Great-booking complete!')
            return render_template('welcome.html', club=club, competitions=competitions)
    else:
        error = "You cannot book more than 12 places for each competition"
        return render_template('booking.html', club=club, competition=competition, error=error)

@app.route('/clubsList', methods=['GET'])
def getClubsList():
    return render_template('clubs_list.html', clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))