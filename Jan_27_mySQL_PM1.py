import MySQLdb

db = MySQLdb.connect(host="94.250.236.149", user ="sscb", passwd = "Tc8FsnKf43nEMnFM", db = "sscb", port = "3306")

cur = db.cursor()
cur.execute("SELECT * FROM campaign")