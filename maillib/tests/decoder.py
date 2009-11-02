# -*- coding: utf-8 -*-
import email
import datetime
from maillib import Message, MessageDecoder
import unittest


BASIC_MESSAGE = """\
From: Sender <sender@example.com>
Content-type: text/plain; charset=us-ascii; format=flowed
Content-transfer-encoding: 7bit
Subject: Test
Date: Sat, 17 Oct 2009 19:05:20 -0500
Message-id: <FF8428AD-ABD8-41C7-ACBB-D4DAF26662F2@example.com>
To: Recipient <recipient@example.com>
Cc: CC One <cc.1@example.com>,
 CC Two <cc.2@example.com>

Testing

"""

ENCODED_MESAGE = """\
Subject: =?utf-8?B?0JLQu9Cw0LTQuMyB0LzQuNGA?=
Content-Type: text/html;
	charset=utf-8
From: Sender <sender@example.com>
Date: Sun, 18 Oct 2009 19:24:11 -0500
Content-Transfer-Encoding: quoted-printable
Message-Id: <AA982891-D323-46D6-99C5-5F1E45DA929B@mac.com>
To: =?utf-8?B?0JLQu9Cw0LTQuMyB0LzQuNGAINCS0LvQsNC00LjMgdC80LjRgNC+?=
 =?utf-8?B?0LLQuNGHINCc0LDRj9C60L7MgdCy0YHQutC40Lk=?= <mayakovsky@example.com>

<html><head></head><body class=3D"ApplePlainTextBody" style=3D"word-wrap: =
break-word; -webkit-nbsp-mode: space; -webkit-line-break: =
after-white-space; ">=D0=92=D0=BB=D0=B0=D0=B4=D0=B8=CC=81=D0=BC=D0=B8=D1=80=
 =D0=92=D0=BB=D0=B0=D0=B4=D0=B8=CC=81=D0=BC=D0=B8=D1=80=D0=BE=D0=B2=D0=B8=D1=
=87 =D0=9C=D0=B0=D1=8F=D0=BA=D0=BE=CC=81=D0=B2=D1=81=D0=BA=D0=B8=D0=B9</bo=
dy></html>=
"""

class BasicDecoderTestCase(unittest.TestCase):
    def setUp(self):
        self.msg = email.message_from_string(BASIC_MESSAGE)
        self.decoder = MessageDecoder(self.msg)

    def test_subject(self):
        self.assertEqual(self.decoder['subject'], u'Test')
        self.assertEqual(self.decoder.get('subject'), u'Test')

class DecoderTestCase(unittest.TestCase):
    def setUp(self):
        self.msg = email.message_from_string(ENCODED_MESAGE)
        self.decoder = MessageDecoder(self.msg)

    def test_subject(self):
        self.assertEqual(self.decoder['subject'], u'Влади́мир')
        self.assertEqual(self.decoder.get('subject'), u'Влади́мир')

    def test_to(self):
        self.assertEqual(self.decoder['to'],
            (u'Влади́мир Влади́мирович Маяко́вский<mayakovsky@example.com>'))

class BasicMessageTestCase(unittest.TestCase):
    def setUp(self):
        self.msg = Message.from_string(BASIC_MESSAGE)

    def test_subject(self):
        self.assertEqual(self.msg.subject, u'Test')

    def test_sender(self):
        self.assertEqual(self.msg.sender, (u'Sender', u'sender@example.com'))

    def test_to(self):
        self.assertEqual(self.msg.to, [
            ('Recipient', 'recipient@example.com')
        ])

    def test_cc(self):
        self.assertEqual(self.msg.cc, [
            ('CC One', 'cc.1@example.com'),
            ('CC Two', 'cc.2@example.com')
        ])

    def test_date(self):
        self.assertEqual(self.msg.date, datetime.datetime(2009, 10, 18, 0, 5, 20))

    def test_body(self):
        self.assertEqual(self.msg.body, u'Testing\n\n')

    def test_headers(self):
        self.assertEqual(self.msg.headers['message-id'],
            u'<FF8428AD-ABD8-41C7-ACBB-D4DAF26662F2@example.com>')


class EncodedMessageTestCase(unittest.TestCase):
    def setUp(self):
        self.msg = Message.from_string(ENCODED_MESAGE)

    def test_subject(self):
        self.assertEqual(self.msg.subject, u'Влади́мир')

    def test_sender(self):
        self.assertEqual(self.msg.sender, (u'Sender', u'sender@example.com'))

    def test_to(self):
        self.assertEqual(self.msg.to, [
            (u'Влади́мир Влади́мирович Маяко́вский', u'mayakovsky@example.com')
        ])

    def test_body(self):
        self.assertEqual(self.msg.html, u'<html><head></head><body class="ApplePlainTextBody" style="word-wrap: break-word; -webkit-nbsp-mode: space; -webkit-line-break: after-white-space; ">Влади́мир Влади́мирович Маяко́вский</body></html>')

    def test_raw_headers(self):
        self.assertEqual(self.msg.raw_headers['subject'], '=?utf-8?B?0JLQu9Cw0LTQuMyB0LzQuNGA?=')

    def test_headers(self):
        self.assertEqual(self.msg.headers['subject'], u'Влади́мир')


if __name__ == '__main__':
    unittest.main()

