import unittest
import maillib

class BasicTests(unittest.TestCase):
    def test_body(self):
        msg = maillib.Message.from_string(RAW_MESSAGE)
        self.assertEqual(msg.body, u'test\n')

    def test_html(self):
        msg = maillib.Message.from_string(RAW_MESSAGE)
        self.assertEqual(msg.html, u'test\n')

    def test_header(self):
        msg = maillib.Message.from_string(RAW_MESSAGE)
        self.assertEqual(msg.subject, u'test')

RAW_MESSAGE = """\
MIME-Version: 1.0
Received: by 10.142.223.2 with HTTP; Mon, 2 Mar 2009 20:00:55 -0800 (PST)
Date: Mon, 2 Mar 2009 22:00:55 -0600
Delivered-To: jkocherhans@gmail.com
Message-ID: <c90890f0903022000g7ddb0965i2360bcbeda6c8e23@mail.gmail.com>
Subject: test
From: Joseph Kocherhans <jkocherhans@gmail.com>
To: joseph@jkocherhans.com
Content-Type: multipart/alternative; boundary=00032556403a5fd82604642efb44

--00032556403a5fd82604642efb44
Content-Type: text/plain; charset=ISO-8859-1
Content-Transfer-Encoding: 7bit

test

--00032556403a5fd82604642efb44
Content-Type: text/html; charset=ISO-8859-1
Content-Transfer-Encoding: 7bit

test

--00032556403a5fd82604642efb44--
"""

if __name__ == '__main__':
    unittest.main()
