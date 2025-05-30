import os
from sshgo.variables import FILE_PATH

def initialconfig():

    if not os.path.exists(FILE_PATH):
        os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
        with open(FILE_PATH, 'w') as f:
            f.write("profiles: {}\n")