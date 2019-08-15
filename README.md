# Command

## Read syslog

```
sudo tail -f /var/log/syslog -n 5000 | more

tail -f /var/log/syslog
```

## Check python process

```
ps aux | grep python
```

## Check PI port 80
sudo tcpdump -A -s 0 'tcp port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0'