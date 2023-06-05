import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost", #host name 
    port=54327,   #insert  port 
    database="csi4142",  #insert your database 
    user="othnieltiendrbeogo", #insert your username 
    password=""
)

cur = conn.cursor()

# Create the table
try:
    with open('DataStagingDataset.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)  # skip the header row
        for row in reader:
            # Extract the values from the row
            id, surrogate_keys, date, health_region, age_group, gender, exposure, case_status, province, confirmed_cases, deaths, total_cases, vaccine_administered, testing, test_positivity_rate, vaccination_rate, total_fatalities, total_recorded_cases = row

            # Insert the values into the table
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO data (id, "Surrogate Keys", "date", "health_region", "age_group", "gender", "exposure", "case_status", "province", "Confirmed_Cases", "Deaths", "Total_Cases", "vaccine_administered", "testing", "Test_positivity_rate", "vaccination_rate", "Total_fatalities", "Total_recorded_cases")
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (id, surrogate_keys, date, health_region, age_group, gender, exposure, case_status, province, confirmed_cases, deaths, total_cases, vaccine_administered, testing, test_positivity_rate, vaccination_rate, total_fatalities, total_recorded_cases))

            conn.commit()

except Exception as e:
    print(e)

finally:
    conn.close()
