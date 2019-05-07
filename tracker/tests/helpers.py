import os


TEST_RESOURCES_PATH = ['resources']


def get_absolute_file_path(filename, *path):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), *path, filename)
