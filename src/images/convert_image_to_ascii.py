import sys
sys.dont_write_bytecode = True
import math
import os
from PIL import Image
from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text

text = Text()
console = Console(highlight=False)

# resize image
def resize_img(img,new_dim=100):
    new_img = img.resize((new_dim,new_dim))
    return new_img

# convert image to greyscale
def greyscale_img(img):
    return img.convert("L")

# convert image to a string 
def img_to_pixels(img,palette):
    img_data = img.getdata()
    img_str = "".join([palette[pixel // math.ceil(255 / len(palette) + 1)] for pixel in img_data])
    return img_str

def format_image_string(img_str):
    img_str_len = len(img_str)
    ascii_img = "\n".join([img_str[index:(index + 100)] for index in range(0,img_str_len,100)])
    return ascii_img


def main(palette: list):
    # keep asking for a file path until a valid one is given and the file is an image of type jpg, png, or jpeg
    while True:
        path = Prompt.ask(Text.assemble(("Enter a valid Image path","green bold")))
        if os.path.isfile(path):
            if path.endswith(".jpg") or path.endswith(".png") or path.endswith(".jpeg"):
                break
        console.print("Invalid file path", style="red bold")
    try:
        img = Image.open(path)
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


    img_string = img_to_pixels(greyscale_img(resize_img(img,100)),palette)

    # formatting string
    ascii_img = format_image_string(img_string)

    # ask user if user wants to save the image
    save_img = Prompt.ask(Text.assemble(("Do you want to save the generated ascii art ? (y/n)", "green bold")))

    if save_img.lower() == "y":
        
        # get the file name and remove the file extension
        file_name = os.path.basename(path).split(".")[0]
        save_path = Prompt.ask(Text.assemble(("Where would you like to save the image (defaults to the current directory)", "green bold")))
        try:
            with open(f'{save_path}/{file_name}.txt',"w") as fs:
                fs.write(ascii_img)

            # if no path is given, save the image in the current directory
            if save_path == "":
                with open(f'{file_name}.txt',"w") as fs:
                    fs.write(ascii_img)
                console.print("Image saved in current directory", style="blue bold")
            else:
                console.print(f"Image saved in {save_path}", style="blue bold")
        except:
            console.print("Invalid file path", style="red bold")
            with open(f'{file_name}.txt',"w") as fs:
                fs.write(ascii_img)
            console.print("Image saved in current directory", style="blue bold")
    else:
        # create a checkbox to choose color to display the image in
        console.print("\n+ ---------------------------------------------------- +\n", style="yellow bold")
        console.print("Choose a color to display the image in: ", style="green bold")
        console.print("0. Default", style="white bold")
        console.print("1. Red", style="red bold")
        console.print("2. Green", style="green bold")
        console.print("3. Blue", style="blue bold")
        console.print("4. Yellow", style="yellow bold")
        console.print("5. Magenta", style="magenta bold")
        console.print("6. Cyan", style="cyan bold")
        console.print("7. White", style="white bold")
        color = Prompt.ask(Text.assemble(("Enter a number", "green bold")))
        console.print("\n+ ---------------------------------------------------- +\n", style="yellow bold")
        if color == "1":
            console.print(ascii_img, style="red")
        elif color == "2":
            console.print(ascii_img, style="green")
        elif color == "3":
            console.print(ascii_img, style="blue")
        elif color == "4":
            console.print(ascii_img, style="yellow")
        elif color == "5":
            console.print(ascii_img, style="magenta")
        elif color == "6":
            console.print(ascii_img, style="cyan")
        elif color == "7":
            console.print(ascii_img, style="white")
        elif color == "0":
            console.print(ascii_img, style="white")
        else:
            console.print(ascii_img, style="white")