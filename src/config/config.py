#!/usr/bin/python3
import os
import json
from pathlib import Path

class Config(object):
  def __init__(self, config_path):
    self.config_path = config_path
    self.config_file = self.LoadConfig()

  def LoadConfig(self):
    try:
      with open(self.config_path) as f:
        config_file = json.loads(f.read())
      return config_file
    except FileNotFoundError:
      print("File Does Not Exist, Assuming you will be using GenerateConfig")
   
  def GenerateConfig(self, ConnectionServer="localhost", ConnectionPort=5000, AllowOnionIp=False):
    Path(self.config_path).touch()
    configSettings = {
      'connection_server': f'{ConnectionServer}',
      'connection_port': f'{ConnectionPort}',
      'allow_onion_ip': f'{AllowOnionIp}'
    }
    with open(self.config_path) as fp:
      configJson = json.dump(configSettings, fp)
      fp.close()

 #TODO: Finish Config Module

