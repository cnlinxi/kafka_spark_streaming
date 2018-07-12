# python producer.pykafka_spark_streaming
A very simple example of using streaming data by kafka &amp; spark streaming &amp; mongodb & bokeh

![](http://7xrvee.com1.z0.glb.clouddn.com/18-7-12/57092408.jpg)

We produce some simulated streaming data and put them into kafka. Spark streaming comsume streaming data and insert data into mongodb. Then we use boken to display streaming data dynamically.

### Get Started

####main dependencies

- [Kafka](http://kafka.apache.org/): Kafka is used for building real-time data pipelines and streaming apps. 
- [Spark streaming](https://spark.apache.org/streaming/): Spark streaming process streaming data.
- [MongoDB](https://www.mongodb.com/): MongoDB is used for storing data.
- [bokeh](https://bokeh.pydata.org/en/latest/): bokeh display data~

####run it

*In your shell,*

- clone this repo.

  ```shell
  git@github.com:cnlinxi/kafka_spark_streaming.git
  ```

-  produce data into kafka.

  ```
  python producer.py
  ```

- receive data by spark streaming and put data into mongodb.

  ```
  spark-submit --packages <spark-streaming-kafka java package> receiver.py
  ```

  in my case (spark2.1.1), it is:

  ```
  spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.1.1 receiver.py
  ```

  or you can follow [this](https://stackoverflow.com/questions/35560767/pyspark-streaming-with-kafka-in-pycharm ) debug spark streaming by pycharm.

- display data by bokeh.

  ```
  bokeh serve data_display.py
  ```

### File Structure

- [data_display.py](https://github.com/cnlinxi/kafka_spark_streaming/blob/master/data_display.py): display data by bokeh.
- [global_vals.py](https://github.com/cnlinxi/kafka_spark_streaming/blob/master/global_vals.py): global variable.
- [mongo_utils.py](https://github.com/cnlinxi/kafka_spark_streaming/blob/master/mongo_utils.py): tools of mongodb.
- [producer.py](https://github.com/cnlinxi/kafka_spark_streaming/blob/master/producer.py): produce data into kafka 
- [producer_without_kafka.py](https://github.com/cnlinxi/kafka_spark_streaming/blob/master/producer_without_kafka.py): simulator of producing data without kafka for debug 
- [receiver.py](https://github.com/cnlinxi/kafka_spark_streaming/blob/master/receiver.py): receive data coming from kafka (producer.py) and insert data into mongodb.

### Connect

cnmengnan@gmail.com

blog: [WinterColor blog](http://wintercolor.azurewebsites.net/)

engoy it~