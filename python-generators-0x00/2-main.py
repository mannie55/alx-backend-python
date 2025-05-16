#!/usr/bin/python3
import sys


processing = __import__('1-batch_processing')

##### print processed users in a batch of 50
try:
    user = processing.batch_processing(50)
    print(user)
except BrokenPipeError:
    sys.stderr.close()
