year=int(raw_input())
if year % 4 == 0:
   if year % 100 == 0:
       if year % 400 == 0:
           print"yes"
       else:
           print"No"
   else:
       print"Yes"
else:
   print"No"
