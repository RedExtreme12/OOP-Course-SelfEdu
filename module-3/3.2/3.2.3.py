from typing import Tuple


class ImageFileAcceptor:

    def __init__(self, extns: Tuple):
        self.__extensions = extns

    def __call__(self, filename) -> bool:
        filename_ext = filename.split('.')[-1]
        if filename_ext in self.__extensions:
            return True
        return False


if __name__ == '__main__':
    filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
    acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
    image_filenames = filter(acceptor, filenames)
    print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]
