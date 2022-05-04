#! /usr/bin/env python3
# mclip.py - A multi-clipboard program
# Credit: Automate The Boring Stuff With Python - No Starch Press - Al Sweigart
import sys, pyperclip

TEXT = {'agree': """Yes I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

if len(sys.argv) < 2:
    print("Usage: python mclip.py [keyphrase] - copy phrase text")
    sys.exit()

keyphrase = sys.argv[1] # first commandline arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f"Text for {keyphrase} copied to clipboard")
else:
    print(f"There is no text for {keyphrase}")
