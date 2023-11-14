import pyfiglet
from termcolor import colored

name = input("enter your name")
color =input("what color do you want")
art = pyfiglet.figlet_format(name)
art_color = colored(art,color)
print(art_color)
