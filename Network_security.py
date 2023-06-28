from scapy.all import *

# Example: Basic packet sniffing and analysis
def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"Source IP: {src_ip} --> Destination IP: {dst_ip}")

sniff(filter="ip", prn=packet_callback, store=0)
