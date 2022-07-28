import sys
sys.dont_write_bytecode = True
import images.convert_image_to_ascii as images_to_ascii
import videos.convert_video_to_ascii as videos_to_ascii
from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text

text = Text()
console = Console(highlight=False)

images_palette = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", " "]
videos_palette = [" ",".",":","-","=","+","*","#","%","@"]

def main():
    # ask user if user wants convert an image or a video
    console.print("Do you want to convert an image or a video?",style="green bold")
    console.print("1. Image",style="yellow bold")
    console.print("2. Video", style="blue bold")
    console.print("3. Exit", style="red bold")
    while True:

        choice = Prompt.ask(Text.assemble(("Enter your choice number", "green bold")))
        if choice == "1":
            images_to_ascii.main(images_palette)
            break

        elif choice == "2":
            videos_to_ascii.main(videos_palette)
            break
        elif choice == "3":
            console.print("Exiting...", style="red bold")
            break
        else:
            console.print("Invalid choice", style="red bold")
            continue
    console.print("Exiting...", style="red bold")

if __name__ == "__main__":
    main()