import socket
from termcolor import colored

def scan(target, ports):
    print('\nStarting scan for ' + str(target))
    try:
        for port in range(1, ports):
            scan_port(target, port)
    except KeyboardInterrupt:
        print("\n[!] Scan stopped by user")

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ipaddress, port))
        print("[+] Port open: " + str(port))
        sock.close()
    except:
        pass

targets = input("[*] Enter targets to scan (split by ,): ")
ports = int(input("[*] Enter how many ports you want to scan: "))

if ',' in targets:
    print(colored("[*] Scanning multiple targets", 'magenta'))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(), ports)
else:
    scan(targets, ports)
    
    print("="*40)
print("      SIMPLE PORT SCANNER")
print("="*40)