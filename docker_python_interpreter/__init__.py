import docker
import os
from container_supervisor import json_handler
from docker_python_interpreter.container_supervisor import container_utils


class docker_interpreter:
    async def __aenter__(self):
        client = docker.from_env()
        image, build_logs = client.images.build(path='.',
                                                dockerfile=f'{os.path.abspath(os.path.curdir)}\Dockerfile',
                                                tag="docker-interpreter")
        self.image = image
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

    async def run_code(self, code, mem='500M', nano_cpus=10000000):

        await container_deployer.deploy_container()


