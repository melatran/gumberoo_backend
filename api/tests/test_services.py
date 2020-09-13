import json
import os
import requests
from django.test import SimpleTestCase, TestCase
from ibm_watson import ToneAnalyzerV3
from .. import watson_service
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

class AnalyzeToneWatson(TestCase):
  def test_analyze_tone_of_text(self):
    mood_text = "I'm so ready for vacation"
    expected = {'document_tones': ['joy']}
    
    self.assertEqual(watson_service.analyze_tone(mood_text), expected)
