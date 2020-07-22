#!/usr/bin/env python3

import logging

# Global logger config
import re

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)


class BinaryTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def print_tree(self):
        logger.info(self.data)

    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryTree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


def compress_string_while(string):
    compressed = ''
    count = 1
    seq_count = 1
    current_char = string[0]

    while count < len(string):
        if count < len(string) and current_char == string[count]:
            seq_count = seq_count + 1
        else:
            compressed = compressed + current_char + str(seq_count)
            current_char = string[count]
            seq_count = 1

        current_char = string[count]
        count = count + 1

    logger.info(compressed)


def compress_string_lookahead(string):
    string_len = len(string)
    current_char = string[0]
    index = 0
    compressed = ''

    while index < string_len:
        count = 1
        pattern = "{0}(?={0})".format(current_char)
        result = re.findall(pattern, string)

        compressed = compressed + current_char + str(len(result) + count)

        count = count + len(result)
        index = index + count

        if not index > len(string) - 1:
            current_char = string[index]

    logger.info(compressed)


def positive_lookbehind(lst):
    pattern = "(?<=tall)\sheight"

    myList = ",".join(lst)
    logger.info(myList)

    result = re.findall(pattern, myList)

    logger.info(result)

    count = len(re.findall(pattern, ", ".join(lst)))
    logger.info(count)


def positive_lookahead(lst):
    pattern = "short\s(?=height)"

    myList = ",".join(lst)
    logger.info(myList)

    result = re.findall(pattern, myList)

    logger.info(result)

    count = len(re.findall(pattern, ", ".join(lst)))
    logger.info(count)


def main():
    """
    :param event: AWS API Gateway REST event
    :param context: AWS API Gateway REST context
    :return: compressed string of input
    """
    # logger.info('hello')
    #
    # compress_string_while('Hello my dear friend to whom I feel very comfortable speaking too.')
    compress_string_lookahead('lla')

    # root.print_tree()
    # positive_lookbehind(["tall height", "tall height", "short height", "medium height", "tall height"])
    # positive_lookahead(["tall height", "tall height", "short height", "medium height", "tall height"])


if __name__ == '__main__':
    main()
