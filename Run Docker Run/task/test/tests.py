import docker
from hstest import StageTest, dynamic_test, CheckResult, WrongAnswer

project_images = ["python:3.11-slim"]

class DockerTest(StageTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.output = None
        try:
            self.client = docker.from_env()
        except docker.errors.DockerException as e:
            self.client = None
            print(f"Error initializing Docker client: {e}")           

    @dynamic_test()
    def test1(self):
        if self.client is None:
            return CheckResult.wrong("Docker client is not initialized. Is Docker installed and running?")
        try:
            self.client.info()
        except docker.errors.DockerException as e:
            return CheckResult.wrong(f"Cannot connect to the Docker daemon: {e}")

        images_text = " ".join([str(image) for image in self.client.images.list()])
        for image in project_images:
            if image not in images_text:
                return CheckResult.wrong(f"'{image}' not found in the system images!")

        return CheckResult.correct()

if __name__ == '__main__':
    DockerTest().run_tests()