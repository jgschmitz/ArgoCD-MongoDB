import subprocess

namespace = "default"

# Check if the namespace exists
def namespace_exists(ns):
    cmd = f"kubectl get namespace {ns}"
    result = subprocess.run(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

# Create the namespace if it doesn't exist
if not namespace_exists(namespace):
    print(f"Namespace '{namespace}' not found. Creating...")
    subprocess.run(f"kubectl create namespace {namespace}".split())
else:
    print(f"Namespace '{namespace}' already exists.")
