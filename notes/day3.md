# GLUE - first attempt
 - created a database in glue, 
 - created a crawler and pointed it to the s3 holding all the files. 
   the files were in a single bucket but had two different layout
   glue ended up putting all the records in the same structure and was not able to determine the heading
 - restructured the files into two folder for the layout
 - added two clawers, one each for the varying schema
   this time it worked as expected. One of the files does not have a header, glue gave default header to them
 ** Alternatively ** we could have use a cloud formation template to create the database, and the crawler.

## we used athena to view the data.

## TODO practice cloudformation as well as check on boto to do this
   automate:
   Kicking off crawlers
   Checking if they completed
   Dumping schema to JSON for metadata checks
   Exporting to repo
