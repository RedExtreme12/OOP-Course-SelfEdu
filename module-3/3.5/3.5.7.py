class FileAcceptor:

    def __init__(self, *extensions):
        self._extensions = set(extensions) if not isinstance(extensions[0], set) else extensions[0]

    def __call__(self, filename: str) -> bool:
        extension = filename.split(sep='.')[-1]
        return True if extension in self._extensions else False

    def __add__(self, other: 'FileAcceptor'):
        return FileAcceptor(self._extensions.union(other._extensions))


filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]
acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames = list(filter(acceptor_images + acceptor_docs, filenames))
print(filenames)

