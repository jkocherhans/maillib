import maillib
import mailbox

# TODO: Write failed messages to a maildir for further examination

def process_mail(filename):
    message_count = 0
    bad_message_count = 0
    mbox = mailbox.mbox(filename)
    for key in mbox.keys():
        raw_message = mbox.get_file(key).read()
        try:
            message = maillib.Message.from_string(raw_message)

            message.sender
            message.to
            message.cc
            message.subject
            message.body
            message.html
        except UnicodeDecodeError:
            bad_message_count += 1

        message_count += 1

    print "Finished processing %s messages" % message_count
    print "%s failed decoding" % bad_message_count


if __name__ == '__main__':
    import sys
    try:
        filename = sys.argv[1]
    except IndexError:
        print "Usage: process-mail.py [path-to-mailbox]"
        sys.exit(1)
    process_mail(filename)

