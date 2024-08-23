#!/usr/bin/env js
# Created by Shuffle, AS. <frikky@shuffler.io>.
# Based on the Slack integration using Webhooks

import json
import sys
import time
import os
from pathlib import Path
from urllib.parse import urlparse

try:
    import requests
    from requests.auth import HTTPBasicAuth

except Exception as e:
    print("No module 'requests' found. Install: pip install requests")
    sys.exit(1)

# ADD THIS TO ossec.conf configuration:
#  <integration>
#      <name>custom-shuffle</name>
#      <hook_url>/file_containing_weebhook</hook_url>
#      <api_key>null</api_key>
#      <level>3</level>
#      <alert_format>json</alert_format>
#  </integration>
 # Global vars

debug_enabled = False
pwd = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
json_alert = {}
now = time.strftime("%a %b %d %H:%M:%S %Z %Y")

# Set paths
log_file = '{0}/logs/integrations.log'.format(pwd)
def main(args):
    debug("# Starting")
    # Read args
    alert_file_location = args[1]
    webhook = args[3]
    webhook_file_path = args[3]
    
    # Read the webhook URL from the file
    try:
        with open(webhook_file_path, 'r') as file:
            webhook = file.read().strip()
    except Exception as e:
        debug(f"Error reading webhook URL from file {webhook_file_path}: {e}")
    debug("# Webhook")
    debug(webhook)
    debug("# File location")
    debug(alert_file_location)

    # Load alert. Parse JSON object.
    with open(alert_file_location) as alert_file:
        json_alert = json.load(alert_file)
    debug("# Processing alert")
    debug(json_alert)
    debug("# Generating message")
    msg = generate_msg(json_alert)
    if isinstance(msg, str):
        if len(msg) == 0:
            return
        debug(msg)
    debug("# Sending message")
    send_msg(msg, webhook)

def debug(msg):
    if debug_enabled:
      msg = "{0}: {1}\n".format(now, msg)
      print(msg)
      f = open(log_file, "a")
      f.write(msg)
      f.close()

# Skips container kills to stop self-recursion
def filter_msg(alert):
    # These are things that recursively happen because Shuffle starts Docker containers
    skip = ["87924", "87900", "87901", "87902", "87903", "87904", "86001", "86002", "86003", "87932", "80710", "87929", "87928", "5710"]

    if alert["rule"]["id"] in skip:
        return False

    #try:
    #if "docker" in alert["rule"]["description"].lower() and "
    #msg['text'] = alert.get('full_log')
    #except:
    #pass
    #msg['title'] = alert['rule']['description'] if 'description' in alert['rule'] else "N/A"

    return True

def generate_msg(alert):
    alertTitle = "Wazuh Alert"
    level = alert['rule']['level']
    if (level <= 4):
            color = "Good"
            color_hex = "38F202"
    elif (level >= 5 and level <= 7):
            color = "warning"
            color_hex = "F2EB02"
    else:
            color = "attention"
            color_hex = "F22A02"

    if 'agent' in alert:
      agentIdName = "({0}) - {1}".format(
            alert['agent']['id'],
            alert['agent']['name']
          )
    elif 'agentless' in alert:
        agentIdName = "Agentless host {0}".format(alert['agentless']['host'])
    else:
        agentIdName = "N/A"

# Initialize the Adaptive Card structure
    adaptive_card = {
        "alertTitle": alertTitle,
        "level": level,
        "color": color,
	    "color_hex": color_hex,
        "agentIdName": agentIdName,
        "location": alert['location'],
        "ruleID": "{0} _(Level {1})_".format(alert['rule']['id'], level),
        "description": alert['rule']['description'] if 'description' in alert['rule'] else "N/A",
        "fullLog": alert.get('full_log') if 'full_log' in alert else "N/A",
	"info": alert['rule']['info'] if 'info' in alert['rule'] else "",
    }
    
    # Convert the Adaptive Card structure to a JSON string
    adaptive_card_json = json.dumps(adaptive_card, indent=2)
    
    return adaptive_card_json


def send_msg(msg, url):
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    res = requests.post(url, data=msg, headers=headers)
    debug(res)

if __name__ == "__main__":
    try:
        # Read arguments
        bad_arguments = False
        if len(sys.argv) >= 4:
            msg = '{0} {1} {2} {3} {4}'.format(
                now,
                sys.argv[1],
                sys.argv[2],
                sys.argv[3],
                sys.argv[4] if len(sys.argv) > 4 else '',
            )

            debug_enabled = (len(sys.argv) > 4 and sys.argv[4] == 'debug')
        else:
            msg = '{0} Wrong arguments'.format(now)
            bad_arguments = True

        # Logging the call
        f = open(log_file, 'a')
        f.write(msg + '\n')
        f.close()
        if bad_arguments:
            debug("# Exiting: Bad arguments.")
            sys.exit(1)

        # Main function
        main(sys.argv)
    except Exception as e:
        debug(str(e))
        raise
