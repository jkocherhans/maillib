import re


def extract_list_id(value):
    """
    Extracts and returns the first things that looks like a list-id from a
    message header value.
    """

    match = re.search(r'<([^>]*?)>', value)
    if match is None:
        return value
    return match.group(1)

