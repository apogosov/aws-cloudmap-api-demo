import pprint
import boto3
from botocore.config import Config
import os


def clear(): os.system('clear')


pp = pprint.PrettyPrinter(indent=4, width=200)

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

client = boto3.client('servicediscovery', config=my_config)
clear()
input("---------- List All Namespaces ----------")
response = client.list_namespaces()
print('---------- Response -----------------------------------------------------')
pp.pprint(response)
input()
clear()

query_parameters = {
    'product': my_service,
    'kind': 'dynamodb'
}
optional_parameters = {'purpose': 'main-table'}

input(f'---------- Discover in {my_namespace} service {my_service} with query {query_parameters} ----------')

response = client.discover_instances(
    NamespaceName=my_namespace,
    ServiceName=my_service,
    MaxResults=123,
    QueryParameters=query_parameters,
    # OptionalParameters=optional_parameters,
    HealthStatus='HEALTHY_OR_ELSE_ALL'
)
print('---------- Response -----------------------------------------------------')
pp.pprint(response['Instances'])
print('---------- Instance configuration K/V -----------------------------------')
for instance in response['Instances']:
    pp.pprint(instance['Attributes'])
input()
clear()

input("Done...")
