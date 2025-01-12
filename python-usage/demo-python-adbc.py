import adbc_driver_manager
import adbc_driver_flightsql
import adbc_driver_flightsql.dbapi as flight_sql

print(adbc_driver_manager.__version__)
print(adbc_driver_flightsql.__version__)

conn = flight_sql.connect(uri="grpc://localhost:9090", db_kwargs={
            adbc_driver_manager.DatabaseOptions.USERNAME.value: "root",
            adbc_driver_manager.DatabaseOptions.PASSWORD.value: "",
        })
cursor = conn.cursor()

cursor.execute("use demo;")
print(cursor.fetchallarrow().to_pandas())
cursor.execute("select * from mytable limit 10;")
print(cursor.fetchallarrow().to_pandas())

# cursor.execute("DROP DATABASE IF EXISTS arrow_flight_sql FORCE;")
# print(cursor.fetchallarrow().to_pandas())

# cursor.execute("create database arrow_flight_sql;")
# print(cursor.fetchallarrow().to_pandas())

# cursor.execute("show databases;")
# print(cursor.fetchallarrow().to_pandas())

# cursor.execute("use arrow_flight_sql;")
# print(cursor.fetchallarrow().to_pandas())

# cursor.execute("""CREATE TABLE arrow_flight_sql_test
#     (
#         k0 INT,
#         k1 DOUBLE,
#         K2 varchar(32) NULL DEFAULT "" COMMENT "",
#         k3 DECIMAL(27,9) DEFAULT "0",
#         k4 BIGINT NULL DEFAULT '10',
#         k5 DATE,
#     )
#     DISTRIBUTED BY HASH(k5) BUCKETS 5
#     PROPERTIES("replication_num" = "1");""")
# print(cursor.fetchallarrow().to_pandas())

# cursor.execute("show create table arrow_flight_sql_test;")
# print(cursor.fetchallarrow().to_pandas())

cursor.execute("use demo;")
print(cursor.fetchallarrow().to_pandas())
cursor.execute("select * from mytable limit 10;")
print(cursor.fetchallarrow().to_pandas())
