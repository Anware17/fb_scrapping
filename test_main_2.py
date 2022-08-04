# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 23:43:01 2022

@author: anwar
"""

from fastapi.testclient import TestClient
import requests
from main import app

client = TestClient(app)


def test_scrapping():
    response = client.get("/scrap/pythonprogramming.net")
    assert response.status_code == 200

