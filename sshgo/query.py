import os
import sys
from sshgo.variables import *
from ruamel.yaml import YAML

def query_data(profile):
    yaml = YAML()

    with open(FILE_PATH, "r") as f:
        data = yaml.load(f)

    return data['profiles'][profile]

def add_profile():
    yaml = YAML()
    yaml.preserve_quotes = True

    with open(FILE_PATH, "r") as file:
        data = yaml.load(file)

    while True:
        alias = input(f"{'Server Alias':<20}|  ")
        if alias in data['profiles']:
            print("Name already exists")
            continue
        host = input(f"{'host':<20}|  ")

        port = input(f"{'port':<20}|  ")
        username = input(f"{'username':<20}|  ")
        identity = input(f"{'identity:':<20}|  ")
        
        break

    if 'profiles' not in data or not isinstance(data['profiles'], dict):
        data['profiles'] = {}

    data['profiles'][alias] = {
        'host': host,
        'port': port,
        'username': username,
        'identity': identity
    }

    with open(FILE_PATH, 'w') as file:
        yaml.dump(data, file)

    print(f"Profile '{alias}' added successfully")

def del_profile():
    yaml = YAML()
    yaml.preserve_quotes = True

    with open(FILE_PATH, "r") as file:
        data = yaml.load(file)

    while True:
        alias = input(f"{'Server Alias':<20}|  ")
        if alias not in data['profiles']:
            print("Name does not exists")
            continue
        break

    del data['profiles'][alias]

    with open(FILE_PATH, 'w') as file:
        yaml.dump(data, file)

    print(f"Profile '{alias}' removed successfully")

def view_profile():
    yaml = YAML()
    yaml.preserve_quotes = True

    with open(FILE_PATH, "r") as file:
        data = yaml.load(file)

    profiles = data.get('profiles', {})

    if not profiles:
        print("No profiles found.")
        return

    print(f"\n{'Alias':<20} | {'Host':<15} | {'Port':<5} | {'Username':<10} | {'Identity'}")
    print("-" * 70)

    for alias, details in profiles.items():
        print(f"{alias:<20} | {details.get('host', ''):<15} | {details.get('port', ''):<5} | {details.get('username', ''):<10} | {details.get('identity', '')}")
