a=raw_input()
if a in {'a','e','i','o','u'}:
    print "vowel"
elif a not in {'a','e','i','o','u'} and a.isalpha():
    print "not a vowel"
else:
    print "invalid"
