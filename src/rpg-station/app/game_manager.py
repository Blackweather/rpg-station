from . config_manager import ConfigManager
from . import config
import os
import json
import ntpath
import shutil
from shutil import copyfile

# this class takes care of sorting the ROMs
class GameManager:
    def get_extensions(self):
        cm = ConfigManager()
        cm.load_config()
        return cm.get_platform_shorts_with_ext()

    # get a list of files from directory
    def get_files(self, directory):
        files = []
        # r=root, d=directories,f=files
        for r, d, f in os.walk(directory):
            for _file in f:
                files.append(os.path.join(r, _file))
        return files

    # checks if given file matches any platform extension
    def match_extension(self, platforms, file_name):
        ext = file_name.split('.')[-1]
        for k, v in platforms.items():
            if ("." + ext) in v:
                return k
        return None

    def match_from_dir(self, directory):
        platforms = self.get_extensions()

        # get the directory files
        files = self.get_files(directory)
        # copy appropriate extensions to appropriate dirs in the rom dir
        matched_files = {}
        # go through all files
        for _file in files:
            # check if matched with extension
            matched_platform = self.match_extension(platforms, _file)
            if matched_platform != None:
                # if matched add to list in dict (platform:files)
                if matched_platform.lower() not in matched_files:
                    matched_files[matched_platform] = []
        for _file in files:
            # check if matched with extension
            matched_platform = self.match_extension(platforms, _file)
            if matched_platform != None:
                # if matched add to list in dict (platform:files)
                matched_files[matched_platform].append(_file)
        return matched_files

    def load_from_dir(self, directory):
        matched_files = self.match_from_dir(directory)
        
        ROOT_ROM_DIR = config.RPG_ROOT + "/rom/"
        for platform in matched_files.keys():
            platform_path = os.path.join(ROOT_ROM_DIR, platform.lower())
            # check if all platform directories exist
            if not os.path.exists(platform_path):
                print("Created directory: " + platform_path)
                # create missing
                os.makedirs(platform_path)
            else:
                # check out all files with extensions for duplicates
                for _file in matched_files[platform]:
                    # check if file already exists in platform dir
                    filename = ntpath.basename(_file)
                    existing_path = os.path.join(ROOT_ROM_DIR, filename)
                    if os.path.isfile(existing_path):
                        # remove duplicates from file list
                        print("File " + filename + " already exists!")
                        matched_files[platform].remove(_file)
        # log platform:files
        print("Files to import:")
        print(json.dumps(matched_files, indent=4, sort_keys=True))

        # copy remaining files
        for platforms in matched_files.keys():
            platform_path = os.path.join(ROOT_ROM_DIR, platforms.lower())
            for files in matched_files[platforms]:
                filename = ntpath.basename(files)
                try:
                    copyfile(files, os.path.join(platform_path, filename))
                except shutil.SameFileError:
                    print("Exception: shutil.SameFileError when trying to copy a file")
        #TODO: show a messagebox - use Window class?
        print("Files imported to Raspberry Pi Gaming Station")

    def load_from_file(self, filename):
        platforms = self.get_extensions()
        matched_platform = self.match_extension(platforms, filename)
        if matched_platform == None:
            print("Failed to import " + filename + ", no matching platform configured")
            exit(-1)
        ROOT_ROM_DIR = config.RPG_ROOT + "/rom/"
        platform_path = os.path.join(ROOT_ROM_DIR, matched_platform.lower())
        # check if platform directory exists
        if not os.path.exists(platform_path):
            print("Created directory: " + platform_path)
            # create missing directory
            os.makedirs(platform_path)
        else:
            # check for duplicate
            fname = ntpath.basename(filename)
            existing_path = os.path.join(platform_path, fname)
            if os.path.isfile(existing_path):
                print("Failed to import " + filename + ", file already exists")
                exit(-1)
        # copy the file
        fname = ntpath.basename(filename)
        try:
            copyfile(filename, os.path.join(platform_path, fname))
        except shutil.SameFileError:
            pass
        print("File imported to Raspberry Pi Gaming Station")
