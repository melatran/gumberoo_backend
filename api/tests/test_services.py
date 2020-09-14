# import json
# import os
# import requests
# from django.test import SimpleTestCase, TestCase
# from ibm_watson import ToneAnalyzerV3
# from .. import watson_service
# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv())

# class AnalyzeToneWatson(TestCase):
#   def test_analyze_tone_of_text(self):
#     mood_text = "I'm so ready for vacation"
#     expected = 'Joy'
#     self.assertEqual(watson_service.analyze_tone(mood_text), expected)

#   def test_analyze_sentences(self):
#     mood_text = "This was so hard. I am going to cry."
#     expected = 'Sadness'
#     self.assertEqual(watson_service.analyze_tone(mood_text), expected)
  
#   def test_analyze_overall_mood_with_two_conflicting_sentences(self):
#     mood_text = "I am going to cry but I'm happy it's over"
#     expected = 'Sadness'
#     self.assertEqual(watson_service.analyze_tone(mood_text), expected)

#   def test_analyze_mood_with_spelling_mistakes(self):
#     mood_text = "I'm ready for vacashion"
#     expected = 'Joy'
#     self.assertEqual(watson_service.analyze_tone(mood_text), expected)
