source: https://github.com/maikroservice/wazuh-discord-integration/tree/main

global configuration api call
```xml
 <integration>
     <name>custom-discord</name>
     <hook_url>https://discord.com/api/webhooks/XXXXXXXXXXX</hook_url>
     <alert_format>json</alert_format>
 </integration>
```


copy both custom-discord and custom-discord.py to /var/ossec/integrations/

set permissions 
```
sudo chmod 750 /var/ossec/integrations/custom-*
sudo chown root:wazuh /var/ossec/integrations/custom-*
```

I'm customizing the .py so dynamic fields are generated depending on the alert for now I have setup network fields, and will make it also behave in a way that user and origin is displayed in case o access alerts
