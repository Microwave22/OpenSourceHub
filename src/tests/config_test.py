import sys
import json
sys.path.insert(1, '../')
from config import config
Config = config.Config("config.json")

def test():
  Config.generateConfig()
  Config.readVariable("connection_server")
  Config.changeVariable("connection_server", "192.168.1.1")
  Config.deleteVariable("connection_port")
  result_file = open('config.json', 'r').read()
  return result_file

if __name__ == "__main__":
  test_result = test()
  if str(test_result) == """{"connection_server": "192.168.1.1", "allow_onion_ip": "False"}""":
    print("TEST PASSED")
  else:
    print("TEST FAILED")


