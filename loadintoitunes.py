from subprocess import call
import os
import shutil
import csv
import audioop
import numpy as np


def iAddSongs(dir):
    """Adds all audio files in dir to iTunes and puts them in Music folder.
    DOES NOT CHECK FOR DUPLICATES so do not call more than one time for any
    given directory unless you want a ton of duplicate files."""
    fileexts = ['mp3', 'm4a', 'm4p']  # Add desired audio filetypes here
    for tuple in os.walk(dir):
        for file in tuple[2]:
            ext = file[file.__len__()-3:]
            if ext in fileexts:
                print "Adding: \"" + tuple[0] + "/" + file + "\""
                try:
                    shutil.copy(tuple[0] + "/" + file, "C:\Users\Owen Buehler\Music\iTunes\iTunes Media\Automatically Add to iTunes")
                    shutil.copy(tuple[0] + "/" + file, "C:\Users\Owen Buehler\Music")  # iTunes add folder doesnt store files prettily, so put them in music too
                    os.remove(tuple[0] + "/" + file)

                except shutil.Error:  # File already exists
                    print "shutil error. Skipping: \"" + tuple[0] + "/" + file + "\""



def remove_silence(song):
    #TODO
    pass


if __name__ == '__main__':
#    url = 'https://www.youtube.com/watch?v=OCYqRkq3vTk'
    songpath = "C:\Users\Owen Buehler\Music\Bullet and a Target.mp3"
    remove_silence(songpath)

