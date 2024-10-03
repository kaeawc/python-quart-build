import unittest
from src.main import app


class StatusEndpointTestCase(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.app = app.test_client()

    async def test_status_endpoint(self):
        response = await self.app.get("/status")

        self.assertEqual(response.status_code, 200)

        response_data = await response.get_json()

        # Check the structure of the response
        self.assertIn("status", response_data)
        self.assertIn("message", response_data)

        # Verify the values
        self.assertEqual(response_data["status"], "OK")
        self.assertEqual(
            response_data["message"], "The application is running smoothly"
        )


if __name__ == "__main__":
    unittest.main()
