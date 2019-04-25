#!/usr/bin/python3

import requests
import csv

baseurl = 'https://api.mailgun.net/v2/mailgun.example.com/messages'

auth = ('api', 'YOUR MAILGUN API KEY')

emailfrom = 'John Smith <johnsmith@example.com>'

emailsubject = 'YOUR SUBJECT'

emailtext = """
YOUR TEXT
 """

with open('file.txt') as f:
    for line in f:

    
    data = {
        'from': emailfrom,
        'to': line,
        'subject': emailsubject,
        'text': emailtext
        }

    print(data)