from sshgo.connect import connect as ssh_connect
from sshgo.config import initialconfig
import yaml
import argparse
from sshgo.query import *

def main():
    initialconfig()
    parser = argparse.ArgumentParser(prog="ssh-go", description="Greet the user.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    connect_parser = subparsers.add_parser("connect", help="connect to server")
    connect_parser.add_argument("profile", help="The profile name to connect to")
    args = parser.parse_args()

    if args.command == "connect":
        print(args.profile)
        data = query_data(args.profile)
        ssh_connect(data["username"], data["host"], data["identity"], data["port"])     
    elif args.test:
        print(args.test)
    else:
        print("hello")

if __name__ == "__main__":
    main()