import re
from main import word_sieve

string = "Example string here containing punctuation usually"

string = re.split(r''', |\. |: |; |! |\? | - |-| \(|\) | \[|\] | "|" | ''|'' | & | \{|\} | \.\.\.''', string)
print string

for x in string:
    x = x.replace(" ", "")
    output = word_sieve(x)
    result = [" ".join(x) for x in output]
    print result
    if result in string:
        print "Found a string"
