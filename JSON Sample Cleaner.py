'''
File for testing means to delete files and also clean up files made while learning code
'''

import os

if os.path.exists("sample1.json"):
  os.remove("sample1.json")
  print("sample1.json deleted")

if os.path.exists("sample2.json"):
  os.remove("sample2.json")
  print("sample2.json deleted")

if os.path.exists("sample3.json"):
  os.remove("sample3.json")
  print("sample3.json deleted")

if os.path.exists("test1.json"):
  os.remove("test1.json")
  print("test1.json deleted")