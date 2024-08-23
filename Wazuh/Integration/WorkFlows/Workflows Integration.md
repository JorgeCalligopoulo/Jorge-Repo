Workflows integration to be used alongside power automate...... because teams integrations are being discontinued.

https://feedbackportal.microsoft.com/feedback/idea/80ed6877-b642-ef11-b4ad-000d3a7aba8b

it was make based on previous teams integration

The msg part of the code was updated to send adaptive card on body: https://adaptivecards.io/designer/

custom-teams-workflow.py is to be used whit weebrook

```python
  <integration> 
    <name>custom-teams-workflow2</name>
    <hook_url>weebrookURL</hook_url>
    <api_key>null</api_key>
    <alert_format>json</alert_format> 
    <level>0</level>
    <group>sshd</group>
  </integration>
```


custom-teams-workflow2.py is to be used pointing to a file that only contain the weebhook as an example bellow

echo "weebhookURL" > /home/root/weebhook_hml

```ptthon
  <integration> 
    <name>custom-teams-workflow2</name>
    <hook_url>/home/root/weebhook_hml</hook_url>
    <api_key>null</api_key>
    <alert_format>json</alert_format> 
    <level>0</level>
    <group>sshd</group>
  </integration>
```

thats because i encountered misbehavior whit how the weebhook is generated on power automate

the URL address has the character "&" that upon saving is transformed into  "&amp;" using wazuh dashboard


Power automate:

---


- Start: When a Teams webhook request is received

Who can trigger the flow?:  Anyone

---

Parse Json
```json
{

"type": "object",

"properties": {

"alertTitle": {

"type": "string"

},

"level": {

"type": "integer"

},

"color": {

"type": "string"

},

"color_hex": {

"type": "string"

},

"agentIdName": {

"type": "string"

},

"location": {

"type": "string"

},

"ruleID": {

"type": "string"

},

"description": {

"type": "string"

},

"fullLog": {

"type": "string"

},

"info": {

"type": "string"

}

}

}
```

---

Compose

```json
{  
"type": "AdaptiveCard",  
"body": [  
{  
"type": "TextBlock",  
"text": "██████████████████████████████████████████████████████████████████",  
"color": <dynamic Color>,  
"horizontalAlignment": "Center",  
"spacing": "None",  
"fontType": "Monospace"  
},  
{  
"type": "TextBlock",  
"text": <dynamic Tittle>,  
"wrap": true,  
"horizontalAlignment": "Left",  
"spacing": "Medium",  
"weight": "Bolder"  
},  
{  
"type": "TextBlock",  
"text": <dynamic desc>,  
"horizontalAlignment": "Left",  
"weight": "Bolder",  
"wrap": true  
},  
{  
"type": "TextBlock",  
"text": <dynamic info>,  
"horizontalAlignment": "Left",  
"weight": "Bolder",  
"wrap": true  
},  
{  
"type": "FactSet",  
"facts": [  
{  
"title": "Agent",  
"value":  <dynamic>
},  
{  
"title": "Location",  
"value":  <dynamic>
},  
{  
"title": "Rule ID",  
"value":  <dynamic>
},  
{  
"title": "Log",  
"value":  <dynamic>
}  
],  
"spacing": "Large"  
}  
],  
"$schema": "http://adaptivecards.io/schemas/adaptive-card.json",  
"msteams": {  
"width": "full"  
},  
"version": "1.0"  
}
```


- Second Step: Post message in a chat or channel

adaptive card field select the output from compose