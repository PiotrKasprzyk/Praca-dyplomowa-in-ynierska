from flask_testing import TestCase
from flask import url_for
from app import app, db
from models import User
import unittest
from xmlrunner import XMLTestRunner

class TestAppEndpoints(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['JSON_AS_ASCII'] = False  
        return app

    def test_homepage(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Witamy w ZeusDAWCompany'.encode('utf-8'), response.data)

    def test_login_page(self):
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Login'.encode('utf-8'), response.data)

    def test_forum_page(self):
        response = self.client.get(url_for('forum'))
        self.assertEqual(response.status_code, 302)  
        self.assertIn('/login', response.location)

    def test_products_page(self):
        response = self.client.get(url_for('products'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Produkty spożywcze'.encode('utf-8'), response.data)

    def test_diets_page(self):
        response = self.client.get(url_for('diets'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Dieta'.encode('utf-8'), response.data)

    def test_exercises_page(self):
        response = self.client.get(url_for('exercises'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Ćwiczenia Fizyczne'.encode('utf-8'), response.data)

    def test_bmi_page(self):
        response = self.client.get(url_for('bmi'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Kalkulator BMI'.encode('utf-8'), response.data)

    def test_opinions_page(self):
        response = self.client.get(url_for('opinions'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Opinie'.encode('utf-8'), response.data)


if __name__ == '__main__':
    with open('test_report.xml', 'wb') as output:
        unittest.main(
            testRunner=XMLTestRunner(output=output),
            verbosity=2
        )

