from easysound import play
import os.path
import keyboard


#virdata

print('Listening...')
while True:
    keyboard.wait('1')
    play.play('goodmorning.mp3')
    print('Succeed_play')
    keyboard.wait('2')
    play.play('no.mp3')
    print('Succeed_2')


