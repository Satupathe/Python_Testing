from locust import HttpUser, task


class ProjectPerfTest(HttpUser):
    def on_start(self):
        self.login_email = "admin@irontemple.com"

    @task
    def index(self):
        self.client.get("/")

    @task
    def logout(self):
        self.client.get('/logout')

    @task
    def showSummary(self):
        self.client.post("/showSummary", {"email": self.login_email})

    @task
    def purchasePlaces(self):
        self.client.post('/purchasePlaces',
                         data=dict(places='1',
                                   club="Simply Lift",
                                   competition="Fall Classic"))
