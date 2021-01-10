import hashlib
import os
import pathlib


def is_directory_empty(path: str) -> bool:
    path_obj = pathlib.Path(path)
    directory_path = path_obj.parent
    files_count = len(os.listdir(directory_path))
    return not bool(files_count)


def remove_directory(path: str) -> None:
    path_obj = pathlib.Path(path)
    os.rmdir(path_obj.parent)


def custom_path_handler(instance, filename: str) -> str:
    """
    Handle path and name to save file in storage
    """
    dir_ = instance.hash[:2]
    name = instance.hash
    if '.' in filename:
        file_extension = f'.{filename.split(".")[-1]}'
        return f'{dir_}/{name}{file_extension}'
    else:
        return f'{dir_}/{name}'


def generate_hash(bytes_, hash_algorithm=hashlib.sha256) -> str:
    """
    Return string with hash containing only hexadecimal digits
    """
    return hash_algorithm(bytes_).hexdigest()
