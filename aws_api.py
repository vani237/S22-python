import boto3

_ec2 = boto3.client('ec2',region_name='us-east-1')

responce = _ec2.describe_instances()
print(type(responce))
for item in responce['ResponseMetadata']:
    print("*********************************************")
    print(item)
