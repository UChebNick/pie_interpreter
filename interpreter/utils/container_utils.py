import docker
import os
import json
import tarfile
import io

async def deploy_container(code, client, name, tag='docker-interpreter', mem='500M', nano_cpus=10000000):
    container = client.containers.run(
        tag,
        name=name,
        detach=True,
        command=f'python -c "{code}"',
        nano_cpus=nano_cpus,
        mem_limit=mem,
        network_mode="none"

    )
    return container


async def get_json(container, path):

    _, output = container.get_archive(path)
    p = list(_)


    content = b''.join(p).decode('utf-8')
    print(output)
    return json.loads(''.join(content.split(chr(0)))[-output['size']:])


async def save_json(container, host_path, container_path):
    stream = io.BytesIO()
    with tarfile.open(fileobj=stream, mode='w|') as tar, open(host_path, 'rb') as f:
        info = tar.gettarinfo(fileobj=f)
        info.name = os.path.basename(host_path)
        tar.addfile(info, f)

    container.put_archive(container_path, stream.getvalue())