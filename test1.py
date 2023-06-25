import unittest
from fake_fetch import FakeFetch

tc = unittest.TestCase()
fetcher = FakeFetch()

res = fetcher.fetch('http://fakeurl/homeassignment/banana')
tc.assertEqual(res['data'][-1]["PRODUCT_NAME"],'BLUE')

res = fetcher.fetch('http://fakeurl/homeassignment/strawberry')
tc.assertEqual(res['data'][0]["CREATED_ERROR_CODE"],101)

res = fetcher.fetch('http://fakeurl/homeassignment/other')
tc.assertNotIn('data',res)

print("SUCCESS")