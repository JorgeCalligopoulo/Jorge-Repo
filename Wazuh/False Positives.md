
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


latest Diff being detected as Trojan file 
" Trojaned version of file '/usr/bin/diff' detected. Signature used: 'bash|^/bin/sh|file\.h|proc\.h|/dev/[^n]|^/bin/.*sh' (Generic)."

/var/ossec/etc/rootcheck/rootkit_trojans.txt
```
-diff        !bash|^/bin/sh|file\.h|proc\.h|/dev/[^n]|^/bin/.*sh!
+diff        !bash|^/bin/sh|file\.h|proc\.h|/dev/[^nf]|^/bin/.*sh!
```
or use a more recent version of the file >> /var/ossec/etc/shared/
https://github.com/ossec/ossec-hids/blob/master/src/rootcheck/db/rootkit_trojans.txt




