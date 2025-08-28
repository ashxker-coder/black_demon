import socket

def run(target, use_tor=False):
    """
    Simple port scanning module.
    Scans a set of common ports on the target.
    
    :param target: Target IP or domain
    :param use_tor: Boolean, if Tor mode is enabled
    """
    print(f"[+] Running Port Scan on {target}")
    if use_tor:
        print("[*] Note: Tor mode is enabled, but this module currently does not support SOCKS proxy.")
    
    # Common ports to scan
    ports = [21, 22, 25, 53, 80, 110, 143, 443, 3306, 8080]

    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[OPEN] Port {port}/tcp")
            s.close()
        except KeyboardInterrupt:
            print("\n[!] Scan aborted by user")
            break
        except Exception as e:
            print(f"[!] Error scanning port {port}: {e}")
