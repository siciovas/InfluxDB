from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
token = "PojpZWMCsnWL-pVgQBG3b5EiY1jdnCXGVWxqwYoPRdgceAJTMRT0KDYnCVfvAAidXgpJTNOMFGNtW_CZWHJ-eg=="
org = "KTU"
bucket = "DB1"

with InfluxDBClient(url="http://localhost:8086", token=token, org=org) as client:
    write_api = client.write_api(write_options=SYNCHRONOUS)
    point = Point("testDelete") \
    .tag("id", "65") \
    .field("Id", 65) \
    .tag("pavadinimas", "Siauliai")    \
    .field("Pavadinimas", "Siauliai")    \
    .tag("spalvos", "Geltona, juoda")    \
    .field("Spalvos", "Geltona, juoda")    \
    .tag("titulai", "9")    \
    .field("Titulai", "9")    \
    .tag("ikurimas", "1986-01-01")    \
    .field("Ikurimas", "1986-01-01")    \
    .tag("id_miestas", "24")    \
    .field("id_miestas", "24")    \
    .time(datetime.utcnow(), WritePrecision.NS)

    write_api.write(bucket, org, point)
