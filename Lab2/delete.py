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
    def delete_data(self,measurement):
            delete_api = self._client.delete_api()
            start = "2022-09-01T23:30:00Z"
            stop = "2022-11-14T00:00:00Z"
            delete_api.delete(start, stop, f'_measurement="{measurement}"', bucket=self._bucket, org=self._org)

token = "PojpZWMCsnWL-pVgQBG3b5EiY1jdnCXGVWxqwYoPRdgceAJTMRT0KDYnCVfvAAidXgpJTNOMFGNtW_CZWHJ-eg=="
org = "KTU"
bucket = "DB22"
IC = InfluxClient(token,org,bucket)


IC.delete_data("test")
