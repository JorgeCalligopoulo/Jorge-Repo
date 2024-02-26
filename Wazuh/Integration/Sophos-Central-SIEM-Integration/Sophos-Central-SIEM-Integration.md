Integrator from sophos
https://github.com/sophos/Sophos-Central-SIEM-Integration
remember to config it!

to collect logs every x time I use a cron rule to run the script 
```crontab
*/5 * * * * /Sophos-Central-SIEM-Integration/run.sh
```

/Sophos-Central-SIEM-Integration/run.sh
```sh
#!/bin/sh
cd "$(dirname "$0")";
CWD="$(pwd)"
echo $CWD
python3 siem.py
```

to grab the logs generate add the folowing to the manager configuration

```xml
  <localfile>
    <log_format>json</log_format>
    <location>/Sophos-Central-SIEM-Integration/log/result.log</location>
  </localfile>
```
