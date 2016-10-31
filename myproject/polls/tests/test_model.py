from django.test import TestCase
import pytest


class TestCustomer:
    def test_http_response(self, client):
        response = client.get('/detail')
        assert response.status_code == 404, "status code successfull"
