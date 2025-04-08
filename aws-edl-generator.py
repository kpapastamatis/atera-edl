import requests

url = "https://ip-ranges.amazonaws.com/ip-ranges.json"
response = requests.get(url)
data = response.json()

# Παίρνουμε μόνο τα IPv4 prefixes
all_ipv4 = sorted(set([prefix["ip_prefix"] for prefix in data["prefixes"]]))

# Αποθήκευση στο αρχείο edl.txt (ώστε να παρακολουθείται από το GitHub)
with open("edl.txt", "w") as f:
    for ip in all_ipv4:
        f.write(ip + "\n")
