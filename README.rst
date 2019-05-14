=====
python-netdiscover
=====

The  python-netdiscover is a simple wrapper for the [netdiscover reconnaissance tool](https://sourceforge.net/projects/netdiscover/)

This library offers a simple way to create scans from a python script and analyse the results.

Installation
============
From the shell, uncompress python-netdiscover.tar.gz and then run make :

.. code-block:: bash

    $ tar xvzf python-netdiscover.tar.gz
    $ cd python-netdiscover
    $ python setup.py install

or using Pip

.. code-block:: bash

    $ pip install python-netdiscover


Usage
=====
From python/ipython:
--------------------

.. code-block:: python
    >>> from netdiscover import *
    >>> disc = Discover()
    >>> disc.scan(ip_range="192.168.1.0/24")
    [{'mac': b'73:8b:10:0e:bd:23', 'ip': b'192.168.2.1'}, {'mac': b'f4:3c:4a:73:47:07', 'ip': b'192.168.2.2'}]


