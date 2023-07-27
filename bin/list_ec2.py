import boto3
from botocore.config import Config
from pprint import pprint

# python3 list_ec2.py

my_config = Config(
  region_name = 'ap-southeast-2'
)

session = boto3.Session(profile_name='dev')
ec2client = session.client('ec2', config=my_config)
response = ec2client.describe_instances()

for instance in response.instances.all():
  #response = ec2client.describe_instances(Filters=[{'Name': 'instance-id', 'Values': [instance_id]}])
  print(instance.id , instance.state)