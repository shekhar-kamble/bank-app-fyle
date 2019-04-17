import time
import unittest
import ast
from app import create_app, db
from app.models import Bank_Branches


class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        # db.drop_all()
        self.app_context.pop()

    def test_search_by_ifsc(self):
        ifsc_code = "ABHY0065305"
        result = Bank_Branches.search_by_ifsc(ifsc_code)
        ex_result = {"ifsc_code":"ABHY0065305","bank_name":"ABHYUDAYA COOPERATIVE BANK LIMITED",
             "branch":"PADUBIDRI", "address":"SHRI SHAKTHI COMPLEX, NH-66, NADSAL VILLAGE, PADUBIDRI, UDUPI-DIST, 574111", 
             "city":"UDUPI", "district":"DAKSHINA KANNADA", "state":"KARNATAKA"}
        result = ast.literal_eval(str(result))
        self.assertDictEqual(result,ex_result)
    
    def test_search_bank(self):
        bank_name = "ALLAHABAD BANK"
        city = "DHANBAD"
        result = Bank_Branches.search(bank_name=bank_name,city=city)
        result = ast.literal_eval(str(result))
        print result
        self.assertTrue(len(result)>0)