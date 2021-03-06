"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from datetime import timedelta

from django.test import TestCase

from django.utils import timezone

from polls.models import Poll


class PollTest(TestCase):
    def setUp(self):
        self.expected_question = "what is the question?"
        self.expected_choice = "do you like spongecake?"
        self.poll = Poll.objects.create(
            question=self.expected_question,
            pub_date=timezone.now())
        self.choice = self.poll.choice_set.create(
            choice=self.expected_choice)
    
    def test_poll_display(self):
        self.assertEqual(unicode(self.poll), self.expected_question, "check initial question")
        new_question = "what is the answer?"
        self.poll.question = new_question
        self.assertEqual(unicode(self.poll), new_question, "Check new question")
    
    def test_choice_display(self):
        self.assertEquals(unicode(self.choice), self.expected_choice)
        new_choice = "is left better than right?"
        self.choice.choice = new_choice
        self.assertEquals(unicode(self.choice), new_choice)

    def test_published_today(self):
        self.assertTrue(self.poll.published_today())
        delta = timedelta(hours=26)
        self.poll.pub_date = self.poll.pub_date - delta
        self.assertFalse(self.poll.published_today())

