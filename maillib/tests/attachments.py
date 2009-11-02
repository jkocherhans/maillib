from maillib import Message
import unittest

RAW_MESSAGE = """\
Return-path: <jkocherhans@gmail.com>
Received: from smtpin132-bge351000 ([10.150.68.132])
 by ms041.mac.com (Sun Java(tm) System Messaging Server 6.3-7.04 (built Sep 26
 2008; 64bit)) with ESMTP id <0KRV00HDRSA264C0@ms041.mac.com> for
 jkocherhans@mac.com; Wed, 21 Oct 2009 13:15:38 -0700 (PDT)
Original-recipient: rfc822;jkocherhans@mac.com
Received: from mail-yx0-f185.google.com ([unknown] [209.85.210.185])
 by smtpin132.mac.com
 (Sun Java(tm) System Messaging Server 7u2-7.04 32bit (built Jul  2 2009))
 with ESMTP id <0KRV00IJ2SA1IC00@smtpin132.mac.com> for jkocherhans@mac.com
 (ORCPT jkocherhans@mac.com); Wed, 21 Oct 2009 13:15:38 -0700 (PDT)
X-Proofpoint-Virus-Version: vendor=fsecure
 engine=1.12.8161:2.4.5,1.2.40,4.0.166
 definitions=2009-10-21_11:2009-09-29,2009-10-21,2009-10-21 signatures=0
X-Proofpoint-Spam-Details: rule=notspam policy=default score=0 spamscore=0
 ipscore=0 phishscore=0 bulkscore=0 adultscore=0 classifier=spam adjust=0
 reason=mlx engine=5.0.0-0908210000 definitions=main-0910210183
Received: by yxe15 with SMTP id 15so8537359yxe.9 for <jkocherhans@mac.com>;
 Wed, 21 Oct 2009 13:15:37 -0700 (PDT)
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;        d=gmail.com;
 s=gamma; h=domainkey-signature:mime-version:received:date:message-id:subject
 :from:to:content-type;        bh=YrtdrLl8RzaFKTuh2w7XAQpOVTR+X/x5bmVCE6Prmzo=;
        b=xJFEqZbmCHhfZet9QYywAg0hs7v8t6Kl1VuHoiZaKUT5E7+Z50vaZDCL9gExAuECAW
   Njeq3HraZHR/mv7bE4Z8o/Xe4TvPIAkUjHZWenqnOpB7FrL9Fesp3Trx/tAesS1boVUg
 pEnEzK3izsZsnxamzdkeVSJuwrfu9O7VRc+8c=
DomainKey-Signature: a=rsa-sha1; c=nofws;        d=gmail.com; s=gamma;
 h=mime-version:date:message-id:subject:from:to:content-type;
 b=gjzGdmdiH9cUeHr7Hmgm2s1SRINtXKmSYORcObaY2Mv/L8ugVOmj1EBfMfZb6ZbX76
 lHg4f0YbA7BAw9diroSv9fXoUXw0mLpdatmTgmYWyFilvGFach4N7U8Z7PD7Iz4GGS9h
 kzntvWSGHmtL44UZidVxUZ4PZS45zsBLJ8NXw=
MIME-version: 1.0
Received: by 10.101.213.34 with SMTP id p34mr1544254anq.151.1256156136938; Wed,
 21 Oct 2009 13:15:36 -0700 (PDT)
Date: Wed, 21 Oct 2009 15:15:36 -0500
Message-id: <c90890f0910211315o3bc3c8a6m6e08248e867fd1e@mail.gmail.com>
Subject: Attachments
From: Joseph Kocherhans <jkocherhans@gmail.com>
To: jkocherhans@mac.com
Content-type: multipart/mixed; boundary=001636c92b78531c06047677a40b

--001636c92b78531c06047677a40b
Content-Type: multipart/alternative; boundary=001636c92b78531bfd047677a409

--001636c92b78531bfd047677a409
Content-Type: text/plain; charset=ISO-8859-1

This is a *test*.

--001636c92b78531bfd047677a409
Content-Type: text/html; charset=ISO-8859-1

This is a <i>test</i>.

--001636c92b78531bfd047677a409--
--001636c92b78531c06047677a40b
Content-Type: text/plain; charset=US-ASCII; name="text_attachment.txt"
Content-Disposition: attachment; filename="text_attachment.txt"
Content-Transfer-Encoding: base64
X-Attachment-Id: f_g12iw4060

c2ltcGxlIHRleHQgYXR0YWNobWVudAo=
--001636c92b78531c06047677a40b
Content-Type: image/gif; name="apache_pb.gif"
Content-Disposition: attachment; filename="apache_pb.gif"
Content-Transfer-Encoding: base64
X-Attachment-Id: f_g12iwbbo1

R0lGODlhAwEgAPcAAP///87OzqWlpYSEhHNzc2tra1paWiEYGP9CGP8xAL1SEN6thO+cQv+EAP/O
GP/OAM7Oxr29xjEA/2MA/5wA/+8A/+dK79573talzv8AnO9KjP8AY+eEnO9SY/8AGAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAAEALAAAAAADASAA
Rwj/AAMIHEiwoMGDCBMqXMiwocOHECNKnEixokWGEQ4cGDCwwIABAgJsMLAhwwYPKFEmWNnAQYSB
B/79MxDzXwSZB2j+OxAgpgEDMgn4FLAzwoCZPWUGJTAzAlACAXDq/FcQ6EyrBKzetHmxq9evYMMW
fEl2g9kKGypQoDBhwj8JSuO+lUB3Atu1FTJQyDAhg0m/BVD+O5kSAQIBLl+KXcy4sePHYiNEaDAA
QYOVCVIKTvnPgwEPZv2G9ivaZF69pdNmGPCgdesGDxrM/CeAo8ALdSdIaNuW7u7duiVcMHhh7drh
Ei+QXs68eQYNBjV7WNhBM4aCGDCvZLhAe4KDDBqI/28A+auA8+fLL4yQniD7kOrjy5/v8OV5uW/n
tl2bIW/fvRlMlZIBCChQU1ECHcVTVLQJJMCBUMW0oEBMKRWSU3JVFddGDsqkGH0ghjhfBAgYsFJn
oJVk2nIUVGDXWm5ZhZ9ccP32G1sVqDXAXhsAmMAALbnUUAS6tRWABb9N8OFBxRlHwUJOIofdcsNZ
sNx1CUm3kAbWYecdd18aFN54IpZp5plopqnmmmy26aZBDy450HkFKOaAAA3g2VBNAljFkVEGDGDf
Ty8ZAJVTBpBFgKAUGiCAU/AJQAB8AkVAQFYyafjPAI4G0Geinhr65qhlGlUTUCDt91+PKkqnUk0f
bv8FVYWSKfUTTgEcRRt6SU0I1AHoPSpTolZp6umwAcgoJ6nMqvfoTwQUEABfwdE4lwESGHCXi6hN
MBJhCaDIkniGIbCsfFtR2uy6IhqVklmhqdWfi2zBNWN+vvW2H714oTbSXyaB1sC5E+U7gQUNNenk
wgwbhyVCGjT3cEIYuGqxqxwYlB1mHYCpHXjjhSzyyAs8hqeJmg2GkoqkscyccWrdNcFPbtk7I1AN
GBDba605IKTGRU5QEJJFTkyQwg0nvZbRypEm5W3LZXyQlhVt7N3VWGMG8sgilzyqZAFIZlQDGyFw
AAIpHuDBABsMANrb8JqF0gFxG+XAAHeqe2S+Rh//hEFwEiA8ENJPN8Rc334fPhAHFzeOUsdefrxQ
d5IXNCbXmIsHAbucd+7556CHLvropJfOOcFhg03RgciKWCxBr5suO0Sm6i0po2hrloBlAyNU07H/
TCqXsJsSZdOvySoFbFJW8XTgAS9VGJemym9lAPOzZ2/QABoJCkABBUCFWgUEmDRSSiztfhjrwBo/
q0yS4iQh/BVqlCmfz+5kP7AycRS7QK/zyVZ8or0CHkRGt6qLk/yTms94QCkeMMzAakJBAMJPV9ez
nqSct5M5DetTSckQ7PATEuNdz4AoDFsBgGIAj9hMKb6RAIyM46+9EABcHliJAiyDGNUlhD0MeVRX
/1iYQhSKjT0v6VZvXgjDfMnQLn3pVtw048AcNqBceoPMBXJSxC5WKmy565Ff8jLDttxrLjd6Ihnb
ohrS3BBcmSkM6ihSl8IlRGl4vADiCnIBC/hRcA2BAAcY57iUcABxGOiAIjvgNYVQbiWNJAgDJknJ
SlqykpG0yGTc9i6XnaZFMGIifmpko/3gSC0xo0AB5FYYBLDNXBLJzW8AmRCkUeACuMylLgmXEOf4
ZY8Dkc4gh0lMDmigOinZHEGs5gHIOTJMlgvZAqZJzWpakzF3u0wcVxaatKjmNDlCpV0KABcZnVEm
wOENb9omntjA5mcIIRJwBkK03aDOlrvMZ5Q0RvOlwV0pS5pZCAYOicisGfRqWxPPJSeZSfWMzUQr
2QxKSMLNbi7nNP3xy17I2KK+xMwAM7tVXH5iAPHAUyB/S5I6eZMkxNkSj8bRIx99SVOpFYRqCeGA
Ig+pMe8UkwPWfKTWxCTNoC5AmWmSTG1c6Z0cuqpHFWWlAf5CGJKoqADthI1rfPYh3ABHjxgIawDC
StYLLLFwvIxI0/wCVrK6NawcWA50CCLMnw7zmJpBKkqhmRChfoeo46GkUa/pRdrpco7uOexAMKBL
YPpNlxAZ6DAnJlm7WlavA4FANR0rEM1W8yCDDS01C0va0pr2tKg9CEACBAQAOw==
--001636c92b78531c06047677a40b--
"""

class AttachmentsTestCase(unittest.TestCase):
    def setUp(self):
        self.msg = Message.from_string(RAW_MESSAGE)

    def test_attachments(self):
        attachments = list(self.msg.attachments())
        self.assertEqual(len(attachments), 2)
        text_filename, text_content = attachments[0]
        self.assertEqual(text_filename, u'text_attachment.txt')
        self.assertEqual(text_content, u'simple text attachment')

if __name__ == '__main__':
    unittest.main()

