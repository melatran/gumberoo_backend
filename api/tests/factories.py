import factory
from .. import models

class TeacherFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = models.Teacher

  first_name = factory.Sequence(lambda n: 'Teacher%dFirst' % n)
  last_name = factory.Sequence(lambda n: 'Teacher%dLast' % n)