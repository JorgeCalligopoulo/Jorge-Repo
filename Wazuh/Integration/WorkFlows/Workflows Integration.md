Workflows integration to be used alongside power automate...... because teams integrations are being discontinued.

it was make based on previous teams integration


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



