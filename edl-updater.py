import subprocess
import time
import random

LOOKUPS = 100
DELAY_BETWEEN = 1  # seconds
HOSTNAME = "a32dl55qcodech-ats.iot.eu-west-1.amazonaws.com"
EDL_FILE = "edl.txt"

def get_current_ips():
    try:
        with open(EDL_FILE, "r") as f:
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        return set()

def run_dig():
    try:
        output = subprocess.check_output(["dig", "+short", HOSTNAME])
        lines = output.decode("utf-8").splitlines()
        return [line.strip() for line in lines if line.strip()]
    except subprocess.CalledProcessError:
        return []

def main():
    all_new_ips = set()
    for _ in range(LOOKUPS):
        new_ips = run_dig()
        all_new_ips.update(new_ips)
        time.sleep(DELAY_BETWEEN + random.uniform(0, 1))

    existing_ips = get_current_ips()
    unique_new_ips = sorted(set(all_new_ips) - existing_ips)

    if unique_new_ips:
        with open(EDL_FILE, "a") as f:
            for ip in unique_new_ips:
                f.write(ip + "\n")
        print(f"✅ Added {len(unique_new_ips)} new IPs:")
        for ip in unique_new_ips:
            print(" -", ip)
    else:
        print("ℹ️ No new IPs found.")

if __name__ == "__main__":
    main()
