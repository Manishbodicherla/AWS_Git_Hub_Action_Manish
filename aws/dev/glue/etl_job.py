import sys
import boto3
from awsglue.utils import getResolvedOptions

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
glueContext = GlueContext(SparkContext())

# Your ETL job logic here
print("Running Glue ETL job...")
