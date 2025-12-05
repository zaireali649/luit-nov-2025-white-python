import json
import boto3
from typing import Any, Dict, List


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Lambda function that retrieves and returns all VPC IDs
    for the current AWS account and region.

    Parameters
    ----------
    event : dict
        Input event payload (not used in this function).
    context : LambdaContext
        AWS Lambda context object providing runtime information (not used here).

    Returns
    -------
    dict
        A dictionary containing an HTTP status code and a JSON-encoded list of VPC IDs.
    """

    # Create an EC2 client to interact with VPC-related APIs
    vpc_client = boto3.client("ec2")

    # Call AWS API to get metadata for all VPCs in this region
    response = vpc_client.describe_vpcs()

    # Extract list of VPC objects from the response
    vpcs: List[Dict[str, Any]] = response["Vpcs"]

    # List to store VPC IDs
    vpc_ids: List[str] = []

    # Loop through each VPC and print/collect its unique identifier
    for vpc in vpcs:
        print(vpc["VpcId"])  # Log VPC ID to CloudWatch
        vpc_ids.append(vpc["VpcId"])  # Add VPC ID to output list

    # Return a 200 response including all VPC IDs found
    return {
        "statusCode": 200,
        "body": json.dumps(vpc_ids)
    }
