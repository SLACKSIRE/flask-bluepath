import sys


def is_ascii_compatible():
    '''
    Check if the terminal supports ascii art. This is a simple check that looks at the encoding of the standard output.
    '''
    encoding = sys.stdout.encoding
    if encoding is None:
        return False
    return encoding.lower() in ["utf-8", "ascii"]
