from django.test import TestCase
from django.contrib.auth import get_user_model

Usuario = get_user_model()

class UsuarioModelTest(TestCase):

    def setUp(self):
        self.user1 = Usuario.objects.create_user(username='user1', password='password1', first_name='User', last_name='One')
        self.user2 = Usuario.objects.create_user(username='user2', password='password2', first_name='User', last_name='Two')

    def test_user_creation(self):
        self.assertEqual(self.user1.username, 'user1')
        self.assertEqual(self.user1.first_name, 'User')
        self.assertEqual(self.user1.last_name, 'One')
        
    def test_follow_user(self):
        self.user1.follow(self.user2)
        self.assertIn(self.user2, self.user1.following.all())
        self.assertIn(self.user1, self.user2.followers.all())

    def test_unfollow_user(self):
        self.user1.follow(self.user2)
        self.user1.unfollow(self.user2)
        self.assertNotIn(self.user2, self.user1.following.all())
        self.assertNotIn(self.user1, self.user2.followers.all())