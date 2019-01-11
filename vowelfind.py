a=raw_input()
if a in {'a','e','i','o','u'}:
    print "Vowel"
elif a not in {'a','e','i','o','u'} and a.isalpha():
    print "Consonant"
else:
    print "invalid"
