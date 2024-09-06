from scapy.layers.inet import IP, TCP
from scapy.sendrecv import sr, sr1
import socket
from tqdm import tqdm
import time
def scan_ports(ip, port_range):
    open_ports = []
    closed_ports = []
    total_ports = port_range[1] - port_range[0] + 1

    with tqdm(total=total_ports, desc="Scanning", unit="port") as pbar:
        for port in range(port_range[0], port_range[1] + 1):
            packet = IP(dst=ip) / TCP(dport=port, flags="S")
            response = sr1(packet, timeout=0.5, verbose=0)

    for port in range(port_range[0], port_range[1]+1):
        packet = IP(dst=ip)/TCP(dport=port, flags="S")
        response = sr1(packet, timeout=0.5, verbose=0)

        if response is not None:
            if response.haslayer(TCP) and response[TCP].flags == "SA":
                open_ports.append(port)
            elif response.haslayer(TCP) and response[TCP].flags == "RA":
                closed_ports.append(port)
    return open_ports, closed_ports

def get_service_name(port):
    try:
        return socket.getservbyport(port, "tcp")
    except OSError:
        return "Unknown"


def display_results(open_ports, closed_ports):
    total_ports = len(open_ports) + len(closed_ports)

    with tqdm(total=total_ports, desc="Displaying Results", unit="port") as pbar:
        print("\nOpen ports and services:")
        for port in open_ports:
            print(f"Port {port} is open - {get_service_name(port)}")
            pbar.update(1)
            time.sleep(0.1)  # Small delay for visual effect

        print("\nClosed ports:")
        for port in closed_ports:
            print(f"Port {port} is closed")
            pbar.update(1)
            time.sleep(0.01)  # Smaller delay for closed ports

        print("\nSummary:")
        print("Open ports:")
        for port in open_ports:
            print(f"Port {port} - {get_service_name(port)}")
        print("\nClosed ports:")
        for port in closed_ports:
            print(f"Port {port} - {get_service_name(port)}")


ip = input("Enter IP Address: ")
port_range = input("Enter Port Range (start-end): ")
start_port, end_port = map(int, port_range.split('-'))
open_ports, closed_ports = scan_ports(ip, (start_port, end_port))

print(f"Total Ports Scanned: {end_port - start_port + 1}")
print(f"Open ports: {len(open_ports)}")
print(f"Closed ports: {len(closed_ports)}")

display_results(open_ports, closed_ports)

print("\nOpen ports and services:")
for port in open_ports:
    print(f"Port {port} is open - {get_service_name(port)}")

print("\nClosed ports:")
for port in closed_ports:
    print(f"Port {port} is closed")

print("\nSummary:")
print("Open ports:")
for port in open_ports:
    print(f"Port {port} - {get_service_name(port)}")
print("\nClosed ports:")
for port in closed_ports:
    print(f"Port {port} - {get_service_name(port)}")