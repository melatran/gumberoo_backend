import numpy as np
import scipy.stats as stats

class StudentScore:
  def __init__(self, student_id, average_score):
    self.student_id = student_id
    self.average_score = average_score

class LessonScore:
  def __init__(self, lesson_id, average_score):
    self.lesson_id = lesson_id
    self.average_score = average_score

class ZScore:
  def __init__(self, student_id, zscore):
    self.student_id = student_id
    self.zscore = zscore

class ZScoreGenerator:
  def __init__(self, lesson_students):
    self.lesson_students = lesson_students

  def generate_zscore(self):
    scores = {}
    for lesson_student in self.lesson_students:
      scores[lesson_student.student_id] = lesson_student.score

    keys, vals = zip(*scores.items())
    zscore = stats.zscore(vals)
    new_scores = dict(zip(keys, zscore))

    zscores = []
    for student_id, score in new_scores.items():
      zscores.append(ZScore(student_id=student_id, zscore=score))
    
    return zscores
