import boto3  # AWS SDK for Python, used to interact with AWS services

# Create an EC2 client to interact with VPC-related APIs
vpc_client = boto3.client('ec2')

# Retrieve metadata for all VPCs in the current AWS account/region
response = vpc_client.describe_vpcs()

# Extract the list of VPC objects from the API response
vpcs = response['Vpcs']

# Loop through each VPC and print its unique identifier
for vpc in vpcs:
    print(vpc['VpcId'])
