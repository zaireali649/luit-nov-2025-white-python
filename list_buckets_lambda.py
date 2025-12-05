import json
import boto3
from typing import Any, Dict, List


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    AWS Lambda handler that retrieves and returns all S3 bucket names in the account.

    Parameters
    ----------
    event : dict
        The event payload passed into the Lambda function (unused in this example).
    context : LambdaContext
        Runtime information provided by AWS Lambda (unused in this example).

    Returns
    -------
    dict
        A response object containing HTTP status code and a JSON list of bucket names.
    """

    # Create an S3 client using boto3
    s3 = boto3.client("s3")

    # Call AWS to list all S3 buckets accessible by this account/role
    response = s3.list_buckets()

    # List to store bucket names that will be returned
    bucket_names: List[str] = []

    # Extract the "Buckets" list from the response
    buckets = response["Buckets"]

    # Loop through each bucket and collect names
    for bucket in buckets:
        print(bucket["Name"])  # Log bucket name to CloudWatch
        bucket_names.append(bucket["Name"])  # Store the name

    # Return successful HTTP response with bucket names encoded as JSON
    return {
        "statusCode": 200,
        "body": json.dumps(bucket_names)
    }
