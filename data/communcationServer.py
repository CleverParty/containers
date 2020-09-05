# notes : 
# ==> Caveats
# To have launchd start kafka now and restart at login:
# brew services start kafka
# To have launchd start zookeeper now and restart at login:
#  brew services start zookeeper
# Or, if you don't want/need a background service you can just run:
#  zkServer start
# ==> kafka
# To have launchd start kafka now and restart at login:
#   brew services start kafka
# Or, if you don't want/need a background service you can just run:
#   zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties & kafka-server-start /usr/local/etc/kafka/server.properties
# to start server : zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties
from time import sleep
from json import dumps
import datetime
import pandas 
from kafka import KafkaProducer
# simplified steps for kafka:
# step 1 : brew install kafka
# step 2 : start brokers, and kafka cluster requirements
# step 3 : create topics , producers and consumers on said topic
# step 4 : enjoy TCP protocol speeds
# default is set to localhost:9092 to change default port edit file at : vim /usr/local/etc/kafka/server.properties
import tickerScanner as ticker


def main():
    start = datetime.datetime(2020,8,1) # format :- year,month,day
    end = datetime.datetime.today()
    dataframe,head = ticker.create("AAPL",start,end)
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
    head = head.to_json()
    producer.send('livedata', value=head)
    sleep(3)                         



if __name__ == "__main__":
    main()

