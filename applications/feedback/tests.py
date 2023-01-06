from django.test import TestCase
import unittest

from applications.feedback.views import LikeAPIView, RatingAPIView

class TestLike(unittest.TestCase):

    def setUp(self):
        self.like = LikeAPIView()

    def 
