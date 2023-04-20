# pyspark

https://github.com/martinkarlssonio/big-data-solution

Mkt_Mktleads.write.option("header",True).option("compression", "snappy").mode("overwrite").parquet("s3://bossa-nova-trusted/Pessoas/Mkt_Mktleads")

boto3 1.26.116 requires botocore<1.30.0

&

Bitwise AND

^

Bitwise XOR

|

Bitwise OR
https://docs.python.org/3/reference/expressions.html#operator-precedence



Estou fazendo assim:

input_paths = [ "s3://bossa-nova-trusted/db-cidadevirtual/prd_cidade_virtual/address",
                "s3://bossa-nova-trusted/db-cidadevirtual/prd_cidade_virtual/userAction",
                "s3://bossa-nova-trusted/db-orulos/buildings",
                "s3://bossa-nova-trusted/db-sigavi-full/Endereco",
                "s3://bossa-nova-trusted/db-site/bnsir_avm",
                "s3://bossa-nova-trusted/db-site/bnsir_avm_site",
                "s3://bossa-nova-trusted/iptu_consolidada"]

dataframes = []
for path in input_paths:
    df = spark.read.parquet(path)
    dataframes.append(df)

df = dataframes[1].filter(col("sequentialId").isNotNull() & col("result").isNotNull())

schema = StructType([StructField("Properties", StructType([StructField("Addresses", ArrayType(StringType()))]))])

df = df.withColumn("result_json", from_json(col("result"), schema))

df = df.select(col("result_json.Properties.Addresses").alias("addresses")).withColumn("address", explode(col("addresses")))
