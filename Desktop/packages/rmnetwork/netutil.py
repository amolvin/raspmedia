import netifaces

def ip4_addresses():
    ips = _ip_addresses(False)
    return ips

def ip6_addresses():
    ips = _ip_addresses(True)
    return ips

def _ip_addresses(v6):
    ip_list = []

    interfaces = netifaces.interfaces()
    for i in interfaces:
        if i == 'lo':
            continue
        if v6:
            iface = netifaces.ifaddresses(i).get(netifaces.AF_INET6)
        else:
            iface = netifaces.ifaddresses(i).get(netifaces.AF_INET)
        if iface != None:
            for j in iface:
                curIP = j['addr']
                if v6:
                    check_ip6_address(curIP)
                ip_list.append(curIP)

    return ip_list

def check_ip6_address(ip6):
    pass