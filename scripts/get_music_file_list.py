import glob
import pathlib

root_dir = "/Users/harris/raspberry_pi_website/html/music/"
web_dir = "http://192.168.1.10/"

if __name__ == "__main__":
    print(root_dir)
    for file_path in glob.iglob(root_dir + '**/*.mp3', recursive=True):
        path = pathlib.Path(file_path)
        index = path.parts.index('music')
        web_path = pathlib.Path(web_dir).joinpath(*path.parts[index:])
        print(web_path)
