from PIL import Image,ImageColor
individual = 255,000,000
img = Image.new('RGB', (60,60), color = ImageColor.getrgb("#ff0000"))
img.save("Resources/image.png")