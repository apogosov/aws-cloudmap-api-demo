import pprint
import boto3
from botocore.config import Config
import os


def clear(): os.system('clear')


def print_instances(resp):
    for instance in resp['Instances']:
        pp.pprint(instance['InstanceId'])
        pp.pprint(instance)


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
input("- List All Namespaces")
response = client.list_namespaces()
print('- Full response')
pp.pprint(response)
input()
clear()

query_parameters = {
    'product': my_service,
    'kind': 'dynamodb'
}
optional_parameters = {'purpose': 'main-table'}

input(f'- Discovering in namespace [{my_namespace}] service [{my_service}] with query parameters {query_parameters}')

response = client.discover_instances(
    NamespaceName=my_namespace,
    ServiceName=my_service,
    MaxResults=123,
    QueryParameters=query_parameters,
    # OptionalParameters=optional_parameters,
    HealthStatus='HEALTHY_OR_ELSE_ALL'
)
print_instances(response)

input()
clear()

query_parameters = {
    'product': my_service,
    'kind': 'dynamodb'
}
optional_parameters = {'purpose': 'main-table'}

input(f'- Discovering in namespace [{my_namespace}] service [{my_service}] with query parameters {query_parameters} and optional parameters {optional_parameters}')

response = client.discover_instances(
    NamespaceName=my_namespace,
    ServiceName=my_service,
    MaxResults=123,
    QueryParameters=query_parameters,
    OptionalParameters=optional_parameters,
    HealthStatus='HEALTHY_OR_ELSE_ALL'
)
print_instances(response)

input()
clear()

input("Done...")
