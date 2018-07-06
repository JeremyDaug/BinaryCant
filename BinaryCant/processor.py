from lxml import etree
from numpy import uint64 as uint
from typing import List
import hashlib as hash


stack = list()


def cant(file: str) -> List[uint]:
    """
    Entrypoint for the processor.
    :param file: The file to process.
    :return: List of
    """
    result = []
    tree = etree.parse(file)
    root = tree.getroot()

    ID = root.attrib['id']
    author = root.attrib['author']

    database = root.attrib.get('dict')
    if(database is None):
        database = 'default.csv'
    # load database

    # process Cant information
    IDBits = [uint(ord(x)) for x in ID]
    authorBits = [uint(ord(x)) for x in author]
    authorKeyList = hash.sha512(author.encode('utf-8')).hexdigest()
    for i in root:
        result.extend(sentence(i))

    return result


def sentence(sentence: etree.Element) -> List[uint]:
    result = list()
    for i in sentence:
        result.append(word(i))
    return result


def word(word) -> uint:
    result = uint(0)
    return result


def extension(word) -> List[uint]:
    result = list()
    return result


if __name__ == '__main__':
    cant('CantExample.xml')
