from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
token = "PojpZWMCsnWL-pVgQBG3b5EiY1jdnCXGVWxqwYoPRdgceAJTMRT0KDYnCVfvAAidXgpJTNOMFGNtW_CZWHJ-eg=="
org = "KTU"
bucket = "DB22"

with InfluxDBClient(url="http://localhost:8086", token=token, org=org) as client:
    write_api = client.write_api(write_options=SYNCHRONOUS)
    point = Point("statistika") \
    .tag("Taskai", "72") \
    .tag("Prazangos", "25") \
    .tag("Pataikyta_tritaskiu", "10") \
    .tag("Pataikyta_dvitaskiu", "13") \
    .tag("Pataikyta_baudu", "16") \
    .tag("Atkovoti_kamuoliai", "27") \
    .tag("Perimti_kamuoliai", "5") \
    .tag("id", "556") \
    .tag("id_komanda", "75") \
    .tag("id_rungtynes", "518") \
    .field("field1", 556) \
    .time(datetime.utcnow(), WritePrecision.NS)

    write_api.write(bucket, org, point)
