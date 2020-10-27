from PIL import Image
class Image2Ascii:
    def __init__(self , path , new_width):
        self.path = path
        self.new_width = new_width

    @staticmethod
    def __resize(image, new_width):
        width, height = image.size
        aspect_ratio = float(height) / float(width)
        new_height = aspect_ratio * new_width * 0.55
        image = image.resize((new_width, int(new_height)))

        return image

    @staticmethod
    def __grayscale(image):
        return image.convert('L')

    @staticmethod
    def __modify(image, buckets=25):
        initial_pixels = image.getdata()
        chars = list("@#S%?*+;:,.")
        new_pixels = [chars[pixel // buckets] for pixel in initial_pixels]
        return ''.join(new_pixels)

    @staticmethod
    def __process(image, new_width):
        image = Image2Ascii.__resize(image, new_width)
        image = Image2Ascii.__grayscale(image)
        pixels = Image2Ascii.__modify(image)

        len_pixels = len(pixels)

        new_image = [pixels[index: index + new_width]
                     for index in range(0, len_pixels, new_width)]
        return '\n'.join(new_image)

    def convert(self):
        image = None
        try:
            image = Image.open(self.path)
        except Exception:
            print('Unable to find image in {} \n'.format(self.path))
            exit()
        return Image2Ascii.__process(image, self.new_width)
