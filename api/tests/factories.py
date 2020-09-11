import factory
from faker.factory import Factory
Faker = Factory.create
fake = Faker()
fake.seed(0)

from .. import models

class TeacherFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = models.Teacher

  first_name = factory.Sequence(lambda n: 'teacher%dFirst' % n)
  last_name = factory.Sequence(lambda n: 'teacher%dLast' % n)

class StudentFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = models.Student

  first_name = factory.Sequence(lambda n: 'student%dFirst' % n)
  last_name = factory.Sequence(lambda n: 'student%dLast' % n)
  teacher = factory.SubFactory(TeacherFactory)

