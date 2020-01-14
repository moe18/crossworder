import numpy as np
import pandas as pd
import nltk
from nltk.corpus import words
from image_getter import get_puzzel


nltk.download('words')

wordlist = words.words()


def next_letter(letters1, letters2, len_word, len_word2):
    word1 = ''
    word2 = ''
    for i in letters1:
        if i != '0.0':
            word1 += i

    for i in letters2:
        if i != '0.0':
            word2 += i

    posible_letter = []
    posible_letter2 = []

    print(word1,len_word, word2,len_word2)
    for i in wordlist:
        if i.startswith(str(word1)) and len(i) == len_word:
            posible_letter.append(i[len(word1)])
        if i.startswith(str(word2)) and len(i) == len_word2:
            posible_letter2.append(i[len(word2)])

    posible_letters = (pd.Series(posible_letter).value_counts() / len(posible_letter) * pd.Series(
        posible_letter2).value_counts() / len(posible_letter2)).dropna()

    sample = np.random.choice(posible_letters.index, 1, p=posible_letters / sum(posible_letters))

    return sample


def word_map_across(matrix):
    matrix = matrix.astype('str')
    down_or_across = []
    for row in matrix:
        count = 0
        count2 = 0
        for i in row:
            count2 += 1
            if i == '1.0':
                count += 1

            else:
                if count > 0:
                    down_or_across.append(count)
                    count = 0

            if count2 == 15:
                down_or_across.append(count)

    down_or_across_2 = []
    for i in down_or_across:
        for j in range(i):
            down_or_across_2.append(i)

    test_1 = matrix.copy()

    test_1 = test_1.astype('float')

    count = 0


    for i in range(len(test_1[:, 1])):
        for j in range(len(test_1[1, :])):
            if test_1[i, j] != 0:
                test_1[i, j] = down_or_across_2[count]
                count += 1

    return test_1


def word_map_down(matrix):
    matrix = matrix.astype('str')
    down_or_across = []

    down = []

    for row in range(15):
        count = 0
        count2 = 0
        for i in matrix[:, row]:
            count2 += 1
            if i == '1.0':
                count += 1

            else:
                if count > 0:
                    down.append(count)
                    count = 0

            if count2 == 15:
                down.append(count)

    down_or_across_2 = []
    for i in down:
        for j in range(i):
            down_or_across_2.append(i)

    print(down_or_across_2)
    test_1 = matrix.copy()

    test_1 = test_1.astype('float')

    count = 0

    for i in range(len(matrix[1, :])):
        for j in range(len(matrix[:, 1])):
            if test_1[j, i] != 0:
                test_1[j, i] = down_or_across_2[count]
                count += 1

    return test_1


puzzle = get_puzzel()

across_words = word_map_across(puzzle)
down_words = word_map_down(puzzle)

puzzle = puzzle.astype('str')
puzzle[0,:4] = ['t','i','m','e']



result = None
while result is None:

    try:

        puzzle_copy = puzzle.copy()
        for i in range(len(puzzle[:, 1])):
            count0 = 0
            count1 = 0
            count2 = 0
            count3 = 0
            for j in range(len(puzzle[1, :])):


                if puzzle[i, j] == '1.0':

                    # TODO: problem with the second input
                    letter = next_letter(puzzle_copy[i, count0:j], puzzle_copy[count1:i, j],
                                         across_words[i, j], down_words[i, j])[0]

                    count3 += 1
                    count2 += 1
                    puzzle_copy[i, j] = letter
                    print(puzzle_copy)
                else:
                    count0 = count2
                    count1 = count3
                    count3 += 1
                    count2 += 1

        result = puzzle_copy
        print('\n', result)
    except ValueError as e:
        print('\n')
        pass
