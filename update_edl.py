import socket
from datetime import datetime

# Static IPs
static_ips = [
    "3.248.116.102", "34.240.34.177", "34.240.35.131", "34.240.138.193",
    "34.240.227.14", "34.241.28.226", "34.241.39.86", "34.241.69.8",
    "34.241.182.193", "34.242.21.81", "34.242.71.99", "34.242.249.9",
    "34.242.176.154", "34.243.139.157", "34.246.87.13", "34.246.106.113",
    "34.248.255.203", "34.250.50.170", "34.251.175.67", "52.16.4.81",
    "52.16.176.212", "52.48.109.74", "52.214.189.164", "54.72.125.47",
    "54.74.42.110", "54.77.190.36", "54.194.1.42", "54.195.236.88",
    "54.246.140.239", "54.247.148.23", "54.247.164.78", "63.35.107.16"
]

domains = ["pubsub.atera.com", "pubsub.pubnub.com", "ps.pndsn.com"]

def resolve_domain(domain):
    try:
        return list(set([res[4][0] for res in socket.getaddrinfo(domain, None)]))
    except:
        return []

resolved_ips = set(static_ips)
for domain in domains:
    resolved_ips.update(resolve_domain(domain))

# Write to file
with open("atera_edl_ips.txt", "w") as f:
    for ip in sorted(resolved_ips):
        f.write(f"{ip}\n")
#    f.write(f"# Updated: {datetime.utcnow().isoformat()}Z\n")
