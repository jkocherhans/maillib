import re
import datetime
import email
import chardet


# Utilities #################################################################

def normalize_subject(subject):
    """
    Strips any leading Re or Fwd from the subject, and returns it. This is
    sometimes useful for grouping messages.
    """
    return re.sub(r'(?i)(re:|fw:|fwd:)\s+', '', subject)

def decode_header(header):
    """
    Decodes an email header to unicode. Assumes ascii if the encoding isn't
    embedded in the header.
    """
    parts = []
    for part in email.Header.decode_header(header):
        header_string, charset = part
        decoded_part = unicode(header_string, charset or 'ascii', errors='replace')
        parts.append(decoded_part)
    return u''.join(parts)

def decode_part(part):
    """
    Decodes a message part to unicode. Assumes ascii if the charset isn't in
    the parts Content-Type header.
    """
    # decode=True decodes quoted-printable and base64
    payload = part.get_payload(decode=True)
    charset = part.get_content_charset('ascii')
    try:
        text = payload.decode(charset)
    except UnicodeDecodeError:
        # If decoding fails, fall back to using chardet to try to guess the
        # encoding, and use that.
        charset = chardet.detect(payload)['encoding']
        text = payload.decode(charset)
    return text

class MessageDecoder(object):
    def __init__(self, message):
        self.message = message

    def __getitem__(self, key):
        raw_value = self.message[key]
        if isinstance(raw_value, unicode):
            return raw_value
        return decode_header(raw_value)

    def get(self, key, failobj=None):
        raw_value = self.message.get(key, failobj)
        if raw_value == failobj:
            return failobj
        return decode_header(raw_value)

    def get_all(self, key, failobj=None):
        raw_value = self.message.get_all(key, failobj)
        for header in raw_value:
            yield decode_header(header)


# Messages ##################################################################

class Message(object):
    """
    A simple class for dealing with email messages.
    """

    @classmethod
    def from_message(cls, msg):
        """
        Creates and returns a ``maillib.Message`` from and instance of
        ``email.Message.Message``.
        """
        message = cls()
        message._message = msg
        message._decoder = MessageDecoder(msg)
        return message

    @classmethod
    def from_file(cls, f):
        """
        Creates and returns a ``maillib.Message`` from a file-like object
        that contains a raw email message.
        """
        msg = email.message_from_file(f)
        return cls.from_message(msg)

    @classmethod
    def from_string(cls, s):
        """
        Creates and returns a ``maillib.Message`` from a string that contains
        a raw email message.
        """
        msg = email.message_from_string(s)
        return cls.from_message(msg)

    @property
    def subject(self):
        return self._decoder.get('subject')

    @property
    def sender(self):
        return email.Utils.parseaddr(self._decoder.get('from'))

    @property
    def to(self):
        return email.Utils.getaddresses(self._decoder.get_all('to', []))

    @property
    def cc(self):
        return email.Utils.getaddresses(self._decoder.get_all('cc', []))

    @property
    def date(self):
        """
        Returns the date of this message, converted to UTC.
        """
        d = email.Utils.parsedate_tz(self._message.get('date'))
        if d is None:
            return None
        timestamp = email.Utils.mktime_tz(d)
        return datetime.datetime.utcfromtimestamp(timestamp)

    @property
    def references(self):
        """
        Returns a list of everything that looks like a message-id in the
        references header, and the first thing that looks like a message-id
        in the in-reply-to header. See jwz's threading article for why you'd
        want to do this. http://www.jwz.org/doc/threading.html
        """
        references = []
        message_id_re = re.compile(r'(<[^>]*?>)')
        matches = message_id_re.finditer(self.raw_headers.get('references', ''))
        if matches is not None:
            for match in matches:
                references.append(match.group(1))
        match = message_id_re.search(self.raw_headers.get('in-reply-to', ''))
        if match is not None:
            references.append(match.group(1))
        return references

    @property
    def headers(self):
        return self._decoder

    @property
    def raw_headers(self):
        return self._message

    @property
    def body(self):
        """
        Returns first text/plain part in the message, or None if one could
        not be found.
        """
        for part in self._message.walk():
             if part.get_content_type() == 'text/plain':
                 return decode_part(part)
        return None

    @property
    def html(self):
        """
        Returns first text/html part in the message, or None if one could
        not be found.
        """
        for part in self._message.walk():
             if part.get_content_type() == 'text/html':
                 return decode_part(part)
        return None

    def attachments(self):
        """
        Returns an iterator over (filename, content) pairs for each attachment
        in the message.
        """
        for part in self._message.walk():
            # Assume that attachments have filenames
            if part.get_filename() is not None:
                if part.get_content_maintype() == 'text':
                    content = decode_part(part)
                else:
                    content = part.get_payload(decode=True)
                yield (part.get_filename(), content)

