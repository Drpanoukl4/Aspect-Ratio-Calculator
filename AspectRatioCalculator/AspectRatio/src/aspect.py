import PIL
import fractions
from PIL import Image
from time import sleep
from rich.console import Console
from rich import print


filepath = "example.png"
img = Image.open(filepath)

w = img.width
h = img.height

print("[blue]The Width of the image is: [/blue] ", w,"px")
print("[red]The Height of the image is: [/red] ", h,"px")


def Aspect(Width, Height):
    return fractions.Fraction(Width/Height).limit_denominator()

resultado = Aspect(w, h)


console = Console()        

with console.status(("[+] [green]The Aspect Ratio is  Calculating:[/green]"))as status:
        sleep(3)
print("\nThe Aspect Ratio of the image is:",resultado)
