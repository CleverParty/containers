from time import sleep
from json import dumps
import datetime
import pandas 
from kafka import KafkaConsumer
import tickerScanner as ticker

def main():
    consumer = KafkaConsumer(
        'livedata',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group')
    start = datetime.datetime(2020,8,1)
    end = datetime.datetime.today()
    # print(client.company_profile(cusip='679295105'))
    for msg in consumer:
        print (msg)

if __name__ == "__main__":
    main()