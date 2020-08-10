#!/usr/bin/python3
import os
import json

class Config(object):
# CRUD App like config manager
  def __init__(self, config_path):
    self.config_path = config_path
    self.config_file = self.loadConfig()
    
  def loadConfig(self):
    try:
      with open(str(self.config_path), "r+") as f:
        config_file = json.loads(f.read())
        return config_file
    except FileNotFoundError:
      print("File Does Not Exist, Assuming you will be using Generate Config")

  def generateConfig(self, ConnectionServer="localhost", ConnectionPort=5000, AllowOnionIp=False):
    os.mknod(str(self.config_path))
    configSettings = {
      'connection_server': f'{ConnectionServer}',
      'connection_port': f'{ConnectionPort}',
      'allow_onion_ip': f'{AllowOnionIp}'
    }
    with open(self.config_path, "w") as fp:
      configJson = json.dump(configSettings, fp)
      fp.close()
    self.config_file = self.loadConfig()


  def readVariable(self, config_variable):
    return print(self.config_file[config_variable])

  def changeVariable(self, config_variable, new_value):
    self.config_file[str(config_variable)] = str(new_value)
    config_path = open(self.config_path, 'r+')
    json.dump(self.config_file, config_path)
    return self.config_file

  def deleteVariable(self, config_variable):
    self.config_file.pop(config_variable)
    config_path = open(self.config_path, 'w')
    json.dump(self.config_file, config_path)
    return self.config_file

