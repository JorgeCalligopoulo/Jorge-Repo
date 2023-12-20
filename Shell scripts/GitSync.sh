#!/bin/bash
#script created to push from git updated files and update them inside wazuh in case changes were detected
#
cd /opt/gitSync
rm /opt/gitSync/custom-discord.py
rm /opt/gitSync/custom-discord
wget https://raw.githubusercontent.com/JorgeCalligopoulo/Projects/main/Wazuh/Integration/Discord/custom-discord.py
wget https://raw.githubusercontent.com/JorgeCalligopoulo/Projects/main/Wazuh/Integration/Discord/custom-discord

clear
echo "########   cleaning done, starting comparations   "

diff -q custom-discord /var/ossec/integrations/custom-discord 1>/dev/null
if [[ $? == "0" ]]
then
echo "########   custom-discord: no change, no action neded   "

else
echo "########   Pushing files to production"
rm /var/ossec/integrations/custom-discord
cp custom-discord /var/ossec/integrations/custom-discord
echo "########   custom-discord updated   "
chmod 750 /var/ossec/integrations/custom-discord
chown root:wazuh /var/ossec/integrations/custom-discord
echo "########   custom-discord updated-permissions   "

fi

diff -q custom-discord.py /var/ossec/integrations/custom-discord.py 1>/dev/null
if [[ $? == "0" ]]
then
echo "########   custom-discord.py: no change, no action neded   "

else
echo "########   Pushing files to production   "
rm /var/ossec/integrations/custom-discord.py
cp custom-discord.py /var/ossec/integrations/custom-discord.py
echo "########   custom-discord.py updated   "
chmod 750 /var/ossec/integrations/custom-discord.py
chown root:wazuh /var/ossec/integrations/custom-discord.py
echo "########   custom-discord updated-permissions   "
fi