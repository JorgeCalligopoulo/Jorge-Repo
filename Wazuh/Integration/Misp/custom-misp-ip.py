#!/usr/bin/env python
import sys
import os
import json
from socket import socket, AF_UNIX, SOCK_DGRAM
from pymisp import ExpandedPyMISP

# Initialize a connection to your MISP instance
misp = ExpandedPyMISP('https://your_misp_instance', 'your_api_authkey', False, 'json')

def send_event(msg, agent = None):
   if not agent or agent["id"] == "000":
       string = '1:misp:{0}'.format(json.dumps(msg))
   else:
       string = '1:[{0}] ({1}) {2}->misp:{3}'.format(agent["id"], agent["name"], agent["ip"] if "ip" in agent else "any", json.dumps(msg))
   sock = socket(AF_UNIX, SOCK_DGRAM)
   sock.connect(socket_addr)
   sock.send(string.encode())
   sock.close()

# Read the alert file
alert = json.load(sys.stdin)

# Extract IP addresses from the alert
srcip = alert["data"]["srcip"]
dstip = alert["data"]["dstip"]

# Query the MISP database
srcip_result = misp.search(value=srcip, type='ip-src')
dstip_result = misp.search(value=dstip, type='ip-dst')

# Create the alert output
alert_output = {
   "srcip": srcip_result,
   "dstip": dstip_result
}

# Send the alert output
send_event(alert_output, alert["agent"])
