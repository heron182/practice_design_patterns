# pylint: disable=W0612
import io
import logging

logging.basicConfig(level=logging.INFO)


class InMemoryStrategy(object):
    @staticmethod
    def save(data):
        return io.BytesIO(data)


class FileStrategy(object):
    @staticmethod
    def save(data):
        file = open('somefile', mode='wb')
        file.write(data)
        return file


def main():
    logging.info('Saving small file in-memory')
    small_file = InMemoryStrategy.save(b'5a 66 a7 92 0f 98 3f 90 78 74')

    logging.info('Saving big file in-file')
    big_file = FileStrategy.save(b''' 
                                     94 c1 d5 38 28 4c 9f 24 62 09 07 94 d8 59 f2 a3 
                                     66 09 f3 0b 4c 0d 82 12 6c 37 47 2e c3 85
                                ''')


if __name__ == '__main__':
    main()
