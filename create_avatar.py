import argparse

from PIL import Image

CMYK = "CMYK"
RGB = "RGB"
LEFT, RIGHT, CENTERED = 'left', 'right', 'centered'
AVATAR_SIZE = 80
SHIFT_SIZE = 50


def get_shifted_image(image, shift_size, shift_direction, opacity=0.5):
    width, height = image.size
    coords_centered = (shift_size // 2, 0, width - shift_size // 2, height)
    if shift_direction == LEFT:
        coords_shifted = (shift_size, 0, width, height)
    elif shift_direction == RIGHT:
        coords_shifted = (0, 0, width - shift_size, height)
    elif shift_direction == CENTERED:
        coords_shifted = coords_centered
    return Image.blend(*map(image.crop, (coords_centered, coords_shifted)),
                       opacity)


def get_image_with_effects(image, shift_size):
    red_img, green_img, blue_img = image.split()
    shifted_red = get_shifted_image(red_img, shift_size, LEFT)
    shifted_blue = get_shifted_image(blue_img, shift_size, RIGHT)
    resized_green = get_shifted_image(green_img, shift_size, CENTERED)
    return Image.merge(RGB, (shifted_red, shifted_blue, resized_green))


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_path")
    parser.add_argument("destination_path")
    args =  parser.parse_args()
    return args.source_path, args.destination_path


if __name__ == '__main__':
    image_path, avatar_path = get_args()
    image = Image.open(image_path).convert(RGB)
    avatar_image = get_image_with_effects(image, SHIFT_SIZE)
    avatar_image.thumbnail((AVATAR_SIZE, AVATAR_SIZE))
    avatar_image.save(avatar_path)
