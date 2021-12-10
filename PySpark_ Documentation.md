```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@


```python
# https://medium.com/renato-dantas/temajupyternotebook-f754c065cfe9
!pip install jupyterthemes
from jupyterthemes import get_themes
import jupyterthemes as jt
from jupyterthemes.stylefx import set_nb_theme
set_nb_theme('chesterish')
#jt.get_themes()

#from jupyterthemes.stylefx import set_nb_theme
#set_nb_theme('chesterish')
#!pip list
#!jt -t chesterish -f fira -fs 10 -nf ptsans -nfs 11 -N -kl -cursw 2 -cursc r -cellw 95% -T

```

```

-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><

SparkSession: SparkSession is a combination of all these differents contexts.

spark = SparkSession \
    .builder \
    .appName('Python Spark create RDD example') \
    .config('spark.some.config.option', 'some-value') \
    .getOrCreate()

spark = SparkSession.builder.appName('Python Spark create RDD example').config('spark.some.config.option', 'some-value').getOrCreate()

-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><

df = spark.sparkContext.parallelize([(1,2,3, 'a b c'),
                                    (4,5,6, 'd e f'),
                                    (7,8,9, 'g h i')])

Why we use parallelize in Spark?
parallelize() method is the SparkContext's parallelize method to create a parallelized collection. This allows Spark to distribute the data across multiple nodes, instead of depending on a single node to process the data: Now that we have created ... Get PySpark Cookbook now with O'Reilly online learning.

-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><

# SparkSession: SparkSession is a combination of all these differents contexts.

# conf = SparkConf().setMaster("local").setAppName("My App")
# sc = SparkContext(conf = conf)
# lines = sc.textFile('README.md')
# lines
# pythonLines = lines.filter(lambda line: "Python" in line)
# pythonLines

-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><

```


```
try:
  run this code 
except:
  Execute this code when there is an exception
else:
  No exception? Run this code.
finally:
  Always run this code.
```


# - Parallelize(x) 
```diff
- from pyspark import SparkContext, SparkConf
- from pyspark.sql import SparkSession

# create entry points to spark
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
#create an RDD parallelize() is a function in SparkContext and is used to create an RDD from a list collection. 

rdd = sc.parallelize(x)
display(rdd)
```
                    ###### Parallelize another example #####
import numpy as np
rdd1 = sc.parallelize(np.arange(0, 30, 2))
```



```
from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
spark = SparkSession.builder.appName('Name_Spark').getOrCreate()

-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><

                    ##### createDataFrame method #####

df = spark.createDataFrame()
- We got total control over the schema customization

from pyspark.sql.types import StructType,StructField, StringType, IntegerType

data2 = [("James","","Smith","36636","M",3000),
    ("Michael","Rose","","40288","M",4000),
    ("Robert","","Williams","42114","M",4000),
    ("Maria","Anne","Jones","39192","F",4000),
    ("Jen","Mary","Brown","","F",-1)
  ]

schema = StructType([ \
    StructField("firstname",StringType(),True), \
    StructField("middlename",StringType(),True), \
    StructField("lastname",StringType(),True), \
    StructField("id", StringType(), True), \
    StructField("gender", StringType(), True), \
    StructField("salary", IntegerType(), True) \
  ])
 
df = spark.createDataFrame(data=data2,schema=schema)
df.printSchema()
df.show(truncate=False)

-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><

                    ###### parallerize #####
                    
- We do not have the total control over/about schema

columns = ["language","users_count"]
data = [("Java", "20000"), ("Python", "100000"), ("Scala", "3000")]

df_rdd = spark.sparkContext.parallelize(data)
- If you to print you gonna to receive "RDD STRUCTURE"

df = spark.createDataFrame(df_rdd).toDF(*columns)

OR

df = spark.sparkContext.parallelize(data).toDF(*columns)

-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><

```

```
        
            ##### Function #####

- df.toPandas()
- df.show()
- df.toDF()

```


```python
# appl_stock.csv 
# people.json

from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
spark = SparkSession.builder.appName('Name_Spark').getOrCreate()

df = spark.read.json('people.json')
df.show()
```

    +----+-------+------+
    | age|   name|weight|
    +----+-------+------+
    |null|Michael|    80|
    |  30|   Andy|    86|
    |  19| Justin|    67|
    |null|    jun|    99|
    |  22|  Carls|    77|
    |  31| Jordan|    83|
    +----+-------+------+
    


```

-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><

new_names = [new_columns.get(col,col) for col in df.columns]
df.toDF(*new_names).show(4)

new_columns = {'age':'AGE', 'name':'NAME'}
new_names = [new_columns.get(col,col) for col in df.columns]
df.toDF(*new_names).show(4)

+----+-------+------+
| AGE|   NAME|weight|
+----+-------+------+
|null|Michael|    80|
|  30|   Andy|    86|
|  19| Justin|    67|
|null|    jun|    99|
+----+-------+------+
only showing top 4 row



-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><-----><

```


```python
new_columns = {'age':'AGE', 'name':'NAME'}
```


```python
new_columns = {'age':'AGE', 'name':'NAME'}
new_names = [new_columns.get(col,col) for col in df.columns]
df.toDF(*new_names).show(4)
```

    +----+-------+------+
    | AGE|   NAME|weight|
    +----+-------+------+
    |null|Michael|    80|
    |  30|   Andy|    86|
    |  19| Justin|    67|
    |null|    jun|    99|
    +----+-------+------+
    only showing top 4 rows
    



```python
new_columns = {'age':'AGE', 'name':'NAME'}

list = []
for col in df.columns:
    list.append(new_columns.get(col,col))

df.toDF(*list).show(4)
```

    +----+-------+------+
    | AGE|   NAME|weight|
    +----+-------+------+
    |null|Michael|    80|
    |  30|   Andy|    86|
    |  19| Justin|    67|
    |null|    jun|    99|
    +----+-------+------+
    only showing top 4 rows
    



```python
new_columns = {'age':'AGE', 'name':'NAME'}

list = []
for col in df.columns:
    list.append(new_columns.get(col,col))

list
```




    ['AGE', 'NAME', 'weight']




```python

```


```python
df.collect()
```




    [Row(col1=1, col2=2, col3=3, col4='a b c'),
     Row(col1=4, col2=5, col3=6, col4='d e f'),
     Row(col1=7, col2=8, col3=9, col4='g h i')]




```python
#SQLContext.getConf(spark.driver.maxResultSize)
```

<ul>
  <li><b> df.printSchema() </b></li>
      <dd></dd>
          <p>
        
  <li><b> df.describe()  </b></li>
      <dd></dd>
          <p>      
        
  <li><b>df.select(*expression(.show()</b></li>
      <dd></dd>
          <p>
              
  <li><b>df.show(), df.head(), df,tail()</b></li>
      <dd></dd>
          <p>
              
  <li><b>df.columns #['Name', 'Age]</b></li>
      <dd></dd>
          <p>
              
  <li><b> df.select('column_name') </b></li>
      <dd></dd>
          <p>
              
  <li><b> df.select(['column_name',]) </b></li>
      <dd></dd>
          <p>
              
  <li><b> df.select['column_name'] </b></li>
  <dd> - ['Name', 'Age ]</dd>
      <p>      
          
  <li><b> df.describe() </b></li>
          <dd> </dd>
    <p>
        
  <li><b> df.types() </b></li>
          <dd> - (['Name', 'string'])</dd>
    <p>
        
  <li><b> spark = SparkSession.builder.appName('Name_Spark').getOrCreate() </b></li>
      <dd></dd>
          <p>      
        
  <li><b> df = spark.read.csv (-File.csv-) </b></li>
      <dd></dd>
          <p>  
              
  <li><b> expression = [func.lower(func.col(x).alias(x) for x in df.columns] </b></li>
      <dd></dd>
          <p> 

</ul>
 

<dl>
   <dt><b> </b></dt>
   <dd> </dd>
   <p>
   <dt><b> </b></dt>
   <dd> </dd>
   <p>
   <dt><b> </b></dt>
   <dd> </dd>
   <p>
   <dt><b> </b></dt>
   <dd>  </dd>
   <dd> </dd>
   <p>
   <dt><b> </b></dt>
   <dd> </dd>
</dl>


```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Name_Spark').getOrCreate()

df = spark.read.csv('test1.csv') #  header=True, inferSchema = True)

df.show()
type(df)
```

    +---------+---+----------+------+
    |      _c0|_c1|       _c2|   _c3|
    +---------+---+----------+------+
    |     Name|age|Experience|Salary|
    |    Krish| 31|        10| 30000|
    |Sudhanshu| 30|         8| 25000|
    |    Sunny| 29|         4| 20000|
    |     Paul| 24|         3| 20000|
    |   Harsha| 21|         1| 15000|
    |  Shubham| 23|         2| 18000|
    +---------+---+----------+------+
    





    pyspark.sql.dataframe.DataFrame




```python

```


```python

```


```python

```


```python

```


```python
my_list = [['a', 1, None], ['b', 2, 3],['c', 3, 4]]
#dp = pd.DataFrame(my_list,columns=['A', 'B', 'C']) <----- to Pandas
ds = spark.createDataFrame(my_list, ['A', 'B', 'C'])
ds
```




    DataFrame[A: string, B: bigint, C: bigint]




```python
ds.toPandas()
```

                                                                                    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>2</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>3</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>



# Importing and creating spark data frame


```python
df = spark.sparkContext.parallelize([(1, 2, 3, 'a b c'),
(4, 5, 6, 'd e f'),
(7, 8, 9, 'g h i')]).toDF(['col1', 'col2', 'col3','col4'])

```


```python
my_list = [['a', 1, None], ['b', 2, 3],['c', 3, 4]]
#dp = pd.DataFrame(my_list,columns=['A', 'B', 'C']) <----- to Pandas
ds = spark.createDataFrame(my_list, ['A', 'B', 'C'])
ds.show()

# or

ds_v0 = spark.createDataFrame([(1, 2, 3, 'a b c'),
                             (4, 5, 6, 'd e f'),
                             (7, 8, 9, 'g h i')],['col1', 'col2', 'col3','col4'])

ds_v0.show()                        
```

    +---+---+----+
    |  A|  B|   C|
    +---+---+----+
    |  a|  1|null|
    |  b|  2|   3|
    |  c|  3|   4|
    +---+---+----+
    
    +----+----+----+-----+
    |col1|col2|col3| col4|
    +----+----+----+-----+
    |   1|   2|   3|a b c|
    |   4|   5|   6|d e f|
    |   7|   8|   9|g h i|
    +----+----+----+-----+
    



```python
# df = spark.read.csv('infojobs_dataset.csv', sep ='<anything>'header = True, inferSchema = True)
df = spark.read.csv('dataset_infojobs.csv',header=True)
df = df.drop('_c0')
display(df)
df.toPandas()
```


    DataFrame[id: string, site: string, url: string, codigo: string, profissao: string, salario: string, localidade: string, conteudo: string, empresa: string, data do scraping: string, 1_dif_data: string]





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>site</th>
      <th>url</th>
      <th>codigo</th>
      <th>profissao</th>
      <th>salario</th>
      <th>localidade</th>
      <th>conteudo</th>
      <th>empresa</th>
      <th>data do scraping</th>
      <th>1_dif_data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendente-...</td>
      <td>7207593</td>
      <td>Atendente De Vendas</td>
      <td>1.500,00 a  1.800,00</td>
      <td>Sao Paulo, SP</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>CESARMAQ</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207597</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Fortaleza, CE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendiment...</td>
      <td>7206929</td>
      <td>Atendimento - Bh</td>
      <td>1.135,00</td>
      <td>Belo Horizonte, MG</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>VALLOR BENEFICIOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207595</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Recife, PE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-consultor-...</td>
      <td>7206056</td>
      <td>Consultor De Vendas</td>
      <td>1.000,00 a  3.000,00</td>
      <td>Caruaru, PE</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>Dragorayeb Incorporadora</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207596</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Curitiba, PR</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-instrutor-...</td>
      <td>7207541</td>
      <td>Instrutor(A) De Solda</td>
      <td>A combinar</td>
      <td>Curitiba, PR</td>
      <td>Area e especializacao profissional: Educacao, ...</td>
      <td>CEBRAC CURITIBA</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207599</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Guarulhos, SP</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-auxiliar-m...</td>
      <td>7207543</td>
      <td>Auxiliar De Manutencao - Campinas</td>
      <td>1.500,00 a  1.600,00</td>
      <td>Campinas, SP</td>
      <td>Area e especializacao profissional: Construcao...</td>
      <td>HM CONSULTORIA E RECURSOS HUMANOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207600</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Brasilia, DF</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
  </tbody>
</table>
</div>



# columns( ), .describe( ), .select( )


```python
df = spark.read.csv('dataset_infojobs.csv',header=True)
df = df.drop('_c0')
display(df)
display(df.toPandas())

df.describe().toPandas()
```


    DataFrame[id: string, site: string, url: string, codigo: string, profissao: string, salario: string, localidade: string, conteudo: string, empresa: string, data do scraping: string, 1_dif_data: string]



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>site</th>
      <th>url</th>
      <th>codigo</th>
      <th>profissao</th>
      <th>salario</th>
      <th>localidade</th>
      <th>conteudo</th>
      <th>empresa</th>
      <th>data do scraping</th>
      <th>1_dif_data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendente-...</td>
      <td>7207593</td>
      <td>Atendente De Vendas</td>
      <td>1.500,00 a  1.800,00</td>
      <td>Sao Paulo, SP</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>CESARMAQ</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207597</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Fortaleza, CE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendiment...</td>
      <td>7206929</td>
      <td>Atendimento - Bh</td>
      <td>1.135,00</td>
      <td>Belo Horizonte, MG</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>VALLOR BENEFICIOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207595</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Recife, PE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-consultor-...</td>
      <td>7206056</td>
      <td>Consultor De Vendas</td>
      <td>1.000,00 a  3.000,00</td>
      <td>Caruaru, PE</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>Dragorayeb Incorporadora</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207596</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Curitiba, PR</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-instrutor-...</td>
      <td>7207541</td>
      <td>Instrutor(A) De Solda</td>
      <td>A combinar</td>
      <td>Curitiba, PR</td>
      <td>Area e especializacao profissional: Educacao, ...</td>
      <td>CEBRAC CURITIBA</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207599</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Guarulhos, SP</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-auxiliar-m...</td>
      <td>7207543</td>
      <td>Auxiliar De Manutencao - Campinas</td>
      <td>1.500,00 a  1.600,00</td>
      <td>Campinas, SP</td>
      <td>Area e especializacao profissional: Construcao...</td>
      <td>HM CONSULTORIA E RECURSOS HUMANOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207600</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Brasilia, DF</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
  </tbody>
</table>
</div>





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>summary</th>
      <th>id</th>
      <th>site</th>
      <th>url</th>
      <th>codigo</th>
      <th>profissao</th>
      <th>salario</th>
      <th>localidade</th>
      <th>conteudo</th>
      <th>empresa</th>
      <th>data do scraping</th>
      <th>1_dif_data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>count</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>mean</td>
      <td>5.5</td>
      <td>None</td>
      <td>None</td>
      <td>7207364.9</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>stddev</td>
      <td>3.0276503540974917</td>
      <td>None</td>
      <td>None</td>
      <td>504.23615499083047</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>min</td>
      <td>1</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendente-...</td>
      <td>7206056</td>
      <td>Atendente De Vendas</td>
      <td>1.000,00 a  3.000,00</td>
      <td>Belo Horizonte, MG</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>4</th>
      <td>max</td>
      <td>9</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207600</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Sao Paulo, SP</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>VALLOR BENEFICIOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.columns
```




    ['id',
     'site',
     'url',
     'codigo',
     'profissao',
     'salario',
     'localidade',
     'conteudo',
     'empresa',
     'data do scraping',
     '1_dif_data']



# drop( ), df.withColumnRenamed('_c0','sno')


```python
df = spark.read.csv('dataset_infojobs.csv',header=True)
df = df.drop('_c0')
display(df)
display(df.toPandas())

print('multi drop columns')
""" The * needs to come outside of the brackets if there are multiple columns to drop """

df_drop = df.drop(*['url', 'codigo', 'salario'])
df_drop.toPandas()
display(df_drop.toPandas())


print('Renaming')

df_renamed = df.withColumnRenamed('id', 'ID_NUMBER')
display(df_renamed.toPandas().head(3))
```


    DataFrame[id: string, site: string, url: string, codigo: string, profissao: string, salario: string, localidade: string, conteudo: string, empresa: string, data do scraping: string, 1_dif_data: string]



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>site</th>
      <th>url</th>
      <th>codigo</th>
      <th>profissao</th>
      <th>salario</th>
      <th>localidade</th>
      <th>conteudo</th>
      <th>empresa</th>
      <th>data do scraping</th>
      <th>1_dif_data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendente-...</td>
      <td>7207593</td>
      <td>Atendente De Vendas</td>
      <td>1.500,00 a  1.800,00</td>
      <td>Sao Paulo, SP</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>CESARMAQ</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207597</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Fortaleza, CE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendiment...</td>
      <td>7206929</td>
      <td>Atendimento - Bh</td>
      <td>1.135,00</td>
      <td>Belo Horizonte, MG</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>VALLOR BENEFICIOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207595</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Recife, PE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-consultor-...</td>
      <td>7206056</td>
      <td>Consultor De Vendas</td>
      <td>1.000,00 a  3.000,00</td>
      <td>Caruaru, PE</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>Dragorayeb Incorporadora</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207596</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Curitiba, PR</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-instrutor-...</td>
      <td>7207541</td>
      <td>Instrutor(A) De Solda</td>
      <td>A combinar</td>
      <td>Curitiba, PR</td>
      <td>Area e especializacao profissional: Educacao, ...</td>
      <td>CEBRAC CURITIBA</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207599</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Guarulhos, SP</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-auxiliar-m...</td>
      <td>7207543</td>
      <td>Auxiliar De Manutencao - Campinas</td>
      <td>1.500,00 a  1.600,00</td>
      <td>Campinas, SP</td>
      <td>Area e especializacao profissional: Construcao...</td>
      <td>HM CONSULTORIA E RECURSOS HUMANOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207600</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Brasilia, DF</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
  </tbody>
</table>
</div>


    multi drop columns



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>site</th>
      <th>profissao</th>
      <th>localidade</th>
      <th>conteudo</th>
      <th>empresa</th>
      <th>data do scraping</th>
      <th>1_dif_data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>infojobs</td>
      <td>Atendente De Vendas</td>
      <td>Sao Paulo, SP</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>CESARMAQ</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>infojobs</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>Fortaleza, CE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>infojobs</td>
      <td>Atendimento - Bh</td>
      <td>Belo Horizonte, MG</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>VALLOR BENEFICIOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>infojobs</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>Recife, PE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>infojobs</td>
      <td>Consultor De Vendas</td>
      <td>Caruaru, PE</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>Dragorayeb Incorporadora</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>infojobs</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>Curitiba, PR</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>infojobs</td>
      <td>Instrutor(A) De Solda</td>
      <td>Curitiba, PR</td>
      <td>Area e especializacao profissional: Educacao, ...</td>
      <td>CEBRAC CURITIBA</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>infojobs</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>Guarulhos, SP</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>infojobs</td>
      <td>Auxiliar De Manutencao - Campinas</td>
      <td>Campinas, SP</td>
      <td>Area e especializacao profissional: Construcao...</td>
      <td>HM CONSULTORIA E RECURSOS HUMANOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>infojobs</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>Brasilia, DF</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
  </tbody>
</table>
</div>


    Renaming



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID_NUMBER</th>
      <th>site</th>
      <th>url</th>
      <th>codigo</th>
      <th>profissao</th>
      <th>salario</th>
      <th>localidade</th>
      <th>conteudo</th>
      <th>empresa</th>
      <th>data do scraping</th>
      <th>1_dif_data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendente-...</td>
      <td>7207593</td>
      <td>Atendente De Vendas</td>
      <td>1.500,00 a  1.800,00</td>
      <td>Sao Paulo, SP</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>CESARMAQ</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207597</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Fortaleza, CE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendiment...</td>
      <td>7206929</td>
      <td>Atendimento - Bh</td>
      <td>1.135,00</td>
      <td>Belo Horizonte, MG</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>VALLOR BENEFICIOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
  </tbody>
</table>
</div>


# adding columns: .lit(values), .otherwise(), when(), &


```python
df = spark.read.csv('dataset_infojobs.csv',header=True)
df = df.drop('_c0')
display(df)
df.toPandas().head(3)


from pyspark.sql.functions import when,col,lit


df_with_column_lit = df.withColumn('lit_column', lit(1000)) 
display(df_with_column_lit.toPandas().head(3))


df_alias = df.withColumn('alias_column', lit('alias_values'))
df_alias.toPandas().head(3)

#df_v1.withColumn('new_column_Age',df_v1['age']*2)
# df3 = df.select(col("EmpId"),col("Salary"),lit("1").alias("lit_value1"))
# df3 = df.select(col("EmpId"),col("Salary"),lit("1").alias("lit_value1"))
# df3 = df2.withColumn("lit_value2", when(col("Salary") >=40000 & col("Salary") <= 50000,lit("100")).otherwise(lit("200")))
```


    DataFrame[id: string, site: string, url: string, codigo: string, profissao: string, salario: string, localidade: string, conteudo: string, empresa: string, data do scraping: string, 1_dif_data: string]



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>site</th>
      <th>url</th>
      <th>codigo</th>
      <th>profissao</th>
      <th>salario</th>
      <th>localidade</th>
      <th>conteudo</th>
      <th>empresa</th>
      <th>data do scraping</th>
      <th>1_dif_data</th>
      <th>lit_column</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendente-...</td>
      <td>7207593</td>
      <td>Atendente De Vendas</td>
      <td>1.500,00 a  1.800,00</td>
      <td>Sao Paulo, SP</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>CESARMAQ</td>
      <td>2021-04-29</td>
      <td>21 days</td>
      <td>1000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207597</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Fortaleza, CE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
      <td>1000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendiment...</td>
      <td>7206929</td>
      <td>Atendimento - Bh</td>
      <td>1.135,00</td>
      <td>Belo Horizonte, MG</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>VALLOR BENEFICIOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
      <td>1000</td>
    </tr>
  </tbody>
</table>
</div>





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>site</th>
      <th>url</th>
      <th>codigo</th>
      <th>profissao</th>
      <th>salario</th>
      <th>localidade</th>
      <th>conteudo</th>
      <th>empresa</th>
      <th>data do scraping</th>
      <th>1_dif_data</th>
      <th>alias_column</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendente-...</td>
      <td>7207593</td>
      <td>Atendente De Vendas</td>
      <td>1.500,00 a  1.800,00</td>
      <td>Sao Paulo, SP</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>CESARMAQ</td>
      <td>2021-04-29</td>
      <td>21 days</td>
      <td>alias_values</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207597</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Fortaleza, CE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
      <td>alias_values</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendiment...</td>
      <td>7206929</td>
      <td>Atendimento - Bh</td>
      <td>1.135,00</td>
      <td>Belo Horizonte, MG</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>VALLOR BENEFICIOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
      <td>alias_values</td>
    </tr>
  </tbody>
</table>
</div>



# types values, casting column type, type(), .dtypes
### https://sparkbyexamples.com/pyspark/pyspark-cast-column-type/


```python
df = spark.read.csv('dataset_infojobs.csv',header=True)
df = df.drop('_c0')
display(df)
df.printSchema()
df.toPandas().head(3)

display(type(df))

display(df.dtypes)

from pyspark.sql.types import IntegerType,BooleanType,DateType

#########################################################################################

df_cast = df.withColumn("codigo", df.codigo.cast(IntegerType()))
display(df_cast)
df_cast.printSchema()

#########################################################################################

df_sql = df.createOrReplaceTempView('Cast_SQL')
df_sql =  spark.sql("SELECT STRING(profissao), INT(codigo), INT(salario) from Cast_SQL")
df_sql.printSchema()

#########################################################################################

# Convert String to Integer Type
#df.withColumn("age",df.age.cast(IntegerType()))
#df.withColumn("age",df.age.cast('int'))
#df.withColumn("age",df.age.cast('integer'))

# Using select
#df.select(col("age").cast('int').alias("age"))

#Using selectExpr()
#df.selectExpr("cast(age as int) age")

#Using with spark.sql()
#spark.sql("SELECT INT(age),BOOLEAN(isGraduated),DATE(jobStartDate) from CastExample")
```


    DataFrame[id: string, site: string, url: string, codigo: string, profissao: string, salario: string, localidade: string, conteudo: string, empresa: string, data do scraping: string, 1_dif_data: string]


    root
     |-- id: string (nullable = true)
     |-- site: string (nullable = true)
     |-- url: string (nullable = true)
     |-- codigo: string (nullable = true)
     |-- profissao: string (nullable = true)
     |-- salario: string (nullable = true)
     |-- localidade: string (nullable = true)
     |-- conteudo: string (nullable = true)
     |-- empresa: string (nullable = true)
     |-- data do scraping: string (nullable = true)
     |-- 1_dif_data: string (nullable = true)
    



    pyspark.sql.dataframe.DataFrame



    [('id', 'string'),
     ('site', 'string'),
     ('url', 'string'),
     ('codigo', 'string'),
     ('profissao', 'string'),
     ('salario', 'string'),
     ('localidade', 'string'),
     ('conteudo', 'string'),
     ('empresa', 'string'),
     ('data do scraping', 'string'),
     ('1_dif_data', 'string')]



    DataFrame[id: string, site: string, url: string, codigo: int, profissao: string, salario: string, localidade: string, conteudo: string, empresa: string, data do scraping: string, 1_dif_data: string]


    root
     |-- id: string (nullable = true)
     |-- site: string (nullable = true)
     |-- url: string (nullable = true)
     |-- codigo: integer (nullable = true)
     |-- profissao: string (nullable = true)
     |-- salario: string (nullable = true)
     |-- localidade: string (nullable = true)
     |-- conteudo: string (nullable = true)
     |-- empresa: string (nullable = true)
     |-- data do scraping: string (nullable = true)
     |-- 1_dif_data: string (nullable = true)
    
    root
     |-- profissao: string (nullable = true)
     |-- codigo: integer (nullable = true)
     |-- salario: integer (nullable = true)
    


# conditions, .union( ) SQL


```python
df = spark.read.csv('dataset_infojobs.csv',header=True)
df = df.drop('_c0')
display(df)
df.printSchema()
df.toPandas().head(3)
```


    DataFrame[id: string, site: string, url: string, codigo: string, profissao: string, salario: string, localidade: string, conteudo: string, empresa: string, data do scraping: string, 1_dif_data: string]


    root
     |-- id: string (nullable = true)
     |-- site: string (nullable = true)
     |-- url: string (nullable = true)
     |-- codigo: string (nullable = true)
     |-- profissao: string (nullable = true)
     |-- salario: string (nullable = true)
     |-- localidade: string (nullable = true)
     |-- conteudo: string (nullable = true)
     |-- empresa: string (nullable = true)
     |-- data do scraping: string (nullable = true)
     |-- 1_dif_data: string (nullable = true)
    





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>site</th>
      <th>url</th>
      <th>codigo</th>
      <th>profissao</th>
      <th>salario</th>
      <th>localidade</th>
      <th>conteudo</th>
      <th>empresa</th>
      <th>data do scraping</th>
      <th>1_dif_data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendente-...</td>
      <td>7207593</td>
      <td>Atendente De Vendas</td>
      <td>1.500,00 a  1.800,00</td>
      <td>Sao Paulo, SP</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>CESARMAQ</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207597</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Fortaleza, CE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendiment...</td>
      <td>7206929</td>
      <td>Atendimento - Bh</td>
      <td>1.135,00</td>
      <td>Belo Horizonte, MG</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>VALLOR BENEFICIOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
  </tbody>
</table>
</div>




```python
# SQl
df.createOrReplaceTempView('name_created')

results = spark.sql('SELECT * FROM name_created')
results.toPandas().head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>site</th>
      <th>url</th>
      <th>codigo</th>
      <th>profissao</th>
      <th>salario</th>
      <th>localidade</th>
      <th>conteudo</th>
      <th>empresa</th>
      <th>data do scraping</th>
      <th>1_dif_data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendente-...</td>
      <td>7207593</td>
      <td>Atendente De Vendas</td>
      <td>1.500,00 a  1.800,00</td>
      <td>Sao Paulo, SP</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>CESARMAQ</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207597</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Fortaleza, CE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendiment...</td>
      <td>7206929</td>
      <td>Atendimento - Bh</td>
      <td>1.135,00</td>
      <td>Belo Horizonte, MG</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>VALLOR BENEFICIOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.createOrReplaceTempView('name_created')

results_sql = spark.sql('select * from name_created where codigo < 7207593')
results_sql.toPandas()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>site</th>
      <th>url</th>
      <th>codigo</th>
      <th>profissao</th>
      <th>salario</th>
      <th>localidade</th>
      <th>conteudo</th>
      <th>empresa</th>
      <th>data do scraping</th>
      <th>1_dif_data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendiment...</td>
      <td>7206929</td>
      <td>Atendimento - Bh</td>
      <td>1.135,00</td>
      <td>Belo Horizonte, MG</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>VALLOR BENEFICIOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-consultor-...</td>
      <td>7206056</td>
      <td>Consultor De Vendas</td>
      <td>1.000,00 a  3.000,00</td>
      <td>Caruaru, PE</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>Dragorayeb Incorporadora</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-instrutor-...</td>
      <td>7207541</td>
      <td>Instrutor(A) De Solda</td>
      <td>A combinar</td>
      <td>Curitiba, PR</td>
      <td>Area e especializacao profissional: Educacao, ...</td>
      <td>CEBRAC CURITIBA</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-auxiliar-m...</td>
      <td>7207543</td>
      <td>Auxiliar De Manutencao - Campinas</td>
      <td>1.500,00 a  1.600,00</td>
      <td>Campinas, SP</td>
      <td>Area e especializacao profissional: Construcao...</td>
      <td>HM CONSULTORIA E RECURSOS HUMANOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = spark.read.csv('dataset_infojobs.csv',header=True)
df = df.drop('_c0')
display(df)
df.printSchema()

df_1 = df.head(1)
df_2 = df.tail(1)


df_11 = spark.createDataFrame(df_1)
df_22 = spark.createDataFrame(df_2)

df_concat = df_11.union(df_22)
display(df_concat)
df_concat.toPandas()
```


    DataFrame[id: string, site: string, url: string, codigo: string, profissao: string, salario: string, localidade: string, conteudo: string, empresa: string, data do scraping: string, 1_dif_data: string]


    root
     |-- id: string (nullable = true)
     |-- site: string (nullable = true)
     |-- url: string (nullable = true)
     |-- codigo: string (nullable = true)
     |-- profissao: string (nullable = true)
     |-- salario: string (nullable = true)
     |-- localidade: string (nullable = true)
     |-- conteudo: string (nullable = true)
     |-- empresa: string (nullable = true)
     |-- data do scraping: string (nullable = true)
     |-- 1_dif_data: string (nullable = true)
    



    DataFrame[id: string, site: string, url: string, codigo: string, profissao: string, salario: string, localidade: string, conteudo: string, empresa: string, data do scraping: string, 1_dif_data: string]





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>site</th>
      <th>url</th>
      <th>codigo</th>
      <th>profissao</th>
      <th>salario</th>
      <th>localidade</th>
      <th>conteudo</th>
      <th>empresa</th>
      <th>data do scraping</th>
      <th>1_dif_data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendente-...</td>
      <td>7207593</td>
      <td>Atendente De Vendas</td>
      <td>1.500,00 a  1.800,00</td>
      <td>Sao Paulo, SP</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>CESARMAQ</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207600</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Brasilia, DF</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
  </tbody>
</table>
</div>



# upper( ), lower( ) case


```python
df = spark.read.csv('dataset_infojobs.csv',header=True)
df = df.drop('_c0')
display(df)
df.printSchema()



for col in df.columns:
    df = df.withColumnRenamed(col, col.upper())
df.show()


#df = df.toDF(*[c.lower() for c in df.columns])
#df.show()

```


    DataFrame[id: string, site: string, url: string, codigo: string, profissao: string, salario: string, localidade: string, conteudo: string, empresa: string, data do scraping: string, 1_dif_data: string]


    root
     |-- id: string (nullable = true)
     |-- site: string (nullable = true)
     |-- url: string (nullable = true)
     |-- codigo: string (nullable = true)
     |-- profissao: string (nullable = true)
     |-- salario: string (nullable = true)
     |-- localidade: string (nullable = true)
     |-- conteudo: string (nullable = true)
     |-- empresa: string (nullable = true)
     |-- data do scraping: string (nullable = true)
     |-- 1_dif_data: string (nullable = true)
    
    +---+--------+--------------------+-------+--------------------+--------------------+-------------------+--------------------+--------------------+----------------+----------+
    | ID|    SITE|                 URL| CODIGO|           PROFISSAO|             SALARIO|         LOCALIDADE|            CONTEUDO|             EMPRESA|DATA DO SCRAPING|1_DIF_DATA|
    +---+--------+--------------------+-------+--------------------+--------------------+-------------------+--------------------+--------------------+----------------+----------+
    |  1|infojobs|https://www.infoj...|7207593| Atendente De Vendas| 1.500,00 a  1.80...|      Sao Paulo, SP|Area e especializ...|            CESARMAQ|      2021-04-29|   21 days|
    |  2|infojobs|https://www.infoj...|7207597| Vue.Js Tech Lead...|          A combinar|      Fortaleza, CE|Area e especializ...|           BairesDev|      2021-04-29|   21 days|
    |  3|infojobs|https://www.infoj...|7206929|    Atendimento - Bh|           1.135,00 | Belo Horizonte, MG|Area e especializ...|   VALLOR BENEFICIOS|      2021-04-29|   21 days|
    |  4|infojobs|https://www.infoj...|7207595| Vue.Js Tech Lead...|          A combinar|         Recife, PE|Area e especializ...|           BairesDev|      2021-04-29|   21 days|
    |  5|infojobs|https://www.infoj...|7206056| Consultor De Vendas| 1.000,00 a  3.00...|        Caruaru, PE|Area e especializ...|Dragorayeb Incorp...|      2021-04-29|   21 days|
    |  6|infojobs|https://www.infoj...|7207596| Vue.Js Tech Lead...|          A combinar|       Curitiba, PR|Area e especializ...|           BairesDev|      2021-04-29|   21 days|
    |  7|infojobs|https://www.infoj...|7207541| Instrutor(A) De ...|          A combinar|       Curitiba, PR|Area e especializ...|     CEBRAC CURITIBA|      2021-04-29|   21 days|
    |  8|infojobs|https://www.infoj...|7207599| Vue.Js Tech Lead...|          A combinar|      Guarulhos, SP|Area e especializ...|           BairesDev|      2021-04-29|   21 days|
    |  9|infojobs|https://www.infoj...|7207543| Auxiliar De Manu...| 1.500,00 a  1.60...|       Campinas, SP|Area e especializ...|HM CONSULTORIA E ...|      2021-04-29|   21 days|
    | 10|infojobs|https://www.infoj...|7207600| Vue.Js Tech Lead...|          A combinar|       Brasilia, DF|Area e especializ...|           BairesDev|      2021-04-29|   21 days|
    +---+--------+--------------------+-------+--------------------+--------------------+-------------------+--------------------+--------------------+----------------+----------+
    



```python
df = spark.read.csv('dataset_infojobs.csv',header=True)
df = df.drop('_c0')
display(df)
df.printSchema()

import pyspark.sql.functions as f

#Customer_Data = Customer_Data.withColumn("Email_Updated",func.lower(func.col("Email")))

for colun in df.columns:
    df = df.withColumn(colun,f.lower(f.col(colun)))
df.show()


#import pandas as pd
#df = df.toDF(*[df.withColumn(colun, lower(colun)) for colun in df.columns])
#df.show()

#new_df = df.withColumn('Channel', lower(df.Channel))
```


    DataFrame[id: string, site: string, url: string, codigo: string, profissao: string, salario: string, localidade: string, conteudo: string, empresa: string, data do scraping: string, 1_dif_data: string]


    root
     |-- id: string (nullable = true)
     |-- site: string (nullable = true)
     |-- url: string (nullable = true)
     |-- codigo: string (nullable = true)
     |-- profissao: string (nullable = true)
     |-- salario: string (nullable = true)
     |-- localidade: string (nullable = true)
     |-- conteudo: string (nullable = true)
     |-- empresa: string (nullable = true)
     |-- data do scraping: string (nullable = true)
     |-- 1_dif_data: string (nullable = true)
    
    +---+--------+--------------------+-------+--------------------+--------------------+-------------------+--------------------+--------------------+----------------+----------+
    | id|    site|                 url| codigo|           profissao|             salario|         localidade|            conteudo|             empresa|data do scraping|1_dif_data|
    +---+--------+--------------------+-------+--------------------+--------------------+-------------------+--------------------+--------------------+----------------+----------+
    |  1|infojobs|https://www.infoj...|7207593| atendente de vendas| 1.500,00 a  1.80...|      sao paulo, sp|area e especializ...|            cesarmaq|      2021-04-29|   21 days|
    |  2|infojobs|https://www.infoj...|7207597| vue.js tech lead...|          a combinar|      fortaleza, ce|area e especializ...|           bairesdev|      2021-04-29|   21 days|
    |  3|infojobs|https://www.infoj...|7206929|    atendimento - bh|           1.135,00 | belo horizonte, mg|area e especializ...|   vallor beneficios|      2021-04-29|   21 days|
    |  4|infojobs|https://www.infoj...|7207595| vue.js tech lead...|          a combinar|         recife, pe|area e especializ...|           bairesdev|      2021-04-29|   21 days|
    |  5|infojobs|https://www.infoj...|7206056| consultor de vendas| 1.000,00 a  3.00...|        caruaru, pe|area e especializ...|dragorayeb incorp...|      2021-04-29|   21 days|
    |  6|infojobs|https://www.infoj...|7207596| vue.js tech lead...|          a combinar|       curitiba, pr|area e especializ...|           bairesdev|      2021-04-29|   21 days|
    |  7|infojobs|https://www.infoj...|7207541| instrutor(a) de ...|          a combinar|       curitiba, pr|area e especializ...|     cebrac curitiba|      2021-04-29|   21 days|
    |  8|infojobs|https://www.infoj...|7207599| vue.js tech lead...|          a combinar|      guarulhos, sp|area e especializ...|           bairesdev|      2021-04-29|   21 days|
    |  9|infojobs|https://www.infoj...|7207543| auxiliar de manu...| 1.500,00 a  1.60...|       campinas, sp|area e especializ...|hm consultoria e ...|      2021-04-29|   21 days|
    | 10|infojobs|https://www.infoj...|7207600| vue.js tech lead...|          a combinar|       brasilia, df|area e especializ...|           bairesdev|      2021-04-29|   21 days|
    +---+--------+--------------------+-------+--------------------+--------------------+-------------------+--------------------+--------------------+----------------+----------+
    



```python
import pyspark.sql.functions as f


for colun in df.columns:
    df = df.withColumn(colun,f.lower(f.col(colun)))
df.show()
```


```python
Customer_Data = Customer_Data.withColumn("Email_Updated",func.lower(func.col("Email")))
```

# Apply( ) with multi columns


```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Name_Spark').getOrCreate()

df = spark.read.csv('dataset_infojobs.csv',header=True)
df = df.drop('_c0')
display(df)
df.printSchema()

df = df.toPandas().head(3)
df
```

    WARNING: An illegal reflective access operation has occurred
    WARNING: Illegal reflective access by org.apache.spark.unsafe.Platform (file:/usr/local/spark-3.2.0-bin-hadoop3.2/jars/spark-unsafe_2.12-3.2.0.jar) to constructor java.nio.DirectByteBuffer(long,int)
    WARNING: Please consider reporting this to the maintainers of org.apache.spark.unsafe.Platform
    WARNING: Use --illegal-access=warn to enable warnings of further illegal reflective access operations
    WARNING: All illegal access operations will be denied in a future release
    Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
    Setting default log level to "WARN".
    To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
    21/11/16 19:53:41 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
    21/11/16 19:53:42 WARN Utils: Service 'SparkUI' could not bind on port 4040. Attempting port 4041.



    DataFrame[id: string, site: string, url: string, codigo: string, profissao: string, salario: string, localidade: string, conteudo: string, empresa: string, data do scraping: string, 1_dif_data: string]


    root
     |-- id: string (nullable = true)
     |-- site: string (nullable = true)
     |-- url: string (nullable = true)
     |-- codigo: string (nullable = true)
     |-- profissao: string (nullable = true)
     |-- salario: string (nullable = true)
     |-- localidade: string (nullable = true)
     |-- conteudo: string (nullable = true)
     |-- empresa: string (nullable = true)
     |-- data do scraping: string (nullable = true)
     |-- 1_dif_data: string (nullable = true)
    





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>site</th>
      <th>url</th>
      <th>codigo</th>
      <th>profissao</th>
      <th>salario</th>
      <th>localidade</th>
      <th>conteudo</th>
      <th>empresa</th>
      <th>data do scraping</th>
      <th>1_dif_data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendente-...</td>
      <td>7207593</td>
      <td>Atendente De Vendas</td>
      <td>1.500,00 a  1.800,00</td>
      <td>Sao Paulo, SP</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>CESARMAQ</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207597</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Fortaleza, CE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendiment...</td>
      <td>7206929</td>
      <td>Atendimento - Bh</td>
      <td>1.135,00</td>
      <td>Belo Horizonte, MG</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>VALLOR BENEFICIOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
  </tbody>
</table>
</div>




```python
!pip install unidecode
from unidecode import unidecode

for col in df.columns:
    df[col] = df[col].apply(unidecode)
df
```

    Requirement already satisfied: unidecode in /opt/conda/lib/python3.9/site-packages (1.3.2)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>site</th>
      <th>url</th>
      <th>codigo</th>
      <th>profissao</th>
      <th>salario</th>
      <th>localidade</th>
      <th>conteudo</th>
      <th>empresa</th>
      <th>data do scraping</th>
      <th>1_dif_data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendente-...</td>
      <td>7207593</td>
      <td>Atendente De Vendas</td>
      <td>1.500,00 a  1.800,00</td>
      <td>Sao Paulo, SP</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>CESARMAQ</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-vue-js-tec...</td>
      <td>7207597</td>
      <td>Vue.Js Tech Lead - Remote Work.</td>
      <td>A combinar</td>
      <td>Fortaleza, CE</td>
      <td>Area e especializacao profissional: Informatic...</td>
      <td>BairesDev</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>infojobs</td>
      <td>https://www.infojobs.com.br/vaga-de-atendiment...</td>
      <td>7206929</td>
      <td>Atendimento - Bh</td>
      <td>1.135,00</td>
      <td>Belo Horizonte, MG</td>
      <td>Area e especializacao profissional: Comercial,...</td>
      <td>VALLOR BENEFICIOS</td>
      <td>2021-04-29</td>
      <td>21 days</td>
    </tr>
  </tbody>
</table>
</div>




```python
from jupyterthemes import get_themes
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    /tmp/ipykernel_50/3930510084.py in <module>
    ----> 1 from jupyterthemes import get_themes
    

    ModuleNotFoundError: No module named 'jupyterthemes'



```python
!pip install jupyterthemes
import jupyterthemes as jt
#from jupyterthemes.stylefx import set_nb_theme
#set_nb_theme('chesterish')
#!pip list
!jt -t chesterish -f fira -fs 10 -nf ptsans -nfs 11 -N -kl -cursw 2 -cursc r -cellw 95% -T

```

    Collecting jupyterthemes
      Downloading jupyterthemes-0.20.0-py2.py3-none-any.whl (7.0 MB)
         |████████████████████████████████| 7.0 MB 1.0 MB/s            
    [?25hRequirement already satisfied: matplotlib>=1.4.3 in /opt/conda/lib/python3.9/site-packages (from jupyterthemes) (3.4.3)
    Requirement already satisfied: ipython>=5.4.1 in /opt/conda/lib/python3.9/site-packages (from jupyterthemes) (7.29.0)
    Requirement already satisfied: notebook>=5.6.0 in /opt/conda/lib/python3.9/site-packages (from jupyterthemes) (6.4.5)
    Requirement already satisfied: jupyter-core in /opt/conda/lib/python3.9/site-packages (from jupyterthemes) (4.9.1)
    Collecting lesscpy>=0.11.2
      Downloading lesscpy-0.15.0-py2.py3-none-any.whl (46 kB)
         |████████████████████████████████| 46 kB 454 kB/s            
    [?25hRequirement already satisfied: pygments in /opt/conda/lib/python3.9/site-packages (from ipython>=5.4.1->jupyterthemes) (2.10.0)
    Requirement already satisfied: traitlets>=4.2 in /opt/conda/lib/python3.9/site-packages (from ipython>=5.4.1->jupyterthemes) (5.1.1)
    Requirement already satisfied: pexpect>4.3 in /opt/conda/lib/python3.9/site-packages (from ipython>=5.4.1->jupyterthemes) (4.8.0)
    Requirement already satisfied: decorator in /opt/conda/lib/python3.9/site-packages (from ipython>=5.4.1->jupyterthemes) (5.1.0)
    Requirement already satisfied: matplotlib-inline in /opt/conda/lib/python3.9/site-packages (from ipython>=5.4.1->jupyterthemes) (0.1.3)
    Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /opt/conda/lib/python3.9/site-packages (from ipython>=5.4.1->jupyterthemes) (3.0.21)
    Requirement already satisfied: setuptools>=18.5 in /opt/conda/lib/python3.9/site-packages (from ipython>=5.4.1->jupyterthemes) (58.5.2)
    Requirement already satisfied: backcall in /opt/conda/lib/python3.9/site-packages (from ipython>=5.4.1->jupyterthemes) (0.2.0)
    Requirement already satisfied: pickleshare in /opt/conda/lib/python3.9/site-packages (from ipython>=5.4.1->jupyterthemes) (0.7.5)
    Requirement already satisfied: jedi>=0.16 in /opt/conda/lib/python3.9/site-packages (from ipython>=5.4.1->jupyterthemes) (0.18.0)
    Collecting ply
      Downloading ply-3.11-py2.py3-none-any.whl (49 kB)
         |████████████████████████████████| 49 kB 372 kB/s            
    [?25hRequirement already satisfied: six in /opt/conda/lib/python3.9/site-packages (from lesscpy>=0.11.2->jupyterthemes) (1.16.0)
    Requirement already satisfied: pyparsing>=2.2.1 in /opt/conda/lib/python3.9/site-packages (from matplotlib>=1.4.3->jupyterthemes) (2.4.7)
    Requirement already satisfied: numpy>=1.16 in /opt/conda/lib/python3.9/site-packages (from matplotlib>=1.4.3->jupyterthemes) (1.20.3)
    Requirement already satisfied: python-dateutil>=2.7 in /opt/conda/lib/python3.9/site-packages (from matplotlib>=1.4.3->jupyterthemes) (2.8.2)
    Requirement already satisfied: pillow>=6.2.0 in /opt/conda/lib/python3.9/site-packages (from matplotlib>=1.4.3->jupyterthemes) (8.3.2)
    Requirement already satisfied: cycler>=0.10 in /opt/conda/lib/python3.9/site-packages (from matplotlib>=1.4.3->jupyterthemes) (0.11.0)
    Requirement already satisfied: kiwisolver>=1.0.1 in /opt/conda/lib/python3.9/site-packages (from matplotlib>=1.4.3->jupyterthemes) (1.3.2)
    Requirement already satisfied: tornado>=6.1 in /opt/conda/lib/python3.9/site-packages (from notebook>=5.6.0->jupyterthemes) (6.1)
    Requirement already satisfied: jupyter-client>=5.3.4 in /opt/conda/lib/python3.9/site-packages (from notebook>=5.6.0->jupyterthemes) (7.0.6)
    Requirement already satisfied: jinja2 in /opt/conda/lib/python3.9/site-packages (from notebook>=5.6.0->jupyterthemes) (3.0.2)
    Requirement already satisfied: terminado>=0.8.3 in /opt/conda/lib/python3.9/site-packages (from notebook>=5.6.0->jupyterthemes) (0.12.1)
    Requirement already satisfied: ipython-genutils in /opt/conda/lib/python3.9/site-packages (from notebook>=5.6.0->jupyterthemes) (0.2.0)
    Requirement already satisfied: Send2Trash>=1.5.0 in /opt/conda/lib/python3.9/site-packages (from notebook>=5.6.0->jupyterthemes) (1.8.0)
    Requirement already satisfied: prometheus-client in /opt/conda/lib/python3.9/site-packages (from notebook>=5.6.0->jupyterthemes) (0.12.0)
    Requirement already satisfied: pyzmq>=17 in /opt/conda/lib/python3.9/site-packages (from notebook>=5.6.0->jupyterthemes) (22.3.0)
    Requirement already satisfied: argon2-cffi in /opt/conda/lib/python3.9/site-packages (from notebook>=5.6.0->jupyterthemes) (21.1.0)
    Requirement already satisfied: nbformat in /opt/conda/lib/python3.9/site-packages (from notebook>=5.6.0->jupyterthemes) (5.1.3)
    Requirement already satisfied: ipykernel in /opt/conda/lib/python3.9/site-packages (from notebook>=5.6.0->jupyterthemes) (6.4.2)
    Requirement already satisfied: nbconvert in /opt/conda/lib/python3.9/site-packages (from notebook>=5.6.0->jupyterthemes) (6.2.0)
    Requirement already satisfied: parso<0.9.0,>=0.8.0 in /opt/conda/lib/python3.9/site-packages (from jedi>=0.16->ipython>=5.4.1->jupyterthemes) (0.8.2)
    Requirement already satisfied: nest-asyncio>=1.5 in /opt/conda/lib/python3.9/site-packages (from jupyter-client>=5.3.4->notebook>=5.6.0->jupyterthemes) (1.5.1)
    Requirement already satisfied: entrypoints in /opt/conda/lib/python3.9/site-packages (from jupyter-client>=5.3.4->notebook>=5.6.0->jupyterthemes) (0.3)
    Requirement already satisfied: ptyprocess>=0.5 in /opt/conda/lib/python3.9/site-packages (from pexpect>4.3->ipython>=5.4.1->jupyterthemes) (0.7.0)
    Requirement already satisfied: wcwidth in /opt/conda/lib/python3.9/site-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython>=5.4.1->jupyterthemes) (0.2.5)
    Requirement already satisfied: cffi>=1.0.0 in /opt/conda/lib/python3.9/site-packages (from argon2-cffi->notebook>=5.6.0->jupyterthemes) (1.14.6)
    Requirement already satisfied: debugpy<2.0,>=1.0.0 in /opt/conda/lib/python3.9/site-packages (from ipykernel->notebook>=5.6.0->jupyterthemes) (1.4.1)
    Requirement already satisfied: MarkupSafe>=2.0 in /opt/conda/lib/python3.9/site-packages (from jinja2->notebook>=5.6.0->jupyterthemes) (2.0.1)
    Requirement already satisfied: testpath in /opt/conda/lib/python3.9/site-packages (from nbconvert->notebook>=5.6.0->jupyterthemes) (0.5.0)
    Requirement already satisfied: mistune<2,>=0.8.1 in /opt/conda/lib/python3.9/site-packages (from nbconvert->notebook>=5.6.0->jupyterthemes) (0.8.4)
    Requirement already satisfied: jupyterlab-pygments in /opt/conda/lib/python3.9/site-packages (from nbconvert->notebook>=5.6.0->jupyterthemes) (0.1.2)
    Requirement already satisfied: pandocfilters>=1.4.1 in /opt/conda/lib/python3.9/site-packages (from nbconvert->notebook>=5.6.0->jupyterthemes) (1.5.0)
    Requirement already satisfied: nbclient<0.6.0,>=0.5.0 in /opt/conda/lib/python3.9/site-packages (from nbconvert->notebook>=5.6.0->jupyterthemes) (0.5.4)
    Requirement already satisfied: defusedxml in /opt/conda/lib/python3.9/site-packages (from nbconvert->notebook>=5.6.0->jupyterthemes) (0.7.1)
    Requirement already satisfied: bleach in /opt/conda/lib/python3.9/site-packages (from nbconvert->notebook>=5.6.0->jupyterthemes) (4.1.0)
    Requirement already satisfied: jsonschema!=2.5.0,>=2.4 in /opt/conda/lib/python3.9/site-packages (from nbformat->notebook>=5.6.0->jupyterthemes) (4.1.2)
    Requirement already satisfied: pycparser in /opt/conda/lib/python3.9/site-packages (from cffi>=1.0.0->argon2-cffi->notebook>=5.6.0->jupyterthemes) (2.20)
    Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /opt/conda/lib/python3.9/site-packages (from jsonschema!=2.5.0,>=2.4->nbformat->notebook>=5.6.0->jupyterthemes) (0.17.3)
    Requirement already satisfied: attrs>=17.4.0 in /opt/conda/lib/python3.9/site-packages (from jsonschema!=2.5.0,>=2.4->nbformat->notebook>=5.6.0->jupyterthemes) (21.2.0)
    Requirement already satisfied: packaging in /opt/conda/lib/python3.9/site-packages (from bleach->nbconvert->notebook>=5.6.0->jupyterthemes) (21.2)
    Requirement already satisfied: webencodings in /opt/conda/lib/python3.9/site-packages (from bleach->nbconvert->notebook>=5.6.0->jupyterthemes) (0.5.1)
    Installing collected packages: ply, lesscpy, jupyterthemes
    Successfully installed jupyterthemes-0.20.0 lesscpy-0.15.0 ply-3.11



```python

```


```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Name_Spark').getOrCreate()

df = spark.read.csv('dataset_infojobs.csv',header=True)
df = df.drop('_c0')
df.printSchema()
```

    root
     |-- id: string (nullable = true)
     |-- site: string (nullable = true)
     |-- url: string (nullable = true)
     |-- codigo: string (nullable = true)
     |-- profissao: string (nullable = true)
     |-- salario: string (nullable = true)
     |-- localidade: string (nullable = true)
     |-- conteudo: string (nullable = true)
     |-- empresa: string (nullable = true)
     |-- data do scraping: string (nullable = true)
     |-- 1_dif_data: string (nullable = true)
    



```python
display(df)
```


    DataFrame[id: string, site: string, url: string, codigo: string, profissao: string, salario: string, localidade: string, conteudo: string, empresa: string, data do scraping: string, 1_dif_data: string]



```python
df.show(5)
```

    +---+--------+--------------------+-------+--------------------+--------------------+-------------------+--------------------+--------------------+----------------+----------+
    | id|    site|                 url| codigo|           profissao|             salario|         localidade|            conteudo|             empresa|data do scraping|1_dif_data|
    +---+--------+--------------------+-------+--------------------+--------------------+-------------------+--------------------+--------------------+----------------+----------+
    |  1|infojobs|https://www.infoj...|7207593| Atendente De Vendas| 1.500,00 a  1.80...|      Sao Paulo, SP|Area e especializ...|            CESARMAQ|      2021-04-29|   21 days|
    |  2|infojobs|https://www.infoj...|7207597| Vue.Js Tech Lead...|          A combinar|      Fortaleza, CE|Area e especializ...|           BairesDev|      2021-04-29|   21 days|
    |  3|infojobs|https://www.infoj...|7206929|    Atendimento - Bh|           1.135,00 | Belo Horizonte, MG|Area e especializ...|   VALLOR BENEFICIOS|      2021-04-29|   21 days|
    |  4|infojobs|https://www.infoj...|7207595| Vue.Js Tech Lead...|          A combinar|         Recife, PE|Area e especializ...|           BairesDev|      2021-04-29|   21 days|
    |  5|infojobs|https://www.infoj...|7206056| Consultor De Vendas| 1.000,00 a  3.00...|        Caruaru, PE|Area e especializ...|Dragorayeb Incorp...|      2021-04-29|   21 days|
    +---+--------+--------------------+-------+--------------------+--------------------+-------------------+--------------------+--------------------+----------------+----------+
    only showing top 5 rows
    



```python
import csv

df = csv.loads(re.sub(72, 'setenta e dois'))
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    /tmp/ipykernel_33/2506699769.py in <module>
          1 import csv
          2 
    ----> 3 df = csv.loads(re.sub(72, 'setenta e dois'))
    

    AttributeError: module 'csv' has no attribute 'loads'



```python
##################################################################################################
```

<ul>
  <li> df_1.union(df_2) </li>
  <li> expression = [func.lower(func.col(x).alias(x) for x in df.columns]</li>
  <li> df.select(*expression(.show() </li>
</ul>


```python
from pyspark.sql import functions as psf

df_concat = df_11.union(df_22)
expression = [ psf.lower(psf.col(x)).alias(x) for x in df_concat.columns ]
df_concat.select(*expression).show()
```


```python
df_accents_0 = [ unidecode(x) for x in df_accents.columns]
```


```python
for item in df.head(1)[0]:
    print(item)
for item in df.head(1)[0]:
    print(item)
Krish
31
10
30000
```

<ul>
  <li><b> df.withColumn('Column_Name', df[''Column_Name']+2) </b></li>
      <dd> - DataFrame[Name: string, age: int, Experience: int, Salary: int, Experience after 2 years: int]</dd>
          <p>
        
  <li><b> df.drop('Column_Name') </b></li>
      <dd></dd>
          <p>      
        
  <li><b> df = df.withColumnRenamed('Column_Name_1',''Column_Name_2')</b></li>
      <dd> - DataFrame[New Name: string, age: int, Experience: int, Salary: int]</dd>
          <p>
              
  <li><b> sfhit+tab+tab </b></li>
      <dd></dd>
          <p>
              
  <li><b> df.na.drop(how='all').show() </b></li>
      <dd></dd>
          <p>
              
  <li><b> df.na.drop(how='any',thresh=2).show() </b></li>
      <dd></dd>
          <p>  
              
  <li><b> df.na.drop(how='any',subset=['Column_Name']).show() </b></li>
      <dd></dd>
          <p>

  <li style="font-size:25px;"><b> ### Filling the missing value ### </b></li>
  <li><b> df.na.fill('Missing Value').show() </b></li>            
  <li><b> df.na.fill(value=3,subset=['Experience']).show() </b></li>                       
  <li><b> df.fillna('Missing Value').show() </b></li>
  <li><b> df.fillna('Missing Value',subset=['age']).show() </b></li>
  <li><b> df.na.fill({'age':'Missing'}).show() </b></li>
              
              
  <dd> </dd>
      <p>      
            
  <li><b> df.na.fill('Missing Value').show() </b></li>
  <li><b> df.na.fill('Missing Value','Experience').show() </b></li>
  <dd> </dd>
      <p>          
          
          
  <li><b> df.describe() </b></li>
          <dd> </dd>
    <p>
        
  <li><b> df.types() </b></li>
          <dd> - (['Name', 'string'])</dd>
    <p>
        
  <li><b> spark = SparkSession.builder.appName('Name_Spark').getOrCreate() </b></li>
      <dd></dd>
          <p>      
        
  <li><b> df = spark.read.csv (-File.csv-) </b></li>
      <dd></dd>
          <p>  
              
  <li><b> expression = [func.lower(func.col(x).alias(x) for x in df.columns] </b></li>
      <dd></dd>
          <p> 

</ul>


```python
spark = SparkSession \
    .builder \
    .appName('Python Spark create RDD example') \
    .config('spark.some.config.option', 'some-value') \
    .getOrCreate()
    
df = spark.sparkContext.parallelize([(1,2,3, 23),
                                    (4,5,6, 32),
                                    (7,8,9, 52)]).toDF(['col1', 'col2', 'col3', 'col4'])
df.show()


df['new_column_created'] = df.apply()
```

    +----+----+----+----+
    |col1|col2|col3|col4|
    +----+----+----+----+
    |   1|   2|   3|  23|
    |   4|   5|   6|  32|
    |   7|   8|   9|  52|
    +----+----+----+----+
    



```python
from pyspark.ml.feature import Imputer
```


```python
imputer = Imputer(
    inputCols = ['col1','col2', 'col3', 'col4'],
outputCols = ["{}_imputed".format(c) for c in ['col1','col2', 'col3', 'col4']]
).setStrategy("mean")
```


```python
imputer.fit(df).transform(df).show()
```

    +----+----+----+----+------------+------------+------------+------------+
    |col1|col2|col3|col4|col1_imputed|col2_imputed|col3_imputed|col4_imputed|
    +----+----+----+----+------------+------------+------------+------------+
    |   1|   2|   3|  23|           1|           2|           3|          23|
    |   4|   5|   6|  32|           4|           5|           6|          32|
    |   7|   8|   9|  52|           7|           8|           9|          52|
    +----+----+----+----+------------+------------+------------+------------+
    



```python
spark_frame_for_training_mapping.toDF(*new_names).show(4)
```

# <h1 style="border:2px solid black; background-color:#33FFF4; color:red"> Filter </h1>

```

- df[(df.column > 2)].show()

- df[(df['column_name > 2')].show()

- df[(df.column_1 > 2) & (df.column_2 == 2) ].show()

- df.filter('salary <= 2000').show()

- df.spark.filter('Salary <= 20000').select(['Name', 'age']).show()

- df.filter(df_pyspark['Salary'] <=20000).show()

- df.filter((df_pyspark['Salary']<=20000) | (df['Salary']>=15000)).show()

- df.filter(~(df_pyspark['Salary']<=20000)).show()

- df_pyspark.filter(~(df_pyspark['Salary']<=20000)).show()

- df_pyspark.filter("age < 50").select('Name').show()

- df_pyspark.filter(df_pyspark["age"] < 50).select('Name').show()

- df_pyspark.filter(df_pyspark["age"] < 50).show()

- df_pyspark.filter( (df_pyspark['age'] < 30) & ~(df_pyspark['Experience'] > 30000) ).show()

- # df_pyspark_DATAFRAME.FILTERING( ( ONLY VALUES FROM df_pyspark < 30)) and (ONLY VALUES DOESNT  df_pyspark > 30000)).show()

- df_pyspark.filter(df_pyspark["age"] == 30).collect()

- result = df_pyspark.filter(df_pyspark["age"] == 30).collect()

- row = result[0]

- row.asDict()
{'Name': 'Sudhanshu', 'age': 30, 'Experience': 8, 'Salary': 25000}

- result[0].asDict()
{'Name': 'Sudhanshu', 'age': 30, 'Experience': 8, 'Salary': 25000}

- row.asDict()['Name']
'Sudhanshu'


- df.filter('Close < 500').select(['Open','Close']).show()

- df.filter("Close < 500").select('Open').show()

- df.filter(df['Close'] < 500).select('Volume').show()

- df.filter("Close < 500").select(["Open","Close"]).show()

- df.filter( (df['Close'] < 200) & (df['Open'] > 200) ).show()

- and === &

df.filter( (df['Close'] < 200) & ~(df['Open'] > 200) ).show()

# ~ NOT

=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x

### Pyspark Group And Aggregate Functions ###

- df_spark.groupBy('Name').sum()
DataFrame[Name: string, sum(salary): bigint]

- df_spark.groupBy('Name').sum().show()

- df_spark.groupBy('Departments').sum().show()

- df_spark.groupBy('Departments').mean().show()

- df_spark.groupBy('Departments').count().show()

- df_spark.agg({'Salary':'sum'}).show()

=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x

- df.head(3)

- df.head(3)[0]

- df.dtypes

- df.columns

- df_imputer.filter(df_imputer['Qual a sua escola?'].isNotNull()).toPandas().head(5)
# isNotNull())

- Dict_Null = {col:df_imputer.filter(df_imputer[col].isNull()).count() for col in df_imputer.columns}
Dict_Null
#Dict_Null = [col:df_imputer.filter(df_imputer[col].isNull()).count() for col in df_imputer.columns]                   ^
#SyntaxError: invalid syntax

- col:df_imputer.filter(df_imputer[col].isNull()).count() 

- df_imputer.filter(df_imputer['Qual o seu nome?'].isNull()).count()

- spark_frame_for_training.na.replace(['1'],['na.replace()']).show()
- spark_frame_for_training.na.replace(['1'],['na.replace()-Id'],subset=['Id']).show()

- spark_frame_for_training_ds.toDF('a','b','c','d').show()

- spark_frame_for_training_dp.columns = ['a','b','c','d']
spark_frame_for_training_dp

```

```
from pyspark.sql import SparkSession

from pyspark.sql.session import SparkSession

# from pyspark.sql.types import (StructField, StringType, IntegerType, StructType)
from pyspark.sql.types import (ArrayType, StructField, StructType, StringType, IntegerType)

spark = SparkSession.builder.getOrCreate()
spark = SparkSession.builder.appName('ops').getOrCreate()

data_schema = [StructField('age', IntegerType(), True),
              StructField('name', StringType(), True)]

final_struc = StructType(fields=data_schema)

df_v1 = spark.read.json('people.json', schema=final_struc)

df_v1.printSchema()

```

```
##### PySpark Session #####

# File location and type
# file_location = "/FileStore/tables/empresa_est.csv"
file_location = "/gov/usr_upload/source/dados.csv"
file_type = "csv"

# CSV options
infer_schema = "false"
first_row_is_header = "false"
delimiter = ","

df = spark.read.format(file_type) \
  .option("inferSchema", infer_schema) \
  .option("header", first_row_is_header) \
  .option("sep", delimiter) \
  .load(file_location)

df

spark = SparkSession \
    .builder \
    .appName('Python Spark create RDD example') \
    .config('spark.some.config.option', 'some-value') \
    .getOrCreate()

------------------><------------------><------------------><------------------><------------------><
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Python Spark create RDD example").config("spark.some.config.option", "some-value").getOrCreate()

my_list = [['a', 1, None], ['b', 2, 3],['c', 3, 4]]
spark.createDataFrame('my_list', ['A', 'B', 'C']

Employee = spark.createDataFrame([ ('1', 'Joe', '70000', '1'),
                                  ('2', 'Henry', '80000', '2'),
                                  ('3', 'Sam', '60000', '2'),
                                  ('4', 'Max', '90000', '1')],
                                 ['Id', 'Name', 'Sallary','DepartmentId'] )
                                 


```
##### SQL #####

df.createOrReplaceTempView('Name')

results = spark.sql("SELECT * FROM people")

results = spark.sql("select * from people WHEre age=30")

results.show()

=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x


```
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

x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x====x=====x===

```

