import docker
import os


async def deploy_container(file, client, tag='docker-interpreter', mem='500M', nano_cpus=10000000):
    container = client.containers.run(
        tag,
        detach=True,
        command=f"python -u -c {file}",
        nano_cpus=nano_cpus,
        mem_limit=mem,
        network_mode="none"
    )
    return container

async def del_container(container):
    container.stop()
    container.remove()

# client = docker.from_env()
# image, build_logs = client.images.build(path='..',
#                                         dockerfile=f'{os.path.abspath(os.path.curdir)}\Dockerfile',
#                                         tag="docker-interpreter")

async def get_json()