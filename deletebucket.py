# Use the boto3 library to communicate with AWS
import boto3

# Buckets you want to delete, specified by their names
BUCKETS = [
    "aws-cloudtrail-logs-698668199773-884589f2",
    "aws-cloudtrail-logs-698668199773-8ff12b52",
    "aws-cloudtrail-logs-698668199773-d9a9e547",
    "aws-cloudtrail-logs-698668199773-a1c893da",
    ]

s3 = boto3.resource("s3")
for bucket_name in BUCKETS:
    # For each bucket, create a resource object with boto3
    bucket = s3.Bucket(bucket_name)
    # Delete all of the objects in the bucket
    bucket.object_versions.delete()

    # Delete the bucket itself!
    bucket.delete()