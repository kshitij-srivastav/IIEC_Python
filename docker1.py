#!/usr/bin/python3
import subprocess
import cgi
print("content-type: text/html")
print()
form=cgi.FieldStorage()
osname=form.getvalue("n")
osimage=form.getvalue("i")
#osname="os1"
cmd="sudo docker run -dit --name {} {}".format(osname,osimage)
s=subprocess.getstatusoutput(cmd)
status=s[0]
output=s[1]
if status==0 :
  print("Command executed!")
else:
  print("command failed!")
print(status)
print(output)
