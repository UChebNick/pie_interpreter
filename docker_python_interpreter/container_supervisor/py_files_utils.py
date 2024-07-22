import os


async def create_and_write_file(container_name, code):
    file_name = f"main-{container_name}.py"

    async with open('docker_copy_files'+ '\\' + file_name, "w") as file:
        await file.write(code)


async def delete_file(container_name):
    file_name = f"main-{container_name}.py"
    os.remove(file_name)

