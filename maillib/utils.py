import re


def normalize_subject(subject):
    """
    Strips any leading Re or Fwd from the subject, and returns it. This is
    sometimes useful for grouping messages.
    """
    return re.sub(r'(?i)(re:|fw:|fwd:)\s+', '', subject)

def extract_list_id(value):
    """
    Extracts and returns the first things that looks like a list-id from a
    message header value.
    """
    match = re.search(r'<([^>]*?)>', value)
    if match is None:
        return value
    return match.group(1)

