from maillib import Message
import unittest


RAW_MESSAGE = """\
Return-path: <jkocherhans@gmail.com>
MIME-version: 1.0
In-reply-to: <AEA56661-72EA-41B0-8666-365317DA3DD2@mac.com>
References: <529C86BD-3F27-44E2-9B73-2E6B73619A3D@mac.com>
 <c90890f0910251824p435ede4eo13274af33473ea6e@mail.gmail.com>
 <AEA56661-72EA-41B0-8666-365317DA3DD2@mac.com>
Date: Sun, 25 Oct 2009 20:27:58 -0500
Message-id: <c90890f0910251827l227227cvae7a6bd44858dd94@mail.gmail.com>
Subject: Re: Thread
From: Joseph Kocherhans <jkocherhans@gmail.com>
To: Joseph Kocherhans <jkocherhans@mac.com>
Content-type: text/plain; charset=UTF-8

Reply to third message.

On Sun, Oct 25, 2009 at 8:26 PM, Joseph Kocherhans <jkocherhans@mac.com> wrote:
> Reply to second message.
>
> On Oct 25, 2009, at 8:24 PM, Joseph Kocherhans wrote:
>
>> Reply to first message.
>>
>> On Sun, Oct 25, 2009 at 8:23 PM, Joseph Kocherhans <jkocherhans@mac.com>
>> wrote:
>>>
>>> First message
>
>

"""

class ReferencesTestCase(unittest.TestCase):
    def setUp(self):
        self.msg = Message.from_string(RAW_MESSAGE)

    def test_subject(self):
        self.assertEqual(self.msg.references, [
            '<529C86BD-3F27-44E2-9B73-2E6B73619A3D@mac.com>',
            '<c90890f0910251824p435ede4eo13274af33473ea6e@mail.gmail.com>',
            '<AEA56661-72EA-41B0-8666-365317DA3DD2@mac.com>',
            '<AEA56661-72EA-41B0-8666-365317DA3DD2@mac.com>'
        ])

if __name__ == '__main__':
    unittest.main()

