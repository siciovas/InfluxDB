from datetime import datetime
import os
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS, ASYNCHRONOUS
from datetime import datetime
import csv

class InfluxClient:
    def __init__(self,token,org,bucket): 
        self._org=org 
        self._bucket = bucket
        self._client = InfluxDBClient(url="http://localhost:8086", token=token)

    # def write_data(self,data,write_option=SYNCHRONOUS):
    #     write_api = self._client.write_api(write_option)
    #     write_api.write(self._bucket, self._org , data,write_precision='s')

    def query_data(self,query):
        query_api = self._client.query_api()
        result = query_api.query(org=self._org, query=query)
        results = []
        for table in result:
            for record in table.records:
                results.append((record.get_value(), record.get_field()))
        print(results)
        return results 
    
    # def delete_data(self,measurement):
    #     delete_api = self._client.delete_api()
    #     start = "1970-01-01T00:00:00Z"
    #     stop = "2021-10-30T00:00:00Z"
    #     delete_api.delete(start, stop, f'_measurement="{measurement}"', bucket=self._bucket, org=self._org)

token = "PojpZWMCsnWL-pVgQBG3b5EiY1jdnCXGVWxqwYoPRdgceAJTMRT0KDYnCVfvAAidXgpJTNOMFGNtW_CZWHJ-eg=="
org = "KTU"
bucket = "DB1"
IC = InfluxClient(token,org,bucket)

query1 = 'from(bucket: "DB1")\
|> range(start: 2022-09-01T23:30:00Z, stop: 2022-11-20T00:00:00Z)\
|> filter(fn: (r) => r._measurement == "komanda2")\
|> filter(fn: (r) => r.id == "61")'

IC.query_data(query1)


