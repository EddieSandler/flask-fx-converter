from unittest import TestCase
from app import app
from flask import session


class FlaskTests(TestCase):
    def test_FX_converter(self):
        with app.test_client() as client:
            res=client.get('/')


            self.assertEqual("success","true")

            return res

