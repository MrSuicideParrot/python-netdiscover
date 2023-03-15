import os
import subprocess
import sys
import shlex
import re

class Discover:

    def __init__(self, netdiscover_path=None, root_verify=True):
        """
        :param netdiscover_path: Path where is the netdiscover binary. If not defined it will search on defaults netdiscover locations
        :param root_verify: Verify if the user is root
        """
        if root_verify and os.getenv('USER') != 'root':
            raise Exception('Programming not running as root.')

        path_found = False

        netdiscover_search_path = ['netdiscover',
                                   '/usr/bin/netdiscover',
                                   '/usr/sbin/netdiscover',
                                   '/usr/local/bin/netdiscover',
                                   '/sw/bin/netdiscover',
                                   '/opt/local/bin/netdiscover']
        if netdiscover_path:
            netdiscover_search_path[0] = netdiscover_path

        for netdiscover_path in netdiscover_search_path:
            try:
                if sys.platform.startswith('freebsd') \
                        or sys.platform.startswith('linux') \
                        or sys.platform.startswith('darwin'):
                    p = subprocess.Popen([netdiscover_path, '-help'],
                                         bufsize=10000,
                                         stdout=subprocess.PIPE,
                                         close_fds=True)
                else:
                    p = subprocess.Popen([netdiscover_path, '-help'],
                                         bufsize=10000,
                                         stdout=subprocess.PIPE)

            except OSError:
                pass
            else:
                self._netdiscover_path = netdiscover_path  # save path
                path_found = True
                break

        if not path_found:
            raise Exception("netdiscover not found")

        self.command = 'netdiscover -P -N'

    def get_command(self):
        """
        :return: Commad used to scan the network
        """
        return self.command

    def scan(self, interface=None, ip_range=None, file=None, passive=False, filter_p=None, sleep=None, node=None,
             count=None, fast=None, sleep_supression=None, output=["ip","mac"]):
        """
        :param interface: Your network device
        :param ip_range: Scan a given range instead of auto scan. 192.168.6.0/24,/16,/8
        :param file: Scan the list of ranges contained into the given file
        :param passive:  Do not send anything, only sniff
        :param macs: File with the list of known MACs and host names
        :param filter_p: Customize pcap filter expression (default: "arp")
        :param sleep: Time to sleep between each arp request (miliseconds)
        :param node: Last ip octet used for scanning (from 2 to 253)
        :param count: Number of times to send each arp reques (for nets with packet loss)
        :param fast: Enable fastmode scan, saves a lot of time, recommended for auto
        :param sleep_supression:  Enable sleep time supression betwen each request (hardcore mode)
        :param output: List of elements that should be part of the output, by default thats ip and mac.

        :return: List with the result of the scan
        """
        self.command = 'netdiscover -P -N'

        if interface:
            self.command += " -i %s" % interface

        if ip_range:
            self.command += ' -r %s' % ip_range

        if file:
            self.command += ' -m %s' % file

        if passive:
            self.command += ' -p'

        """if macs:
            self.command += z"""

        if filter_p:
            self.command += ' -F %s' % filter_p

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

        self._raw_result = subprocess.check_output(shlex.split(self.command))
        self._scan_result = self.parse_output(self._raw_result, output)

        return self._scan_result

    @staticmethod
    def parse_output(data, output):
        """

        :param data: Raw output to parse
        :param output: List of elements that should be part of the output.
        :return: List with the results from the scan. Each result is represented by a dictionary.
        """

        # decode and split raw output
        content = data.decode("UTF-8").split("\n")

        # sanitize user coices for output
        output = [key for key in output if key in ("ip","mac","count","len","vendor")]

        results = []

        if len(content) != 0:
            for chunk in content:
                pars = re.search(r"\s?(?P<ip>\d+\.\d+\.\d+\.\d+)"
                                 r"\s+(?P<mac>[a-fA-F0-9:]{17})"
                                 r"\s+(?P<count>\d+)"
                                 r"\s+(?P<len>\d+)"
                                 r"\s+(?P<vendor>.*)",
                                 chunk)
                if pars:
                    pars = pars.groupdict()
                    results.append({key: pars[key] for key in output})

        return results
