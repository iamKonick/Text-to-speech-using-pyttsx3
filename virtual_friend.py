import pyttsx3  # import library python text to speech

# to install pyttsx3 type pip install pyttsx3 in the terminal

# if the code doesn't run properly and gives an error "ModuleNotFoundError: No module named 'pythoncom'  in pyttsx3"
# try installing pip install pywin32

friend_amin = pyttsx3.init() # intialization of virtual friends
friend_miraj = pyttsx3.init()
friend_jishan = pyttsx3.init()
friend_shaharia = pyttsx3.init()
friend_Konick = pyttsx3.init()

friend_amin.say("Toke diye kicchu hobe na - You can not do anything properly") # making virtual friend say something
friend_miraj.say("obaahi ki je hoise mane erokom erokom - You won't believe what happened!")
friend_jishan.say("ekta meye de na bhai - please give me a girlfriend")
friend_shaharia.say("Tumi beparta bhujte parteso na - You do not understand the matter properly")
friend_Konick.say("Chol kori feli - Let's do it")


friend_amin.runAndWait() # run the text to speech and wait
