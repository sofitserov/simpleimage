# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PIL import Image
def circumfrence(r):
    cir = 2 * 3.1415926 * r
    return cir

def generateimage(name):
    width = 800
    height = 800
    img = Image.new('RGB', (width, height))

    for x in range(height):
        for y in range(width):
            img.putpixel((x, y), (0, x % 1, y % 100, 255))

    img.save(name)
    return

print('GENERATING...')
generateimage("generateimage.png")
print('DONE.')
typed = input("radius")
radius = float(typed)
f = circumfrence(radius)
print("circumfrence:",f)



