from django.test import TestCase
from user.models.user import Usuario
from ..models import Tweet  # Ajuste o caminho se necessário

class TweetModelTest(TestCase):

    def setUp(self):
        self.user = Usuario.objects.create_user(username='user', password='password', first_name='User', last_name='Test')
        self.tweet = Tweet.objects.create(author=self.user, content='This is a test tweet')

    def test_tweet_creation(self):
        self.assertEqual(self.tweet.author.username, 'user')
        self.assertEqual(self.tweet.content, 'This is a test tweet')
        self.assertTrue(self.tweet.created_at)

    def test_tweet_str_method(self):
        self.assertEqual(str(self.tweet), 'user: This is a test tweet')