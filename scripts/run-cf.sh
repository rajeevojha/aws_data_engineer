aws cloudformation deploy \
  --template-file glue-crawlers.yaml \
  --stack-name glue-crawlers-stack \
  --capabilities CAPABILITY_NAMED_IAM

