
Common:
LXC -- it is expected to be present in /dev so the bellow config can be incremented to ignore it
/var/ossec/etc/ossec.conf
```
<rootcheck>
<!-- (...) -->
    <ignore>/dev/.lxc-boot-id</ignore>
    <ignore>/dev/lxc</ignore>
    <ignore>/dev/.lxc</ignore>
  </rootcheck>
```


