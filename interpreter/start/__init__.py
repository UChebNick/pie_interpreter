import docker
import os




tag = "docker-interpreter"
client = docker.from_env()
image, build_logs = client.images.build(path='interpreter\\copy_dir',
                                        dockerfile=f'{os.path.abspath(os.path.curdir)}\interpreter\Dockerfile',
                                        tag=tag)

