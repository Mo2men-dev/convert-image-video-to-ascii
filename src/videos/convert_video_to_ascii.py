import sys
sys.dont_write_bytecode = True
import math
import cv2
import os
from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text
from images.convert_image_to_ascii import format_image_string

text = Text()
console = Console(highlight=False)

def play_video_in_terminal(palette: list):

    # keep asking for a file path until a valid one is given and the file is a video of type mp4
    while True:
        path = Prompt.ask(Text.assemble(("Enter a valid Video path","green bold")))
        if os.path.isfile(path):
            if path.endswith(".mp4") or path.endswith(".avi"):
                break
        console.print("Invalid file path", style="red bold")
    try:
        video = cv2.VideoCapture(path)
    except:
        console.print("Invalid file path", style="red bold")

    # ask if user wants to use a custom palette
    console.print("the default palette is: ", style="white bold",end="")
    console.print(" ".join(palette), style="yellow bold")
    custom_palette = Prompt.ask(Text.assemble(("Do you want to use a custom palette? (y/n)", "green bold")))
    if custom_palette.lower() == "y":
        # ask for the custom palette
        custom_palette = Prompt.ask(Text.assemble(("Enter the custom palette separate each char with a ',' ", "green bold")))
        # convert the palette to a list
        custom_palette = custom_palette.split(",")
        # convert the palette to a list of characters
        palette = custom_palette
        console.print("Using custom palette... The custom palette is: ", end="")
        console.print(" ".join(palette), style="yellow bold")
    else:
        console.print("Using default palette...", style="blue bold")

    # ask user which color they want to use for the text
    text_color = Prompt.ask(Text.assemble(("Enter the color you want to use for the text","green bold")),choices=["red","green","blue","yellow","cyan","magenta","white"],default="white")
    text_color = text_color.lower()

    while video.isOpened():
        ret, frame = video.read()
        if ret:
            # greyscale the frame
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # resize the frame
            resized_frame = cv2.resize(gray, (100, 50))

            # convert the frame to a string
            img_str = "".join([palette[pixel // math.ceil(255 / len(palette) + 1)] for pixel in resized_frame.flatten()])

            # formatting string
            ascii_img = format_image_string(img_str)

            # print the frame
            console.print(ascii_img, style=f"{text_color}")

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    
def play_live_feed_in_terminal(palette: list):

    # ask user which color they want to use for the text
    text_color = Prompt.ask(Text.assemble(("Enter the color you want to use for the text","green bold")),choices=["red","green","blue","yellow","cyan","magenta","white"],default="white")
    text_color = text_color.lower()

    # define a video capture object
    video = cv2.VideoCapture(0)
    
    while video.isOpened():
        ret, frame = video.read()
        if ret:
            # greyscale the frame
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # resize the frame
            resized_frame = cv2.resize(gray, (100, 50))

            # convert the frame to a string
            img_str = "".join([palette[pixel // math.ceil(255 / len(palette) + 1)] for pixel in resized_frame.flatten()])

            # formatting string
            ascii_img = format_image_string(img_str)

            # print the frame
            console.print(ascii_img, style=f"{text_color}")

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    

        

def main(palette: list):
    # ask user if user wants convert a video and play it  in the terminal or play a video/live feed in terminal
    console.print("Do you want to play a video or live feed in the terminal ?",style="green bold")
    console.print("1. Video",style="yellow bold")
    console.print("2. Live Feed", style="blue bold")
    console.print("3. Exit", style="red bold")
    while True:
        choice = Prompt.ask(Text.assemble(("Enter your choice number", "green bold")))
        if choice == "1":
            play_video_in_terminal(palette)
            break
        elif choice == "2":
            play_live_feed_in_terminal(palette)
            break
        elif choice == "3":
            console.print("Exiting...", style="red bold")
            break
        else:
            console.print("Invalid choice", style="red bold")
            continue