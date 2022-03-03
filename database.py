from boto3 import client, resource
import os

client = client('dynamodb',
                aws_access_key_id=os.environ.get('ACCESS_KEY_ID'),
                aws_secret_access_key=os.environ.get('SECRET_ACCESS_KEY'),
                region_name='us-east-2')
resource = resource('dynamodb',
                    aws_access_key_id=os.environ.get('ACCESS_KEY_ID'),
                    aws_secret_access_key=os.environ.get('SECRET_ACCESS_KEY'),
                    region_name='us-east-2')
