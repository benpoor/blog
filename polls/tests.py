import datetime
from django.test import TestCase
from django.utils import timezone

from polls.models import Poll

# Create your tests here.

class PollMethodTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question=Poll(pub_date=time)
        self.assertEqual(future_question.was_publish(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now()-datetime.timedelta(days=30)
        old_question = Poll(pub_date=time)
        self.assertEqual(old_question.was_publish(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now()-datetime.timedelta(hours=1)
        recent_question = Poll(pub_date=time)
        self.assertEqual(recent_question.was_publish(), True)
