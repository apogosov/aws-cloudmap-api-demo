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

pp = pprint.PrettyPrinter(indent=4)
client = boto3.client('servicediscovery', config=my_config)
clear()
input("---------- List Namespaces ----------")
response = client.list_namespaces()
pp.pprint(response)

input(f'---------- Discover in {my_namespace} service {my_service} ----------')

response = client.discover_instances(
    NamespaceName=my_namespace,
    ServiceName=my_service,
    MaxResults=123,
    QueryParameters=product,
    OptionalParameters=purpose,
    HealthStatus='HEALTHY' | 'UNHEALTHY' | 'ALL' | 'HEALTHY_OR_ELSE_ALL'
)
pp.pprint(response)

input("Pause...")
