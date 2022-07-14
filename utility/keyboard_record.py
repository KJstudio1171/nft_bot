import keyboard
import pickle

# keyboard.wait('s')
# recorded = keyboard.record(until='esc')
# with open('keys\\1.p','wb') as file:
# 	pickle.dump(recorded, file)

with open('1.p','rb') as file:
	recorded = pickle.load(file)
keyboard.wait('s')
keyboard.play(recorded, speed_factor=1)