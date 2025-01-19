import subprocess

namespace = "default"

def check_health(namespace):
    cmd = f"kubectl get all -n {namespace}"
    result = subprocess.run(cmd.split(), stdout=subprocess.PIPE)
    print(result.stdout.decode("utf-8"))

check_health(namespace)
