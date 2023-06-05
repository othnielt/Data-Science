import psycopg2



conn = psycopg2.connect(
    host="localhost", #host name 
    port=54327,   #insert  port 
    database="csi4142",  #insert your database 
    user="", #insert your username 
    password=""
)

cur = conn.cursor()

# Create the table
try:
    

    cur = conn.cursor()

    # Create the table
    cur.execute('''
    CREATE TABLE data (
        id SERIAL PRIMARY KEY,
        "Surrogate Keys" VARCHAR(255),
        "date" DATE,
        "health_region" VARCHAR(255),
        "age_group" VARCHAR(255),
        "gender" VARCHAR(255),
        "exposure" VARCHAR(255),
        "case_status" VARCHAR(255),
        "province" VARCHAR(255),
        "Confirmed_Cases" BIGINT,
        "Deaths" BIGINT,
        "Total_Cases" BIGINT,
        "vaccine_administered" FLOAT,
        "testing" BIGINT,
        "Test_positivity_rate" FLOAT,
        "vaccination_rate" FLOAT,
        "Total_fatalities" BIGINT,
        "Total_recorded_cases" BIGINT
    )
''')




    conn.commit()

except Exception as e:
    print(e)

finally:
    cur.close()
    conn.close()
