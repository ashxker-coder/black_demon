import http.client
from urllib.parse import urlparse
import re

# Security headers we want to check
SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy",
    "Permissions-Policy"
]

def run(target, use_tor=False):
    """
    Basic HTTP security header check.
    
    :param target: Target URL or hostname
    :param use_tor: Boolean, if Tor mode is enabled
    """
    print(f"[+] Running HTTP Security Check on {target}")
    if use_tor:
        print("[*] Note: Tor mode is enabled, but this module does not currently support SOCKS proxy.")

    # Ensure the target has a scheme
    if not re.match(r'^https?://', target, re.I):
        target = "http://" + target

    u = urlparse(target)
    port = u.port or (443 if u.scheme == "https" else 80)
    conn_cls = http.client.HTTPSConnection if u.scheme == "https" else http.client.HTTPConnection

    try:
        conn = conn_cls(u.hostname, port=port, timeout=3)
        conn.request("HEAD", u.path or "/", headers={"User-Agent": "BlackDemon/1.0"})
        resp = conn.getresponse()
        headers = {k: v for k, v in resp.getheaders()}

        print(f"[*] Response: {resp.status} {resp.reason}")
        print(f"[*] Server: {headers.get('Server', '(not disclosed)')}")
        print(f"[*] X-Powered-By: {headers.get('X-Powered-By', '(none)')}")

        missing = [h for h in SECURITY_HEADERS if h not in headers]
        if missing:
            print("[!] Missing important security headers:")
            for h in missing:
                print(f"    - {h}")
        else:
            print("[+] All key security headers are present.")

    except Exception as e:
        print(f"[!] Error checking {target}: {e}")
    finally:
        try:
            conn.close()
        except Exception:
            pass
