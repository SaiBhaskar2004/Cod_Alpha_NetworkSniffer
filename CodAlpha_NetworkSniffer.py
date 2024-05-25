pip install scapy
from scapy.all import *
def packet_callback(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        print(f"IP Packet: {src_ip} -> {dst_ip} [Protocol: {protocol}]")

        if packet.haslayer(TCP):
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            print(f"  TCP: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")
        
        if packet.haslayer(UDP):
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            print(f"  UDP: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")
        
        if packet.haslayer(ICMP):
            icmp_type = packet[ICMP].type
            icmp_code = packet[ICMP].code
            print(f"  ICMP: {src_ip} -> {dst_ip} [Type: {icmp_type}, Code: {icmp_code}]")
sniff(prn=packet_callback, store=0)
