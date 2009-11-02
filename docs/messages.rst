.. module:: maillib

Messages
========

``maillib``'s ``Message`` class provides a simple wrapper around Python's
``email.message.Message`` that tries to decode values to unicode automatically,
but leaves access to the underlying object in case you need to do something
more complex.


Creating Message objects
------------------------

.. classmethod:: Message.from_string(string)

    Creates and returns a ``maillib.Message`` from a string that contains
    a raw mime message.

.. classmethod:: Message.from_file(file)

    Creates and returns a ``maillib.Message`` from a file-like object
    that contains a raw mime message.

.. classmethod:: Message.from_message(message)

    Creates and returns a ``maillib.Message`` from an
    ``email.message.Message`` instance.


Message attributes 
------------------

.. class:: Message

    .. attribute:: subject

        The value of the message's :mailheader:`Subject` header.

    .. attribute:: sender

        A ``(name, email_address)`` tuple from the message's :mailheader:`From` header.
        For example: ``('John Doe', 'john@example.com')``

    .. attribute:: to

        A list of ``(name, email_address)`` tuples for every
        recipient in the message's :mailheader:`To` header. For example:
        ``[('John Doe', 'john@example.com'), ('Jane Doe', 'jane@example.com')]``

    .. attribute:: cc

        A list of ``(name, email_address)`` tuples for every
        recipient in the message's :mailheader:`Cc` header. For example:
        ``[('John Doe', 'john@example.com'), ('Jane Doe', 'jane@example.com')]``

    .. attribute:: date

        A ``datetime.datetime`` object representing the message's :mailheader:`Date`
        header. 

        .. warning:: 
            The value is always UTC, so you might want to convert it to local time.

    .. attribute:: body

        The plain text body of the message if one exists, otherwise ``None``.

        In practice, we do a depth-first traversal of the message using
        ``message.walk()`` and return the first payload that has a
        :mailheader:`Content-type` of :mimetype:`text/plain`.

    .. attribute:: html

        The HTML body of the message if one exists, otherwise ``None``.

        In practice, we do a depth-first traversal of the message using
        ``message.walk()`` and return the first payload that has a 
        :mailheader:`Content-type` of :mimetype:`text/html`.

    .. method:: attachments()

        Returns an iterator over (filename, content) tuples for every attachment
        in the message.

    .. attribute:: references

        A list of everything that looks like a :mailheader:`Message-id`
        in the :mailheader:`References` header, and the first thing that looks
        like a :mailheader:`Message-id` in the :mailheader:`In-reply-to` header.
        See jwz's threading article [#jwzthreding]_ for why you'd want to do this.

    .. attribute:: headers

        A dictionary like interface to decoded message headers.

    .. attribute:: raw_headers

        A dictionary like interface to raw message headers.

.. [#jwzthreding] http://www.jwz.org/doc/threading.html

