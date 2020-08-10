import wget
import json
import sys
sys.path.append(1, '../utils')
from tools import getIpType
sys.path.append(1, '../config')
from config import Config
Config = config.Config()
CONNECTION_SERVER = str(Config.Default("connection_server"))
CONNECTION_PORT = int(Config.Default("connection_port"))
ALLOW_ONION_IPS = bool(Config.Default("allow_onion_ips"))

def connect(repo):
  content = wget.download(f"http://{CONNECTION_SEVER}:{CONNECTION_PORT}/{repo}.json")
  with open(content) as f:
    repo_content = json.load(f)

   

