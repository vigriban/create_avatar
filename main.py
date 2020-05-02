from PIL import Image
if __name__ == '__main__':
    path = "/tmp/alupka.jpeg"
    image = Image.open(path)
    print(image.size())
