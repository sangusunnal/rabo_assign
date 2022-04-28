# -*- coding: utf-8 -*-
from rabo_assign.src.utils.word_count import find_word_frequency


class WordFrequency:
    """
        Attributes:
            word (str): The word attribute
            frequency(int): the frequency attribute
    """

    def __init__(self):
        self.word = ""
        self.frequency = 0

    @property
    def word(self):
        return self.word

    @property
    def frequency(self):
        return self.frequency

    @word.setter
    def word(self, value):
        self._word = value

    @frequency.setter
    def frequency(self, value):
        self._frequency = value


class WordFrequencyAnalyzer(WordFrequency):
    """
    The WordFrequencyAnalyzer class use below method for analyze
    the word frequency.
    """

    def __init__(self):
        super().__init__()

    def calulate_highest_frequency(self, text: str) -> object:
        """
        input text : The input text contains words separated text.
        calulate_highest_frequency : calulate_highest_frequency of word.
        :type text: object
        :param text:
        :return int:
        """
        res = find_word_frequency(text)
        # text is empty it will return 0
        return res[0][1] if res != 0 else 0

    def calulate_frequency_for_word(self, text: str, word: str) -> object:
        """
        input text,word : The input text contains words separated text
        and word which we to calulate frequency.
        calulate_frequency_for_word (int) : A highest_frequency of given
        specified word.
        :type text: object
        :param text:
        :param word:
        :return int:
        """
        res = find_word_frequency(text)
        # word is empty it will return 0
        # word not found in text it will return 0
        return dict(res).get(word, 0)

    def calulate_most_frequent_n_words(self, text: str, n: int) -> object:
        """
        input text, n: The input text contains words separated text
        and frequent 'n' words.
        calulate_most_frequent_n_words [] : A highest_frequency n word
        which given text.
        :type text: object
        :param text:
        :param n:
        :return []:
        """
        res = find_word_frequency(text)
        # this will return 0 when nth value more than the frequent
        if res != 0 and len(res) >= n:
            return [res[i] for i in range(len(res)) if i < n]
        else:
            return []

