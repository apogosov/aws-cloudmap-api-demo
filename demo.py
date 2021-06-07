import pprint
import boto3
from botocore.config import Config
import os


clear = lambda: os.system('clear')

my_config = Config(
    region_name = 'us-east-1',
    signature_version = 'v4',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)

pp = pprint.PrettyPrinter(indent=4)
client = boto3.client('servicediscovery', config = my_config)
clear()
input("---------- List Namespaces ----------")
response = client.list_namespaces()
pp.pprint(response)

input("Pause...")

