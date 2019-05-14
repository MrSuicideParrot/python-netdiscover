=====
Usage
=====

To use python-netdiscover in a project::

    from netdiscover import *
    
    disc = Discover()
    
    hosts = disc.scan(ip_range="192.168.1.0/24")

    for i in hosts:
        print("%s -> %s" % (i["ip"], i["mac"]))

