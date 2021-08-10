import playsound
import os.path
import keyboard

# virdata

print('Listening...')
def GM():
    playsound.playsound('goodmorning.mp3')
    print('Succeed play')
    
def NO():
    playsound.playsound('no.mp3')
    print('Succeed play')

while True:
    keyboard.add_hotkey('Q',GM)
    keyboard.add_hotkey('W',NO)
