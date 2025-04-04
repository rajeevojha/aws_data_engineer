# added files in s3
## used aws cli for the task
 - mkdir -p s3_datalake/raw
 - cd s3_datalake/raw/
 - echo "Sample folder structure for raw data stored in S3 used in this project" >> README.md
 - cd ~/aws_data_engineer/
 - cd s3_datalake/raw/
 - ls
 - vi sample_orders.csv
 - aws s3 mb s3://ro-aws-de-30
 - aws s3 cp --recursive . s3://ro-aws-de-30/raw < copy the content of current folder to s3, keep folder structure
 - aws s3 ls --recursive
 - aws s3 ls ro-aws-de-30 --recursive < get content of the folder
 - aws s3 rb s3://ro-aws-de-30/raw/README.md < rb is for removing bucket and not file
 - aws s3 rm s3://ro-aws-de-30/raw/README.md < rm to remove file
