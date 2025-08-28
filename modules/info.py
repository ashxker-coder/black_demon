import socket
import http.client
from urllib.parse import urlparse

def run(target, use_tor=False):
    """
    Basic information gathering module.
    
    :param target: Domain or hostname
    :param use_tor: Boolean, if Tor mode is enabled
    """
    print(f"[+] Running Info Gathering on {target}")
    if use_tor:
        print("[*] Note: Tor mode is enabled, but this module does not currently support SOCKS proxy.")

    # DNS Resolution
    try:
        print("\n[*] Resolving host...")
        addrs = socket.getaddrinfo(target, None)
        unique_ips = set()
        for fam, _, _, _, sa in addrs:
            unique_ips.add(sa[0])
        if unique_ips:
            for ip in unique_ips:
                print(f"    - {ip}")
        else:
            print("    (No IP addresses found)")
    except Exception as e:
        print(f"[!] DNS resolution failed: {e}")
        return

    # Reverse Lookup
    print("\n[*] Reverse DNS lookup...")
    for ip in unique_ips:
        try:
            rev = socket.gethostbyaddr(ip)
            print(f"    {ip} -> {rev[0]}")
        except Exception:
            print(f"    {ip} -> (no PTR record)")

    # Fetch robots.txt
    print("\n[*] Fetching robots.txt...")
    try:
        conn = http.
