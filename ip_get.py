#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,socket,fcntl,struct
from urllib import urlopen


def public_ip():
    read_res = urlopen('http://ipecho.net/plain').read()
    return read_res.decode('utf-8')


def local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', "eth0"[:15]))[20:24])

if __name__ == "__main__":
    print("Getting public and local IP...")
    print("Public IP:%s\nLocal IP: %s"%(public_ip(), local_ip()))

