```python
# libraries installed
#>> pip list
```


```python
#!pip install jupyterthemes
#from jupyterthemes import get_themes
#import jupyterthemes as jt
#from jupyterthemes.stylefx import set_nb_theme
#set_nb_theme('chesterish')
#jt.get_themes()

#from jupyterthemes.stylefx import set_nb_theme
#set_nb_theme('chesterish')
#!pip list
#!jt -t chesterish -f fira -fs 10 -nf ptsans -nfs 11 -N -kl -cursw 2 -cursc r -cellw 95% -T
```

```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```


```python
!pip install pyspark
```

    Collecting pyspark
      Downloading pyspark-3.2.0.tar.gz (281.3 MB)
         |████████████████████████████████| 281.3 MB 51 kB/s              
    [?25h  Preparing metadata (setup.py) ... [?25ldone
    [?25hCollecting py4j==0.10.9.2
      Downloading py4j-0.10.9.2-py2.py3-none-any.whl (198 kB)
         |████████████████████████████████| 198 kB 16.9 MB/s            
    [?25hBuilding wheels for collected packages: pyspark
      Building wheel for pyspark (setup.py) ... [?25ldone
    [?25h  Created wheel for pyspark: filename=pyspark-3.2.0-py2.py3-none-any.whl size=281805912 sha256=61623df64ccf53b3b2ff9f7aeaf1ef05df415f58605f43a78145f42e649eb60c
      Stored in directory: /home/jovyan/.cache/pip/wheels/2f/f8/95/2ad14a4614b4a9f645ee928fbbd057b1b254c67adb494c9a58
    Successfully built pyspark
    Installing collected packages: py4j, pyspark
    Successfully installed py4j-0.10.9.2 pyspark-3.2.0



```python
# Parallelize(x)

from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

- create entry points to spark
try:
    #stop sparkcontext if running
    sc.stop()
except:
    pass
finally:
    #create object of SparkContext
    sc = SparkContext()
    spark = SparkSession(sparkContext=sc)
    
x = [1, 2, 3, 4]

- create an RDD parallelize() is a function in SparkContext and is used to create an RDD from a list collection. 
rdd = sc.parallelize(x)
display(rdd)
```


```python
##################################################################
# SAVING
##################################################################

#>> data lake address
data_lake_address = 'abfss://datalake@cnibigdatadlsgen2.dfs.core.windows.net'

#>> path_of_file
path_of_file = "/uds/uniepro/inteligencia_ocupacional/monitor_de_emprego.csv"

#>> path to load the file
path = '{data_lake}{file}'.format(data_lake = data_lake_address, file = path_of_file)

df.repartition(1).write.mode("overwrite").option('header', True).csv(path)

df.write.format("json").mode("overwrite).save(outputPath/file.json)
                             
#################################################################
#################################################################
```


```python
##################################################################
# LOADING
##################################################################

#>> data lake address
data_lake_address = 'abfss://datalake@cnibigdatadlsgen2.dfs.core.windows.net'

#>> path_of_file
path_of_file = "/uds/uniepro/inteligencia_ocupacional/monitor_de_emprego.csv"

#>> path to load the file
path = '{data_lake}{file}'.format(data_lake = data_lake_address, file = path_of_file)

# df = spark.read.format("csv").option("header","true").load(filePath)

#>> 2 method to read files
df_data = spark.read.csv(path, header=True)
df = spark.read.format("csv").option("header","true").load(path)

df = spark.read.\
.format("csv")\
.option("header","true")\
.option("sep", "delimiter")\
.load(path)

##################################################################
##################################################################
```


```python
#https://github.com/xavier211192/Databricks/blob/main/Spark%20Read_Write%20Cheat%20Sheet.pdf
#https://ichi.pro/pt/spark-essentials-como-ler-e-gravar-dados-com-pyspark-101455223728077
#https://www.geeksforgeeks.org/read-text-file-into-pyspark-dataframe/
# https://medium.com/renato-dantas/temajupyternotebook-f754c065cfe9

# File location and type
# file_location = "/FileStore/tables/empresa_est.csv"
file_location = "/gov/usr_upload/source/dados.csv"
file_type = "csv"

# CSV options
infer_schema = "false"
first_row_is_header = "false"
delimiter = ","

df = spark.read.format(file_type).option("inferSchema", infer_schema) \
  .option("header", first_row_is_header) \
  .option("sep", delimiter) \
  .load(file_location)


# Parquet
df = spark.read.format("parquet).load(parquetDirectory)
df = spark.read.parquet(parquetDirectory)
df = spark.read.json('people.json', schema=final_struc)
                                        
# There are three was to read text files into Pyspark DataFrame (CSV)                
df = spark.read.text()
df = spark.read.csv()
df = spark.read.format().load()
                       
                       
                       
# Read Delta
# Spark SQL
#>> SELECT * FROM delta. "path"

# Spark SQL Unmanaged Table
#>> spark.sql(" DROP TABLE IF EXISTS table_name")
#>> spark.sql(" CREATE TABLE table_name USING DELTA LOCATION '{}'".format(path))

# WRITTING Delta
#>> df.write.format('delta').partitionBy('someColumn').save("path")
```


```python
from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
from pyspark.sql.types import (ArrayType, StructField, StructType, StringType, IntegerType)
# from pyspark.sql.types import StructType,StructField, StringType, IntegerType
from pyspark.sql import SparkSession
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.appName('Name_Spark')\
.config("spark.some.config.option").getOrCreate()

data = [("James","","Smith","36636","M",3000),
         ("Michael","Rose","","40288","M",4000),
         ("Robert","","Williams","42114","M",4000),
         ("Maria","Anne","Jones","39192","F",4000),
         ("Jen","Mary","Brown","","F",-1)]

columns = ["firstname",
           "middlename",
           "lastname",
           "id",
           "gender",
           "salary"]

#schema = StructType([
#StructField("firstname",StringType(),True),
#StructField("middlename",StringType(),True),
#StructField("lastname",StringType(),True),
#StructField("id", StringType(), True),
#StructField("gender", StringType(), True),
#StructField("salary", IntegerType(), True)
#])

display(df)

# df = spark.createDataFrame( my_list, columns)
df = spark.createDataFrame(data,schema = columns)
df.show()
```


    DataFrame[firstname: string, middlename: string, lastname: string, id: string, gender: string, salary: bigint]


    +---------+----------+--------+-----+------+------+
    |firstname|middlename|lastname|   id|gender|salary|
    +---------+----------+--------+-----+------+------+
    |    James|          |   Smith|36636|     M|  3000|
    |  Michael|      Rose|        |40288|     M|  4000|
    |   Robert|          |Williams|42114|     M|  4000|
    |    Maria|      Anne|   Jones|39192|     F|  4000|
    |      Jen|      Mary|   Brown|     |     F|    -1|
    +---------+----------+--------+-----+------+------+
    

rdd = sc.parallelize(data)
type(rdd) # pyspark.rdd.RDD

df = rdd.toDF()
type(df)
pyspark.sql.dataframe.DataFrame

```python
df.columns
```




    ['firstname', 'middlename', 'lastname', 'id', 'gender', 'salary']




```python
df.select("firstname").show()
```

    +---------+
    |firstname|
    +---------+
    |    James|
    |  Michael|
    |   Robert|
    |    Maria|
    |      Jen|
    +---------+
    



```python
df[(df.salary > 2)].show()
```

    +---------+----------+--------+-----+------+------+
    |firstname|middlename|lastname|   id|gender|salary|
    +---------+----------+--------+-----+------+------+
    |    James|          |   Smith|36636|     M|  3000|
    |  Michael|      Rose|        |40288|     M|  4000|
    |   Robert|          |Williams|42114|     M|  4000|
    |    Maria|      Anne|   Jones|39192|     F|  4000|
    +---------+----------+--------+-----+------+------+
    



```python
df.filter(df["salary"] == 3000).collect()
```




    [Row(firstname='James', middlename='', lastname='Smith', id='36636', gender='M', salary=3000)]




```python
result = df.filter(df["salary"] == 3000).collect()
```


```python
row = result[0]
row
```




    Row(firstname='James', middlename='', lastname='Smith', id='36636', gender='M', salary=3000)




```python
result[0].asDict()
```




    {'firstname': 'James',
     'middlename': '',
     'lastname': 'Smith',
     'id': '36636',
     'gender': 'M',
     'salary': 3000}




```python
row.asDict()['firstname']
```




    'James'




```python
and === &
```


```python
df[(df.column_one > 2) & (df.column_two == 3)].show()
```


```python
df.filter("salary <= 3000").show()
```

    +---------+----------+--------+-----+------+------+
    |firstname|middlename|lastname|   id|gender|salary|
    +---------+----------+--------+-----+------+------+
    |    James|          |   Smith|36636|     M|  3000|
    |      Jen|      Mary|   Brown|     |     F|    -1|
    +---------+----------+--------+-----+------+------+
    



```python
df.filter(~(df["salary"] <= 3000)).show()
```

    +---------+----------+--------+-----+------+------+
    |firstname|middlename|lastname|   id|gender|salary|
    +---------+----------+--------+-----+------+------+
    |  Michael|      Rose|        |40288|     M|  4000|
    |   Robert|          |Williams|42114|     M|  4000|
    |    Maria|      Anne|   Jones|39192|     F|  4000|
    +---------+----------+--------+-----+------+------+
    



```python
df.filter("salary <= 3000").select(['id', 'gender']).show()
```

    +-----+------+
    |   id|gender|
    +-----+------+
    |36636|     M|
    |     |     F|
    +-----+------+
    



```python
df_pyspark.filter( (df_pyspark['age'] < 30) & ~(df_pyspark['Experience'] > 30000) ).show()
```


```python
df.groupBy('firstname').sum().show()
```

    +---------+-----------+
    |firstname|sum(salary)|
    +---------+-----------+
    |    James|       3000|
    |  Michael|       4000|
    |   Robert|       4000|
    |      Jen|         -1|
    |    Maria|       4000|
    +---------+-----------+
    



```python
df.toPandas()

df.show()

df.toDF()

df.printSchema()

df.describe()

df.select(*expression).show()

df.show()

df.head()

df.tail()

df.columns

df.select('column_name')
df.select(['column_name_1','column_name_2'])

df.describe()

df.types() # (['Name', 'string']) 

df.drop("column_name")

df.withColumnRenamed('id', 'ID_NUMBER')

df_drop = df.drop(*['url', 'codigo', 'salario'])

## Filling the missing value ### 
df.na.fill('Missing Value').show()

df.na.fill(value=3,subset=['Experience']).show()

df.fillna('Missing Value').show()

df.fillna('Missing Value',subset=['age']).show()

df.na.fill({'age':'Missing'}).show()

df.na.fill('Missing Value').show()

df.na.fill('Missing Value','Experience').show()

expression = [func.lower(func.col(x).alias(x) for x in df.columns] 
```


```python
spark = SparkSession.builder.appName('Name_Spark').getOrCreate()

df = spark.read.csv (-File.csv-)

expression = [func.lower(func.col(x).alias(x) for x in df.columns]
```


```python
##### SQL #####

df.createOrReplaceTempView('Name')

results = spark.sql("SELECT * FROM people")

results = spark.sql("select * from people WHEre age=30")

results.show()

x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x===

###### spark_dataframe to dataframe #####

df = spark.createDataFrame(data)
df
type(df)
pyspark.sql.dataframe.DataFrame

x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x===

Python Dictionary get() Method
dictionary.get(keyname, value)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("brand","NEW_BRAND")
print(x)
Ford

x = car.get("price","NEW_BRAND")
print(x)
NEW_BRAND
```
