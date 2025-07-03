from databricks.connect import DatabricksSession
from pyspark.sql.types import *
from datetime import date

# This example uses databricks-connect, which reads credentials from your local Databricks CLI profile.
# Make sure you have run the OAuth login and set up your profile with the Databricks CLI.
# To use a specific profile, use: DatabricksSession.builder.profile("<profile-name>").getOrCreate()

print("\n🚀 Connecting to Databricks Serverless using local CLI profile...")
# Create a DatabricksSession using local CLI profile
spark = DatabricksSession.builder.serverless().getOrCreate()

print("\n📦 Creating a DataFrame with airport temperature data...")
# Create a Spark DataFrame consisting of high and low temperatures by airport code and date.
schema = StructType([
    StructField('AirportCode', StringType(), False),
    StructField('Date', DateType(), False),
    StructField('TempHighF', IntegerType(), False),
    StructField('TempLowF', IntegerType(), False)
])

data = [
    ['BLI', date(2021, 4, 3), 52, 43],
    ['BLI', date(2021, 4, 2), 50, 38],
    ['BLI', date(2021, 4, 1), 52, 41],
    ['PDX', date(2021, 4, 3), 64, 45],
    ['PDX', date(2021, 4, 2), 61, 41],
    ['PDX', date(2021, 4, 1), 66, 39],
    ['SEA', date(2021, 4, 3), 57, 43],
    ['SEA', date(2021, 4, 2), 54, 39],
    ['SEA', date(2021, 4, 1), 56, 41]
]

temps = spark.createDataFrame(data, schema)
print("\n🖨️ Showing the DataFrame:")
temps.show()

print("\n🗄️ Writing the DataFrame to a Databricks table: 'zzz_demo_temps_table'...")
# Create a table on the Databricks cluster and then fill the table with the DataFrame's contents.
spark.sql('USE default')
spark.sql('DROP TABLE IF EXISTS zzz_demo_temps_table')
temps.write.saveAsTable('zzz_demo_temps_table')

print("\n🔎 Querying the table for non-BLI airports after 2021-04-01, grouped and ordered by high temperature:")
# Query the table on the Databricks cluster, returning rows where the airport code is not BLI and the date is later than 2021-04-01.
df_temps = spark.sql("""
    SELECT * FROM zzz_demo_temps_table
    WHERE AirportCode != 'BLI' AND Date > '2021-04-01'
    GROUP BY AirportCode, Date, TempHighF, TempLowF
    ORDER BY TempHighF DESC
""")
df_temps.show()

print("\n🧹 Cleaning up: dropping the table 'zzz_demo_temps_table'...")
# Clean up by deleting the table from the Databricks cluster.
spark.sql('DROP TABLE zzz_demo_temps_table')

print("\n✅ Example complete! Stopping Spark session.\n")
# Stop the Spark session
# spark.stop() 