import json
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(
    'C5A_uO1F6b3ncrvWf5uSmR0wwrAJhrGN2LxfgICO5udJ')
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    authenticator=authenticator
)

tone_analyzer.set_service_url(
    'https://api.us-south.tone-analyzer.watson.cloud.ibm.com/instances/bbe286c2-3d3c-4fdc-ae5e-89f0419c10cb')

text = 'I cried a lot during this test'

tone_analysis = tone_analyzer.tone(
    {'text': text},
    content_type='application/json'
).get_result()
print(json.dumps(tone_analysis, indent=2))
