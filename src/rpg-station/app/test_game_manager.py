import pytest
from .game_manager import GameManager
import os

class TestGameManager:
    def test_get_files():
        # arrange
        cwd = os.getcwd()
        files = []
        files.append(path.join(cwd, "tmp/plik.txt"))
        files.append(path.join(cwd, "tmp/tmp2/plik2.txt"))
        files.append(path.join(cwd, "tmp/tmp3/plik3.txt"))
        for f in files:
            os.makedirs(os.path.dirname(file), exist_ok=True)
            with open(f, "w") as ff:
                ff.write("FOOBAR")
        p = path.join(cwd, "tmp/")
        # act
        result = GameManager.get_files(p)
        # assert
        print("Expected ="+files)
        print("Result ="+result)
        assert result == files
        pass
