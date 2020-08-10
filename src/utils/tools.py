#!/usr/bin/python3
import re

def getIpType(ip):
  if ip.endswith(".onion"):
    return "onion"
  elif ":" in ip:
    return "ipv6"
  elif re.match(r"[0.9\.]+$", ip):
    return "ipv4"
  else:
    return "unknown"

