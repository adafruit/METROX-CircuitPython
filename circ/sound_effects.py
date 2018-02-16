"""
'sound_effects.py'
=================================================
Using AudioIO to produce some fun sounds!
"""
import audioio
import analogio
import board

f = open('siren.wav', 'rb')
a = audioio.AudioOut(board.A0, f)

fsr = analogio.AnalogIn(board.A2)
while True:
    if fsr.value < 200:
        a.play(loop=True)
    else:
        a.pause()
