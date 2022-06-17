import GuiDBConfig as guiConf
import mysql.connector
conn = mysql.connector.connect(**guiConf.dbConfig)  
print(conn)
