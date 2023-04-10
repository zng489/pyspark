import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col


args = getResolvedOptions(sys.argv, ["JOB_NAME"])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Lendo os dados do Data Catalog
source_df = glueContext.create_dynamic_frame.from_catalog(
    database="orulo_s3", table_name="buildings", transformation_ctx="source_df"
)

# Convertendo DynamicFrame para DataFrame e particionando os dados
source_df = source_df.toDF().repartition(100)

# Realizando tratamentos necessários no DataFrame (exemplo: removendo colunas nulas)
# Trate os dados conforme necessário, por exemplo:
# cleaned_df = source_df.na.drop()

# Convertendo DataFrame para DynamicFrame
cleaned_dynamic_df = DynamicFrame.fromDF(source_df, glueContext, "cleaned_dynamic_df")

# Escrevendo os dados como arquivos Parquet no S3
glueContext.write_dynamic_frame.from_options(
    frame=cleaned_dynamic_df,
    connection_type="s3",
    format="parquet",
    connection_options={
        "path": s3_output_path,
        "partitionKeys": [],
    },
    transformation_ctx="s3://bossa-nova-sss/csv-files/teste_transferencia/",
)

job.commit()