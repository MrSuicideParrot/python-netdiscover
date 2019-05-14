==================
python-netdiscover
==================

The  python-netdiscover is a simple wrapper for the `netdiscover reconnaissance tool <https://sourceforge.net/projects/netdiscover/>`_.

This library offers a simple way to create scans from a python script and analyse the results.

Notes
=====
This tool needs to be run as root. It is necessary to be presented on the system the *netdiscover* tool. The library will look for the *netdiscovery* binary in the following paths:

*  netdiscover
* /usr/bin/netdiscover
* /usr/sbin/netdiscover
* /usr/local/bin/netdiscover
* /sw/bin/netdiscover
* /opt/local/bin/netdiscover

If *netdiscovery* is not present in any of the paths above, you can specifie path with the argument *netdiscover_path* on Discover class.

.. code-block:: python

    disc = Discover(netdiscover_path="path_of_netdiscover")