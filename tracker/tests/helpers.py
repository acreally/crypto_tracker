import os


TEST_RESOURCES_PATH = ['tests', 'resources']

def get_absolute_file_path(filename, *path):
  return os.path.join(os.getcwd(), *path, filename)