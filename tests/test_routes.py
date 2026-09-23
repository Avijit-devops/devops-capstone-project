"""
Test cases for Account REST API Service
"""
import unittest
from service import app
from service.models import accounts_db


class TestAccountService(unittest.TestCase):
    """Account Service Tests"""

    def setUp(self):
        """Set up test environment"""
        self.client = app.test_client()
        accounts_db.clear()

    def test_index(self):
        """It should return the home page"""
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(data["name"], "Account REST API Service")

    def test_security_headers(self):
        """It should return security headers"""
        resp = self.client.get("/")
        self.assertIn("X-Content-Type-Options", resp.headers)
        self.assertIn("X-Frame-Options", resp.headers)

    def test_cors_headers(self):
        """It should return a CORS header"""
        resp = self.client.get("/")
        self.assertIn("Access-Control-Allow-Origin", resp.headers)

    def test_crud_flow(self):
        """It should perform full CRUD operations"""
        payload = {
            "name": "John Doe",
            "email": "john@example.com",
            "address": "123 Main Street",
            "phone_number": "555-1234",
            "date_joined": "2026-09-23"
        }
        res = self.client.post("/accounts", json=payload)
        self.assertEqual(res.status_code, 201)
        acc_id = res.get_json()["id"]

        res = self.client.get(f"/accounts/{acc_id}")
        self.assertEqual(res.status_code, 200)

        res = self.client.get("/accounts")
        self.assertEqual(len(res.get_json()), 1)

        update_payload = {"name": "John Updated"}
        res = self.client.put(f"/accounts/{acc_id}", json=update_payload)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()["name"], "John Updated")

        res = self.client.delete(f"/accounts/{acc_id}")
        self.assertEqual(res.status_code, 204)

        res = self.client.get(f"/accounts/{acc_id}")
        self.assertEqual(res.status_code, 404)


if __name__ == "__main__":
    unittest.main()
