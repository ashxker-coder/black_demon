#!/usr/bin/env python3
import argparse
from core import BlackDemon

def main():
    parser = argparse.ArgumentParser(
        description="Black Demon - Lightweight Pentest Framework (for authorized use only)"
    )
    parser.add_argument(
        "module",
        help="Module name to run (e.g., portscan, httpcheck, info)"
    )
    parser.add_argument(
        "target",
        help="Target IP or domain"
    )
    parser.add_argument(
        "--tor",
        action="store_true",
        help="Enable Tor mode (modules route traffic through Tor if supported)"
    )
    args = parser.parse_args()

    demon = BlackDemon(use_tor=args.tor)
    demon.run_module(args.module, args.target)

if __name__ == "__main__":
    main()
