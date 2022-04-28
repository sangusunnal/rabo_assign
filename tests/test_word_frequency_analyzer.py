import pytest
from rabo_assign.src.word_frequency_analyzer import WordFrequencyAnalyzer

testdata1 = [
    ("The sun shines over the lake", 2),
    ("The sun shines THE over the lake thE", 4),
    ("The sun shines over the lake Lake LAKE", 3),
    ("", 0)
]

testdata2 = [
    ("The sun shines over the lake", "the", 2),
    ("The sun shines over the s@un lake", "sun", 2),
    ("The sun shines over the lake Lake LAKE", "lake", 3),
    ("The sun shines THE over the lake sun", "sun", 2),
    ("The sun shines THE over the lake sun", "apple", 0)
]

testdata3 = [
    ("The sun shines over the lake", 3, [('the', 2), ('lake', 1), ('over', 1)]),
    ("sun shines over the lake and over", 2, [('over', 2), ('and', 1)]),
    ("The sun shines over the lake tHE way to moon Lake", 3, [('the', 3), ('lake', 2), ('moon', 1)]),
    ("The sun shines over the lake", 99, []),
    ("The", 1, [('the', 1)]),
    ("", 1, [])
]


@pytest.mark.parametrize("a,expected", testdata1)
def test_calulate_highest_frequency(a, expected):
    res = WordFrequencyAnalyzer().calulate_highest_frequency(a)
    assert res == expected


@pytest.mark.parametrize("a,b,expected", testdata2)
def test_calulate_frequency_for_word(a, b, expected):
    res = WordFrequencyAnalyzer().calulate_frequency_for_word(a, b)
    assert res == expected


@pytest.mark.parametrize("a,b,expected", testdata3)
def test_calulate_most_frequent_n_word(a, b, expected):
    res = WordFrequencyAnalyzer().calulate_most_frequent_n_words(a, b)
    assert res == expected
