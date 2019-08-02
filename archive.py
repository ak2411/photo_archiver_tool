import os
import argparse
from PIL import Image
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filepath", type=str, default="./ddlovato")
parser.add_argument("-d", "--date", type=str, default="")

try:
    args = parser.parse_args()
except:
    parser.print_help()
    sys.exit(0)

FILEPATH = args.filepath
if FILEPATH[-1] != "/":
    FILEPATH = FILEPATH + "/"
DATE = args.date

def rename_file():
    global FILEPATH, DATE
    for filename in os.listdir(FILEPATH):
        src = FILEPATH + filename
        viewer = subprocess.Popen(["open", "-W", src])
        desc = input("Image description:")
        dst = FILEPATH + DATE + "_" +  desc + ".jpg"
        os.rename(src, dst)
        viewer.terminate()
        viewer.kill()  # make sure the viewer is gone; not needed on Windows
if __name__ == "__main__":
    rename_file()
