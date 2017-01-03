#! /usr/bin/env python

import sys, doctest, string, StringIO
from colors import colorString
from tp_b1 import *

def prompt_release_stdout(fakestdout):
    # Function that prompts the user to realease content of fakestdout
    while True:
        action = raw_input("Print failed tests? [F(irst)/a(ll)/n(one)] ")
        action = action.lower()
        if action == '' or action == 'f':
            print fakestdout.getvalue().split("*" * 70)[1]
            break
        elif action == 'a':
            print fakestdout.getvalue()
            break
        elif action.lower() == 'n':
            break






fakestdout = StringIO.StringIO() # Fake file object for Stdout interception
stdout = sys.stdout # Backup stdout


targets = [
    ("add_ints", add_ints),
    ("sum_evens", sum_evens),
    ("surround", surround),
    ("center_in_field", center_in_field),
    ("comment_block", comment_block),
    ("is_nucleotide", is_nucleotide),
    ("is_valid_dna_sequence", is_valid_dna_sequence),
    ("get_complement", get_complement),
    ("get_complement_sequence", get_complement_sequence),
    ("get_number_from_letter", get_number_from_letter),
    ("get_letter_from_number", get_letter_from_number),
    ("shift_mod26", shift_mod26),
    ("encrypt_char", encrypt_char),
    ("encrypt_string", encrypt_string)
]

print "=" * 79
__test__ = {}
for fname, f in targets:
    __test__[fname] = f

    # Intercept Stdout
    sys.stdout = fakestdout
    res = doctest.testmod()
    # Restore Stdout
    sys.stdout = stdout
    test = string.ljust("{}".format(fname), 20, ' ') + " {}"

    if res.failed == 0:
        print colorString("green", test.format(res))
    else:
        print "=" * 79
        print colorString("red", test.format(res))
        print
        prompt_release_stdout(fakestdout)
        break

    del __test__[fname]


print "=" * 79

