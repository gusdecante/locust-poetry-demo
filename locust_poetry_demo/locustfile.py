from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/hello")

    def on_start(self):
        self.client.post('/create-account', json=dict(username="foo", password="bar"))
