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

keyboard.add_hotkey('1',GM)
keyboard.add_hotkey('2',NO)

keyboard.wait()