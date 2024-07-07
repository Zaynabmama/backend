import yaml
import os

config_file = os.path.join(os.path.dirname(__file__), '../fullstack-repo/config.yaml')

with open(config_file, 'r') as f:
    config = yaml.safe_load(f)

server = config.get('ServerIPAddress')
print(f"Starting server at IP address: {server}")
