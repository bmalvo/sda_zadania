""" Content_manager_tasks solutions"""

# task 1:


def reader(file):
    read = open(file, encoding='utf-8')
    yield read.read()


print(next(reader(r'inwokacja')))

# task 2:


class ReadFile:

    def __init__(self, path=''):
        self.__source = path

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, path: str):
        self.__source = path

    def __enter__(self):
        self.__file_descriptor = open(self.source, 'a')
        return self.__file_descriptor

    def __exit__(self, *args):
        self.__file_descriptor.close()


def write_file_with_object(path='for_test.txt', text='abc'):
    try:
        with ReadFile(path) as rf:
            rf.write(text)
    except IOError as e:
        print(f'IOError caught {e.args}')


write_file_with_object()
