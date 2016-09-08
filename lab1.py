# -*- coding: utf-8 -*-
import requests

response = requests.get("https://raw.githubusercontent.com/palmpilot71/CMPUT404Lab1/master/lab1.py")

print response.text
