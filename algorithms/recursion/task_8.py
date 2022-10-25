import os


def get_files(path):
    files = []
    dir = os.scandir(path)
    for item in dir:
        if item.is_file():
            files.append(item.name)
        elif item.is_dir():
            new_path = f'{path}/{item.name}'
            files += get_files(new_path)
    return files
