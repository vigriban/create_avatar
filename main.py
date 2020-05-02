from PIL import Image


def view_attributes(image):
    width, height = image.size
    format = image.mode
    print(f'Ширина - {width}\nВысота - {height}\nЦветовая модель - {format}')


if __name__ == '__main__':
    path = "/tmp/alupka.jpeg"
    image = Image.open(path)
    view_attributes(image)
