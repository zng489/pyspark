
# What's RDD...
##### http://vishnuviswanath.com/spark_rdd.html

Spark RDDs are very simple at the same time very important concept in Apache Spark. Most of you might be knowing the full form of RDD, it is Resilient Distributed Datasets. Resilient because RDDs are immutable(can’t be modified once created) and fault tolerant, Distributed because it is distributed across cluster and Dataset because it holds data.

So why RDD? Apache Spark lets you treat your input files almost like any other variable, which you cannot do in Hadoop MapReduce. RDDs are automatically distributed across the network by means of Partitions.

Partitions

RDDs are divided into smaller chunks called Partitions, and when you execute some action, a task is launched per partition. So it means, the more the number of partitions, the more the parallelism. Spark automatically decides the number of partitions that an RDD has to be divided into but you can also specify the number of partitions when creating an RDD. These partitions of an RDD is distributed across all the nodes in the network.

---


# .cache() and .persist() ...
##### https://www.learntospark.com/2020/05/persist-and-cache-in-apache-spark.html
##### https://www.youtube.com/watch?v=4U1qscwcB1g&t=10s
#####
#####
#####

Use when you work constantly with the same dataset.

##### https://medium.com/pecan-ai/caching-spark-dataframe-how-when-79a8c13254c0
When to cache?
If you’re executing multiple actions on the same DataFrame then cache it.
Let’s look on an example:

---

# Sc.parallelize() - sc.parallelize() method is the spark context parallelize method to create a parallelized collection.
##### https://www.oreilly.com/library/view/pyspark-cookbook/9781788835367/891b6c2a-889b-4189-a133-52c14436e666.xhtml
Spark context parallelize method
Under the covers, there are quite a few actions that happened when you created your RDD. Let's start with the RDD creation and break down this code snippet:

myRDD = sc.parallelize(  [('Mike', 19), ('June', 18), ('Rachel',16), ('Rob', 18), ('Scott', 17)])
Focusing first on the statement in the sc.parallelize() method, we first created a Python list (that is, [A, B, ..., E]) composed of a list of arrays (that is, ('Mike', 19), ('June', 19), ..., ('Scott', 17)). The sc.parallelize() method is the SparkContext's parallelize method to create a parallelized collection. This allows Spark to distribute the data across multiple nodes, instead of depending on a single node to process the data:

Now that we have created ...

