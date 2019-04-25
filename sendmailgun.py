import requests

baseurl = 'https://api.mailgun.net/v3/mailgun.example.com/messages'

emailauth = ('api', 'YOUR MAILGUN API KEY')

emailfrom = 'John Smith <johnsmith@example.com>'

emailsubject = 'YOUR SUBJECT'

emailtext = """
YOUR TEXT
 """

with open('file.txt') as f:
    for line in f:

        emaildata = {
            'from': emailfrom,
            'to': line.rstrip(),
            'subject': emailsubject,
            'text': emailtext
            }

        requests.post(baseurl, data=emaildata, auth=emailauth)