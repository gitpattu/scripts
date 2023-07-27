import boto3
import logging # enable logging/debug

from botocore.exceptions import ClientError

# Start a AWS boto3 session
session = boto3.Session
try:
  # get s3 resources from the session
  s3list = session.resource('s3')
  
  # get all the buckets from s3list
  buckets = s3list.Bucket('bucketName')

  # Display list of buckets
  print(buckets)

  #for s3_file in buckets.objects.all():
    #print(s3_file.key)
except ClientError as err:
  print(f"{err}")