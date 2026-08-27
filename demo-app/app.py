import subprocess

def run(cmd):
    subprocess.run([cmd], shell=False)
