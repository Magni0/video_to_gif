from argparse import ArgumentParser, RawDescriptionHelpFormatter
from os import listdir, getcwd, mkdir, remove, path
from moviepy.video.io.VideoFileClip import VideoFileClip

formats = (".webm", ".mp4")

class ConvertVideo:
    
    def __init__(self, args):
        self.args = args
        self.path = self.args.path
        self.output = self.args.output

    def get_path(self):
        """if path is specified return path, else return current working dir"""

        if self.path == None: # if no path given
            self.path = getcwd()
            return self.path
        else: # if path given
            return self.path
    
    def out_put_dir(self):
        """if output is specified create/return output path, else create/return `gif` dir"""

        self.files = listdir(self.get_path())
        if self.output == None:
            if "gif" in self.files:
                return "gif"
            else:
                mkdir(f"{self.path}/gif")
                return "gif"
        else:
            if self.output in self.files:
                return self.output
            else:
                mkdir(self.path + "/" + self.output)
                return self.output

    def convert(self):
        _path = self.get_path()
        output_dir = self.out_put_dir()
        count_max = 0
        count_current = 0

        for i in self.files:
            if i.endswith(formats):
                count_max += 1

        for file in self.files:
            if file.endswith(formats):
                clip = VideoFileClip(file)
                output_path = f"{_path}/{output_dir}/{path.splitext(file)[0]}.gif"
                count_current += 1
                print(f"converting: {file}  ({count_current}/{count_max})")
                clip.write_gif(output_path)

parser = ArgumentParser(
    formatter_class=RawDescriptionHelpFormatter, 
    description="""Converts all Video files to gif in dir"""
        )

parser.add_argument("-p", "--path", type=str, help="the path (path is cwd by default)")
parser.add_argument("-o", "--output", type=str, help="path of where the gifs are put, outputs into `gif` dir if not given")
# parser.add_argument("-r", "--replace", action="store_true", help="replaces the video with gif in same dir")
args = parser.parse_args()

run = ConvertVideo(args)
run.convert()