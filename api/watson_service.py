import json
import os
import requests
from dotenv import load_dotenv, find_dotenv
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv(find_dotenv())

tone_analyzer_authenticator = IAMAuthenticator(os.environ.get('WATSON_APIKEY'))
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    authenticator=tone_analyzer_authenticator)

tone_analyzer.set_service_url(
    'https://api.us-south.tone-analyzer.watson.cloud.ibm.com/instances/bbe286c2-3d3c-4fdc-ae5e-89f0419c10cb')

text = 'I cried a lot during this test'

tone_analysis = tone_analyzer.tone(
    {'text': text},
    content_type='application/json'
).get_result()
print(json.dumps(tone_analysis, indent=2))
