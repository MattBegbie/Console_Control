#Music_Control.py

import win32api as w

def nextSong():
    w.keybd_event(0xB0, 0)

def prevSong():
    w.keybd_event(0xB1, 0)

def stop():
    w.keybd_event(0xB2, 0)

def playPause(): 
    w.keybd_event(0xB3, 0)



while True:
    inp = str.lower(input("Input Playback Command: "))

    #print(inp)
    if inp == '?' or inp == '/?' or inp == 'help':
        print('\t? for help \n\tp for pause/play \n\tn/d/> for next song \n\tl/a/< for last song \n\te for exit')
        #?      -   help 
        #p      -   pause/play    
        #n/d/>  -   next song 
        #l/a/<  -   last song 
        #e      -   exit
    elif inp == 'p' or inp == 'pause' or inp == 'play':
        print('Song Paused')
        playPause()
    elif inp == 'd' or inp == 'n' or inp == 'next' or inp == '>':
        print('Song Skipped')
        nextSong()
    elif inp == 'l' or inp == 'last' or inp == 'previous' or inp == 'prev' or inp == 'a' or inp == '<':
        print('song returned')
        prevSong()
    elif inp == 'x' or inp == 'exit' or inp == 'e':
        print('Peace out')
        stop()
        break
    else:
        print('try again')

input()


#finding song name
# using api with verification from  spotify is too much work
# an api that connects to windows makes more sense to me because the media volume thing popup shows the song name so windows has the info somewhere or an easy way to access it.

