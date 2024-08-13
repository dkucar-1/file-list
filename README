This is a simple utility to recursively list files in a web directory.
It uses `BeautifulSoup` to find http links within a webpage and recursively searches through its sub directories. It uses a breath-first search (level order search) so it will display all files under the current level first before going to the next level.

### Usage ###
From the directory where you've copied this file, let's say we want to view the entire spark subdirectory of apache.org, we run something like this.

```
./recursive_list.py https://downloads.apache.org/spark/
```

This will display something like this
```
KEYS
spark-3.4.3/
  SparkR_3.4.3.tar.gz
  SparkR_3.4.3.tar.gz.asc
  SparkR_3.4.3.tar.gz.sha512
  pyspark-3.4.3.tar.gz
  pyspark-3.4.3.tar.gz.asc
  pyspark-3.4.3.tar.gz.sha512
  spark-3.4.3-bin-hadoop3-scala2.13.tgz
  spark-3.4.3-bin-hadoop3-scala2.13.tgz.asc
  spark-3.4.3-bin-hadoop3-scala2.13.tgz.sha512
  spark-3.4.3-bin-hadoop3.tgz
  spark-3.4.3-bin-hadoop3.tgz.asc
  spark-3.4.3-bin-hadoop3.tgz.sha512
  spark-3.4.3-bin-without-hadoop.tgz
  spark-3.4.3-bin-without-hadoop.tgz.asc
  spark-3.4.3-bin-without-hadoop.tgz.sha512
  spark-3.4.3.tgz
  spark-3.4.3.tgz.asc
  spark-3.4.3.tgz.sha512
spark-3.5.2/
  SparkR_3.5.2.tar.gz
  SparkR_3.5.2.tar.gz.asc
  SparkR_3.5.2.tar.gz.sha512
  pyspark-3.5.2.tar.gz
  pyspark-3.5.2.tar.gz.asc
  pyspark-3.5.2.tar.gz.sha512
  spark-3.5.2-bin-hadoop3-scala2.13.tgz
  spark-3.5.2-bin-hadoop3-scala2.13.tgz.asc
  spark-3.5.2-bin-hadoop3-scala2.13.tgz.sha512
  spark-3.5.2-bin-hadoop3.tgz
  spark-3.5.2-bin-hadoop3.tgz.asc
  spark-3.5.2-bin-hadoop3.tgz.sha512
  spark-3.5.2-bin-without-hadoop.tgz
  spark-3.5.2-bin-without-hadoop.tgz.asc
  spark-3.5.2-bin-without-hadoop.tgz.sha512
  spark-3.5.2.tgz
  spark-3.5.2.tgz.asc
  spark-3.5.2.tgz.sha512
spark-4.0.0-preview1/
  SparkR_4.0.0-preview1.tar.gz
  SparkR_4.0.0-preview1.tar.gz.asc
  SparkR_4.0.0-preview1.tar.gz.sha512
  pyspark-4.0.0.dev1.tar.gz
  pyspark-4.0.0.dev1.tar.gz.asc
  pyspark-4.0.0.dev1.tar.gz.sha512
  pyspark_connect-4.0.0.dev1.tar.gz
  pyspark_connect-4.0.0.dev1.tar.gz.asc
  pyspark_connect-4.0.0.dev1.tar.gz.sha512
  spark-4.0.0-preview1-bin-hadoop3.tgz
  spark-4.0.0-preview1-bin-hadoop3.tgz.asc
  spark-4.0.0-preview1-bin-hadoop3.tgz.sha512
  spark-4.0.0-preview1-bin-without-hadoop.tgz
  spark-4.0.0-preview1-bin-without-hadoop.tgz.asc
  spark-4.0.0-preview1-bin-without-hadoop.tgz.sha512
  spark-4.0.0-preview1.tgz
  spark-4.0.0-preview1.tgz.asc
  spark-4.0.0-preview1.tgz.sha512
```
