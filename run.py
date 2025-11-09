from os import system
import sys
name: str = sys.argv[-1].split('\\')[-2]
system(f'manim {name}/main.py {name} && copy media\\videos\\main\\1080p60\\{name}.mp4 {name}\\{name}.mp4')