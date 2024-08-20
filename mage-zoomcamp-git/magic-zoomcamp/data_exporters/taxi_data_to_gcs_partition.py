import pyarrow as pa
import pyarrow.parquet as pq
import os


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

# MANUALLY DEFINE THE CREDENTIALS
# Set the environment variable to the location of the mounted key. json
# This will tell pyarrow where our credentials are
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/dtc-de-429610-177e72bd9e67.json"

# Define the bucket, project, and table  
bucket_name = 'mage-zoomcamp-juju-1'
project_id = 'dtc-de-429610'
table_name = 'ny_taxi_data'          

root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data(data, *args, **kwargs):
    # define the column to partition on 
    # create a date column from the timestamp so that we can partition on date
    data['tpep_pickup_date'] = data['tpep_pickup_datetime'].dt.date

    # define the pyarrow table and read the df into it
    table = pa.Table.from_pandas(data)

    # define file system - the google cloud object that is going to authorize using the environmental variable automatically
    gcs = pa.fs.GcsFileSystem()

    # write to the dataset using a parquet function
    pq.write_to_dataset(
        table, 
        root_path=root_path, 
        partition_cols=['tpep_pickup_date'], # needs to be a list
        filesystem=gcs
    )