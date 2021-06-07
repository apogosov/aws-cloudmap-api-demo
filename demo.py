import pprint
import boto3
from botocore.config import Config
import os

clear = lambda: os.system('clear')

my_config = Config(
    region_name='us-east-1',
    signature_version='v4',
    retries={
        'max_attempts': 10,
        'mode': 'standard'
    }
)

my_namespace = 'productbased.service.consul'
my_service = 'configuration-storage'
product = {'product': my_service}
purpose = {'purpose': 'main-table'}

pp = pprint.PrettyPrinter(indent=4, width=200)
client = boto3.client('servicediscovery', config=my_config)
clear()
input("---------- List All Namespaces ----------")
response = client.list_namespaces()
print('Response ---------------------------------------------------')
pp.pprint(response)

input(f'---------- Discover in {my_namespace} service {my_service} ----------')

response = client.discover_instances(
    NamespaceName=my_namespace,
    ServiceName=my_service,
    MaxResults=123,
    QueryParameters=product,
    OptionalParameters=purpose,
    HealthStatus='HEALTHY_OR_ELSE_ALL'
)
print('---------- Response -----------------------------------------------------')
pp.pprint(response)
print('---------- Instance configuration K/V -----------------------------------')
for instance in response['Instances']:
    pp.pprint(instance['Attributes'])

input("Pause...")
