# triggered by zip file getting loaded
# unzips the file, stores temp in s3
# triggers glue crawler previously defined

import json
import boto3

glue_client = boto3.client('glue')

def lambda_handler(event, context):
    # Get details of the S3 event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    
    # Ensure that the file is in the processed-1 folder
    if 'processed-1' in file_key:
        # Trigger the Glue job for transformation
        response = glue_client.start_job_run(JobName='my-glue-job')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Lambda triggered Glue job successfully!')
    }


