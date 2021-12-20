from locust import HttpUser, task, TaskSet

class ProjectPerfTest(HttpUser):
    def on_start(self):
        self.login_email = "admin@irontemple.com"
    
    @task
    def index(self):
        self.client.get("/")

    @task
    def showSummary(self):
        self.client.post("/showSummary", {"email":self.login_email})

    """@task
    def showsummarytest(self):
        self.client.post("http://127.0.0.1:5000/showSummary", data=dict(email="kate@shelifts.co.uk"))"""

    @task
    def purchasePlaces(self):
        self.client.post('/purchasePlaces', {"places_required":"1",
                                             "club":"Simply Lift",
                                             "competition":"Fall Classic"})
