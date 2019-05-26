import pytest
from . game_manager import GameManager
import os

class TestGameManager:
    def test_get_files(self):
        # arrange
        cwd = os.getcwd()
        files = []
        files.append(os.path.join(cwd, "tmp/plik.txt"))
        files.append(os.path.join(cwd, "tmp/tmp2/plik2.txt"))
        files.append(os.path.join(cwd, "tmp/tmp3/plik3.txt"))
        for f in files:
            os.makedirs(os.path.dirname(f), exist_ok=True)
            with open(f, "w") as ff:
                ff.write("FOOBAR")
        p = os.path.join(cwd, "tmp/")
        gm = GameManager()
        # act
        os.chdir("../")
        result = gm.get_files(p)
        # assert
        assert result == files

