from django.test import TestCase
from api.popos import LessonScore, StudentScore, ZScoreGenerator, ZScore

class PopoTest(TestCase):
  def setUp(self):
    self.student_score = StudentScore(student_id=1, average_score=80)
    self.lesson_score = LessonScore(lesson_id=1, average_score=73)
    self.zscore = ZScore(student_id=1, zscore=.45454)
    self.zscore_generator = ZScoreGenerator(lesson_students=[1, 2, 3])

  def test_it_exists(self):
    self.assertIsInstance(self.student_score, StudentScore)
    self.assertIsInstance(self.lesson_score, LessonScore)
    self.assertIsInstance(self.zscore, ZScore)
    self.assertIsInstance(self.zscore_generator, ZScoreGenerator)

  def test_attributes(self):
    self.assertEqual(self.student_score.student_id, 1)
    self.assertEqual(self.student_score.average_score, 80)

    self.assertEqual(self.lesson_score.lesson_id, 1)
    self.assertEqual(self.lesson_score.average_score, 73)

    self.assertEqual(self.zscore.student_id, 1)
    self.assertEqual(self.zscore.zscore, .45454)

    self.assertEqual(self.zscore_generator.lesson_students, [1, 2, 3])