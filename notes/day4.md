# Day 4
## first gule job
  - used gluestudio to create a job
  - first section is Visual which gives options to select source, transformation, target << interesting >>
  - under the hood the studio is generating a python + spark script
  - used this job to place the output in another s3 bucket. Had specified the output type as Parquet. /processed
  - observed the job had created multiple smaller files.
## SQL Notes
**Note** avoid using - (hyphen) in database. Athena does not like it.
  - used Athena studio to execute the below commands.
 
_creates database_
``` 
 CREATE database abcd; => 
 ```
_the next one is creating a table in abcd database by using the parquet file stored in the s3 bucket. Quite simple._
```
CREATE EXTERNAL TABLE IF NOT EXISTS abcd.processed_employee_dtl (
  first_name STRING,
  last_name STRING,
  email STRING,
  date_of_birth STRING
)
STORED AS PARQUET
LOCATION 's3://{your bucket}/processed/';
```
> Note: ` the above command just consumed all the smaller files present in the folder and created the table. No other step was required.`

Finally a select statment to complete the puzzle.
```
SELECT * FROM abcd.processed_employee_dtl;
```
## `TODO` study more about 
- Parquet
- spark
- QuickSight
