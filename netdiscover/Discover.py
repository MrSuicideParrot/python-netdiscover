import os
import subprocess

class Discover:

    def __init__(self, interface, range=None, file=None, passive=False,
                 macs=None, filter=None, sleep=None, node=None, count=None, fast=True,
                 sleep_supression=False, netdiscover_path=None):
        """
        :param interface: Your network device
        :param range: Scan a given range instead of auto scan. 192.168.6.0/24,/16,/8
        :param file: Scan the list of ranges contained into the given file
        :param passive:  Do not send anything, only sniff
        :param macs: File with the list of known MACs and host names
        :param filter: Customize pcap filter expression (default: "arp")
        :param sleep: Time to sleep between each arp request (miliseconds)
        :param node: Last ip octet used for scanning (from 2 to 253)
        :param count: Number of times to send each arp reques (for nets with packet loss)
        :param fast: Enable fastmode scan, saves a lot of time, recommended for auto
        :param sleep_supression:  Enable sleep time supression betwen each request (hardcore mode)
        """
        if os.getenv('USER') == 'root':
            raise Exception('Programming not running as root.')

        if netdiscover_path:
            self.netdiscover_path = netdiscover_path

        else:





        self.command = 'netdiscover -P -N -i %s' % interface

        if range:
            self.command += ' -r %s' % range

        if file:
            self.command += ' -m %s' % file

        if passive:
            self.command += ' -p'

        """if macs:
            self.command += z"""

        if filter:
            self.command += ' -F %s' % filter

        if sleep:
            self.command += ' -s %d' % sleep

        if node:
            self.command += ' -n %d' % node

        if count:
            self.command += ' -c %d' % count

        if fast:
            self.command += ' -f'

        if sleep_supression:
           self.command += ' -S'

    def get_command(self):
        return self.command

    def scan(self):
        self.raw_result = subprocess.Popen()
