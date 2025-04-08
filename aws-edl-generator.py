import requests

url = "https://ip-ranges.amazonaws.com/ip-ranges.json"
response = requests.get(url)
data = response.json()

# Παίρνουμε μόνο τα IPv4 prefixes
all_ipv4 = sorted(set([prefix["ip_prefix"] for prefix in data["prefixes"]]))

# Αποθήκευση στο αρχείο
with open("aws-all-ipv4.txt", "w") as f:
    for ip in all_ipv4:
        f.write(ip + "\n")

print(f"✅ Saved {len(all_ipv4)} IPv4 ranges to aws-all-ipv4.txt")
