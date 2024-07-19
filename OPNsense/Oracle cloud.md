since free account can't upload custom images it is necessaire to do some OS transformations

you start whit a ubuntu machine then transform it to BSD and import base config, after that install opnsense through CLI


source: https://forum.opnsense.org/index.php?topic=32546.0

##### [Quick tutorial: how to deploy OPNsense easily on Oracle Cloud for free.](https://forum.opnsense.org/index.php?topic=32546.msg157450#msg157450)

« **on:** February 18, 2023, 05:56:30 am »

Hi Everyone,  
  
Been using pfsense for many years before switching to opnsense at its inception.  
Used the forums for years silently, and am very happy with this fantastic piece of software.  
  
Today I am reporting a successful deployment of Opnsense on an Oracle Cloud free instance.  
Thought I'd share this short tutorial to give back to the community, hoping it'll be useful to someone out there:  
  
**Some Background** (_you can skip this section and go straight to the OCI tutorial_):  
  
I have been using Opnsense on several VPS providers successfully over the years.  
First Digital Ocean, then Vultr, then Upcloud.  
The switch was done each time to select a VPS location closer to me for better latency.  
The three were good from a technical standpoint, although Vultr is to be avoided if you do not want to be outright scammed.  ![::)](https://forum.opnsense.org/Smileys/default/rolleyes.gif "Roll Eyes")  
Was most recently on Upcloud, they have a great platform, great customer service, but they jacked up their monthly subscription price by nearly 50% overnight due to rising energy costs, so I decided to check out alternatives.  
A few months ago I started a free trial on OCI. Unfortunately the location I had selected did not have any available capacity during the initial free trial period.  
Recently some "_Always Free_" AMD instances, 1CPU core / 1GB ram became available in my preferred location, so I decided to deploy Opnsense.  
Freebsd & Opnsense are not offered as options on OCI for X64, so a bit of creativity was in order.  
  
**OCI free instance deployment steps:**  
  
-Prepare an xml config for the Oracle deployment on a local machine.  
The main _required_ changes from vanilla were:  
      - 1 NIC only for WAN, configured via DHCP  
      - Disable HTTP_REFERER enforcement check  
       
- Create a VCN and Public subnet on OCI, setup the Oracle firewall to allow SSH/HTTP/HTTPS ingress  
  
- Fire up an Oracle Linux instance on AMD (mine was VM.Standard.E2.1.Micro -1 core 2.55 GHz AMD EPYC\u2122 7J13).  
An SSH key was uploaded during instance setup for remote access.  
  
- Convert the Oracle Linux instance into a FreeBSD instance via SSH using:  

Code: [Select]

```
# wget https://download.freebsd.org/ftp/releases/VM-IMAGES/13.1-RELEASE/amd64/Latest/FreeBSD-13.1-RELEASE-amd64.raw.xz # xz -dc FreeBSD-13.1-RELEASE-amd64.raw.xz | sudo dd of=/dev/sda bs=1M conv=fdatasync
```

Where sda is the boot disk.  
Reboot to Freebsd  
  
- Upload the prepared config.xml to the Freebsd instance using ssh  
  
- Convert FreeBSD into Opnsense via SSH using opnsense-bootstrap:  

Code: [Select]

```
# pkg install ca_root_nss# fetch https://raw.githubusercontent.com/opnsense/update/master/src/bootstrap/opnsense-bootstrap.sh.in# sh ./opnsense-bootstrap.sh.in -r 23.1
```

  
- Using web based cloud console interface, load the previously prepared config.xml during opnsense first boot  
  
Now the Opensense instance is accessible via the web interface for further configuration.  
Since this setup was done using an Always Free instance, the good news is this cloud based edge router comes at no cost.  
  
Enjoy  ![:)](https://forum.opnsense.org/Smileys/default/smiley.gif "Smiley")