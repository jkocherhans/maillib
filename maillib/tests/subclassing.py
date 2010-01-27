from maillib import Message
from StringIO import StringIO
import unittest
import email


RAW_MESSAGE = """\
Date: Sun, 25 Oct 2009 20:27:58 -0500
Subject: Test
From: Joseph Kocherhans <jkocherhans@gmail.com>
To: Joseph Kocherhans <jkocherhans@gmail.com>

Test.

"""

class TestMessage(Message):
    pass

class ConstructorsTestCase(unittest.TestCase):
    """
    Make sure the constructors work for subclasses.
    """
    def test_from_file(self):
        msg = TestMessage.from_file(StringIO(RAW_MESSAGE))
        self.assertTrue(isinstance(msg, TestMessage))

    def test_from_string(self):
        msg = TestMessage.from_string(RAW_MESSAGE)
        self.assertTrue(isinstance(msg, TestMessage))

    def test_from_message(self):
        msg = TestMessage.from_message(email.message_from_string(RAW_MESSAGE))
        self.assertTrue(isinstance(msg, TestMessage))

