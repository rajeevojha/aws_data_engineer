# s3->lambda->glue crawler ->s3 ->lambda ->glue job ->s3 ->lambad -> cleanup
## Revised Workflow Overview:
 - S3 Event Trigger: A zipped file is uploaded to my-bucket/retail/raw/.
 - Lambda for Unzipping: 
   - unzips the file 
   -  moves the unzipped data to my-bucket/retail/unzip/
   - trigger the glue crawler 
   - wait for the started job to finish. No direct way, the wait is in a inflite loop waiting for the status to change to READY.
 - Glue job remoes duplicates (minor task) for now and saves the files to my-bucket/retail/processed. The file is in parquet format. Checked the size of the s3 buckt which is holding the parquet file. Strangely, it is the very close to the zip file we had used/
 - Anothr Lambda gets triggered (TODO)
   - delete the temp zip file
## File intro
  with so many moving parts, lets put as much as possible as memory aid.
 The lambda that gets triggered once the zip file is loaded into the s3 must have the following
 - read from s3, write to s3, get crawler list, trigger a crawller, trigger a glue job. the json file is a good copy  
- jsons/lambda_permission.json
### we did try using a json and clie to directly create the crawler, but ti failed. 
We will be trying again.
the json file is commited though online_retail_crawler.json
