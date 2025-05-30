import os

from sshgo.variables import *
from ruamel.yaml import YAML

def query_data(profile):
    yaml = YAML()

    with open(FILE_PATH, "r") as f:
        data = yaml.load(f)

    return data['profiles'][profile]