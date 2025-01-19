import subprocess
import time

app_name = "darkstar"

def check_status():
    cmd = f"argocd app get {app_name}"
    result = subprocess.run(cmd.split(), stdout=subprocess.PIPE)
    output = result.stdout.decode("utf-8")
    if "Sync Status: OutOfSync" in output:
        print(f"{app_name} is out of sync. Please investigate!")
    elif "Sync Status: Synced" in output:
        print(f"{app_name} is synced and healthy.")
    else:
        print(f"Unknown state for {app_name}: \n{output}")

while True:
    check_status()
    time.sleep(60)  # Check every 60 seconds
