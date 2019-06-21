import os
import game_manager

print(os.getcwd())
p = "/home/Karol/troll"
gm = game_manager.GameManager()
print (gm.get_extensions())
print (gm.match_from_dir(p))
gm.load_from_dir(p)
