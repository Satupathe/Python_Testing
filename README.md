# gudlift-registration

1. Why

    This is a proof of concept (POC) project to show a light-weight version of our competition booking platform. The aim is the keep things as light as possible, and use feedback from the users to iterate.

2. Getting Started

    This project uses the following technologies:

    * Python v3.x+

    * [Flask](https://flask.palletsprojects.com/en/1.1.x/)

        Whereas Django does a lot of things for us out of the box, Flask allows us to add only what we need. 

    * [Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)

        This ensures you'll be able to install the correct packages without interfering with Python on your machine.

        Before you begin, please ensure you have this installed globally. 

    * [Selenium](https://selenium-python.readthedocs.io/)

        Allow to automate test of functional/user path by emulating real user action 

        You can directly test it with selenium for functionnal test will be included in Pytest tests (next part)  
    
    * [Pytest](https://docs.pytest.org/en/6.2.x/) 

        Package for unit and integration testing using features like mocker and fixture.

    * [Locust](https://locust.io/)

        Define tasks to be tested continuously and assess response time hence define project performance

    * [Coverage](https://coverage.readthedocs.io/en/6.2/)

        Assess code percentage cover by tests. Define 

3. Installation

    - After cloning, change into the directory and type <code>virtualenv .</code>. This will then set up a a virtual python environment within that directory.

    - Next, type <code>source bin/activate</code>. You should see that your command prompt has changed to the name of the folder. This means that you can install packages in here without affecting affecting files outside. To deactivate, type <code>deactivate</code>

    - Rather than hunting around for the packages you need, you can install in one step. Type <code>pip install -r requirements.txt</code>. This will install all the packages listed in the respective file. If you install a package, make sure others know by updating the requirements.txt file. An easy way to do this is <code>pip freeze > requirements.txt</code>

    - Switch to the QA branch with <code>git branch QA<code>

    - Flask requires that you set an environmental variable to the python file. However you do that, you'll want to set the file to be <code>server.py</code>. Check [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) for more details

    - You should now be ready to test the application. In the directory, type either <code>flask run</code> or <code>python -m flask run</code>. The app should respond with an address you should be able to go to using your browser.

4. Current Setup

    The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around having a DB until we actually need one. The main ones are:
     
    * competitions.json - list of competitions
    * clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will accept for login.

5. Testing

    * [Pytest](https://docs.pytest.org/en/6.2.x/) 

        - Set your terminal to your project parent directory and type <code>flask run<code> then enter to start your Flask server. This will be needed in the following steps.
            * If you ever encounter an error <code>Error: Could not locate a Flask application.<code> type <code>$env:FLASK_APP="server.py"<code> then enter and try again to launch your server

        - Open another terminal(don't close the first one) and set it again to your project parent directory

        - In the new terminal type <code>pytest<code> then enter

        - All test will be launch consecutively and you'll find a success report at the end. Approximative testing time: 1 minute.

    * [Coverage](https://coverage.readthedocs.io/en/6.2/)

        - Keep your flask server running on your first terminal or launch it if you close it before(following Pytest steps)

        - Set your second terminal to your project parent directory

        - Activate coverage with <code>pytest --cov=.<code> in your second terminal. This will launch your testing again and display coverage percentage

        - Activate coverage with an html report through <code>pytest --cov=. --cov-report html<code> 
        
        - In a web browser follow this adress: http://127.0.0.1:5500/coverage_html/index.html

        - You will find coverage detail by clicking on a file name

    * [locust](https://locust.io/)

        - Keep your flask server running on your first terminal or launch it if you close it before(following Pytest steps)
        
        - Set your second terminal to the following folder tests/performance_tests

        - Activate Locust with <code>locust<code> in your second terminal.

        - Open a web browser with one of the following adress: http://0.0.0.0:8089 or localhost:8089

        - In the window set:
            * Number of users to 6
            * Spawn rate to 1
            * Host to http://127.0.0.1:5000
            * Click on Start swarming
