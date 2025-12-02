import boto3  # AWS SDK for Python, used to interact with AWS services

# Create an S3 client using your configured AWS credentials
s3 = boto3.client('s3')

# Call the S3 API to list all buckets for the authenticated account
response = s3.list_buckets()

# Extract the list of bucket dictionaries from the API response
buckets = response["Buckets"]

# Loop through each bucket and print its name
for bucket in buckets:
    print(bucket["Name"])
