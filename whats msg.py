import pywhatkit
wno=input("enter the whats app number :- ")
msg=input("enter massage :-")
hr=int(input("enter time (hours in 24 hours time)"))
mnt=int((input("enter time (minutes)")))
pywhatkit.sendwhatmsg('+91'+wno,msg,hr,mnt)
input()