#!/usr/bin/python3
import os
import json
from pathlib import Path

class Config(object):
# CRUD App like config manager
  def __init__(self, config_path):
    self.config_path = config_path
    self.config_file = self.loadConfig()

  def loadConfig(self):
    try:
      with open(self.config_path) as f:
        config_file = json.loads(f.read())
      return config_file
    except FileNotFoundError:
      print("File Does Not Exist, Assuming you will be using GenerateConfig")
   
  def generateConfig(self, ConnectionServer="localhost", ConnectionPort=5000, AllowOnionIp=False):
    Path(self.config_path).touch()
    configSettings = {
      'connection_server': f'{ConnectionServer}',
      'connection_port': f'{ConnectionPort}',
      'allow_onion_ip': f'{AllowOnionIp}'
    }
    with open(self.config_path) as fp:
      configJson = json.dump(configSettings, fp)
      fp.close()

  def readVariable(self, config_variable):
    config_json = json.loads(self.config_file)
    return config_json[config_variable]

  def changeVariable(self, config_variable, new_value):
    config_json = json.loads(self.config_file)
    config_json[config_variable] = new_value
    return config_json

  def deleteVariable(self, config_variable):
    config_json = json.loads(self.config_file)
    config_json.pop(config_variable)
    return config_json

