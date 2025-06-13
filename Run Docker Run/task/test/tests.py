import docker
from hstest import StageTest, dynamic_test, CheckResult

ancestor = "hyper-web-app"
project_images = ["hyper-web-app"]

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
        """Tests if the container is deleted"""
        if self.client is None:
            return CheckResult.wrong("Docker client is not initialized. Is Docker installed and running?")
        try:
            all_containers = self.client.containers.list(all=True)
        except docker.errors.DockerException as e:
            return CheckResult.wrong(f"Cannot connect to the Docker daemon: {e}")

        for container in all_containers:
            if container.attrs.get("Config").get("Image") == ancestor:
                return CheckResult.wrong(f"You should delete the container for the ancestor '{ancestor}'!")

        return CheckResult.correct()

    @dynamic_test()
    def test2(self):
        """Tests if the image is removed from the system"""
        if self.client is None:
            return CheckResult.wrong("Docker client is not initialized. Is Docker installed and running?")
        try:
            images_text = " ".join([str(image) for image in self.client.images.list()])
        except docker.errors.DockerException as e:
            return CheckResult.wrong(f"Cannot connect to the Docker daemon: {e}")

        for image in project_images:
            if image in images_text:
                return CheckResult.wrong(f"You should delete the image '{image}'!")

        return CheckResult.correct()

if __name__ == '__main__':
    DockerTest().run_tests()