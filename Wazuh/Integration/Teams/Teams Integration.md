

global configuration api call

```xml
<!-- Webhook to teams general alerts -->
  <integration> 
    <name>custom-teams</name>
    <!-- ^^ script name to be called ^^ -->
    <hook_url>WebHookURL</hook_url>
    <!-- ^^ webhook url + key ^^ -->
    <alert_format>json</alert_format> 
    <!-- ^^ log format ^^ -->
    <level>3</level>
    <!-- ^^ minimum rule level to call this ^^ -->
  </integration> 

```

copy both custom-teams and custom-teams.py to /var/ossec/integrations/
