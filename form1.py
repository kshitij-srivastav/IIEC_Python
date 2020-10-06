#!/usr/bin/python3
import cgi
import subprocess
print("content-type: text/html")
print()
form=cgi.FieldStorage()
cmd=form.getvalue("n") or "abc"
if ("run" in cmd or "execute" in cmd) and "date" in cmd:
  x=subprocess.getoutput("date")
  print(x)
elif ("run" in cmd or "execute" in cmd) and ("calendar" in cmd or "cal" in cmd):
  x=subprocess.getoutput("cal")
  print(x)
else:
  print("Enter correct command!")

