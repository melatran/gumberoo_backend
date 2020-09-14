import json
import os
import requests
from dotenv import load_dotenv, find_dotenv
from django.http import JsonResponse
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
load_dotenv(find_dotenv())

def analyze_tone(mood_text):
  authenticator = IAMAuthenticator(os.getenv("WATSON_APIKEY"))
  tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    authenticator=authenticator)

  tone_analyzer.set_service_url(
    'https://api.us-south.tone-analyzer.watson.cloud.ibm.com/instances/bbe286c2-3d3c-4fdc-ae5e-89f0419c10cb')

  result = tone_analyzer.tone(
            {'text': mood_text},
              content_type='application/json',
          ).get_result()
  
  raw_watson_response = result['document_tone']['tones'][0]
  watson_result = raw_watson_response['tone_name']

  return watson_result
