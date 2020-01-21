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

## Change PI wifi
```
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```

## Add ssh key to server
```
cat ~/.ssh/id_rsa.pub | ssh andybao@192.168.10.122 'cat >> ~/.ssh/authorized_keys'
```

## Create soft link
```
ln -s link soft_link_name
ln -sfn {path/to/file-name} {link-name}
```

## Create python venv using sys config
```
python3 -m venv --system-site-packages py3env
```

## restart bluetooth
```
sudo service bluetooth restart
```