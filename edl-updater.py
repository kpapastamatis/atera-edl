import subprocess
import re
from pathlib import Path

DOMAIN = "a32dl55qcodech-ats.iot.eu-west-1.amazonaws.com"
NUM_QUERIES = 100
edl_file = Path("edl.txt")

# Get current IPs from the file
existing_ips = set()
if edl_file.exists():
    existing_ips = set(edl_file.read_text().splitlines())

# Do dig queries and extract A records
new_ips = set()
for _ in range(NUM_QUERIES):
    result = subprocess.run(["dig", "+short", DOMAIN], capture_output=True, text=True)
    ips = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", result.stdout)
    new_ips.update(ips)

# Merge and sort unique IPs
all_ips = sorted(existing_ips.union(new_ips))

# Write back to the file
edl_file.write_text("\n".join(all_ips) + "\n")
