from peewee import PostgresqlDatabase
__dbUsername = 'postgres'
__dbPassword = "1"
__dbName = "test_orm"
__dbHost = "localhost"
__dbPort = 5432
db = PostgresqlDatabase(__dbName,host=__dbHost,port=__dbPort,user=__dbUsername,password=__dbPassword)