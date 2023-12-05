import pymysql
USERNAME = 'admin' # Replace with your master username
PASSWORD = 'chessdata' # Replace with your RDS instance password
ENDPOINT = "database-1.cj0pkahttugp.us-west-1.rds.amazonaws.com" 
PORT = 3306 # Replace with instance port
REGION = "us-west-1" # Replace with your AWS region
DBNAME = 'OpeningsData' # Replace with the name of your SCHEMA in MySQL workbench
SSL_CA = "ssl/rds-combined-ca-bundle.pem" # Replace with folder location of SSL bundle
CURSORCLASS = pymysql.cursors.DictCursor # NO NEED to modify this
