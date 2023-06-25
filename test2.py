import unittest
from database import DataBase

tc = unittest.TestCase()
db = DataBase()
db.refresh()
res = db.filter({"Provider":6111, "STATUS": "Open"})
tc.assertEqual(res["data"][0]['Products Affected'],{'BLUE', 'ORANGE'})

print("SUCCESS")