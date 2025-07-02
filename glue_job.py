import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

datasource = glueContext.create_dynamic_frame.from_catalog(
    database = "legacy_db", table_name = "customer_data")
transformed = ApplyMapping.apply(frame = datasource, mappings = [
    ("id", "int", "customer_id", "int"),
    ("name", "string", "full_name", "string")
])
datasink = glueContext.write_dynamic_frame.from_options(
    frame = transformed,
    connection_type = "redshift",
    connection_options = {"dbtable": "customer_table", "database": "target_dw"},
    format = "json"
)
job.commit()
