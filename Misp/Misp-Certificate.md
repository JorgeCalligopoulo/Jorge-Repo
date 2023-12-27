Certificate can be found att /etc/ssl/private/misp.local.crt and misp.local.key

note: backup the old certificate in case it is needed, 
```shell
mkdir old
cp misp.local.crt old/misp.local.crt
cp misp.local.key old/misp.local.key
```
I had the problem of firefox refusing to open the page because of ¨SEC_ERROR_INADEQUATE_CERT_TYPE¨ it was a config error while generating the certificate. inside opnsense I was creating it a server type, since that did not worked after some Search i discovery that the type of certificate was invalid for a web-server and creating it as  ¨Combined Client/Server Certificate¨ it was accepted.