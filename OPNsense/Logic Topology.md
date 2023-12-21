
```css
Home_Lab{
	OPNSense(host){
		Tunnel-to-oracle(ipsec)
		Lan(network layer)
		DNS(Unbound)}
	proxmox(cluster(2 hosts)){
		wazuh-dash(vm) -> host 1
		wazuh-index(vm) -> host 1
		wazuh-manager(vm) -> host 2}}
```

```css
Oracle-Cloud(free tier)
	VCN(network layer)
	Misp(vm)
	OPNSense(vm){
		Tunnel-to-Home_Lab(ipsec)
		wireguard(VPN)
		DNS(Unbound)}
```
Oracle(OPNSense) has a tunnel site-to-site to Home-lab(OPNSense), since Home-Lab ip address is dynamic he is the initiator always, and OPNSense sitting at cloud only waits for the connection

Wireguard is used to close a tunnel between personal devices and my lan allowing myself asses to resources all the time
