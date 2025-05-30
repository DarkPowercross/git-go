import subprocess

def connect(username, host, identity, port=22):
    cmd = ["ssh", "-i", identity, "-p", str(port), f"{username}@{host}"]
    subprocess.run(cmd)

if __name__ == "__main__":
    pass