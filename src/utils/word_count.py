import re
from collections import Counter


def find_word_frequency(text: str) -> object:
    """
    this function is to calculate the word frequency
    with key value pair
    :param text:
    :return sorted dictionary:
    """
    if len(text) > 1:
        lst = re.findall(r'\S+', re.sub('[^a-zA-Z \n]', "", text))
        res = Counter([x.lower() for x in lst]).most_common()
        return sorted(res, key=lambda x: (-x[1], x[0]))
    else:
        # text is empty return 0
        return 0
