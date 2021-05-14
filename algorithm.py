import form_data_finnish
#import form_data_english
import random
data = form_data_finnish.read_and_form_data()
#data = form_data_english.read_and_form_data()

# WORKS WITH 4 OR 3 LETTERS with finnish or english list
# there can be multiple instances of the same value in the board


def return_list_of_words(wordlength):
    return data[wordlength]


def set_chars_to_string(list):
    text = ''
    for s in list:
        text += s

    return text


def set_word_start_horizontal(line, board):

    new_list = []
    for x in range(line):
        new_list.append(board[line][x])
    return set_chars_to_string(new_list)


def set_word_start_vertical(line, board):

    new_list = []
    for x in range(line + 1):
        new_list.append(board[x][line])
    return set_chars_to_string(new_list)


def find_possible_words(word_start, word_list):
    return list(filter(lambda word: word.startswith(word_start), word_list))


def find_random_word(possible_words_list):
    return list(random.choice(possible_words_list))


def set_word_horizontal(index, board, word):
    board[index] = word


def set_word_vertical(x, board, word):
    for z in range(len(board[x])):
        board[z][x] = word[z]


def initial_board(size):
    two_dimensional = []
    for t in range(size):
        line = []
        for f in range(size):
            line.append('0')
        two_dimensional.append(line)
    line = []
    return two_dimensional


def ask_board_size():
    value = input('How big is the board?\n')
    return value


def draw_board():
    x = int(ask_board_size())
    board = initial_board(x)

    words = return_list_of_words(x)
    words_on_board = 0
    words_in_the_end = 2 * x

    while words_on_board != words_in_the_end:
        words_on_board = 0
        for x in range(len(board)):
            if x == 0:
                # FIRST ROW
                # set horizontal
                # no need to use the word_start: board is empty
                word = find_random_word(words)
                set_word_horizontal(x, board, word)
                words_on_board += 1

                # set vertical
                word_start = set_word_start_vertical(x, board)
                possible_words = find_possible_words(word_start, words)

                word2 = find_random_word(possible_words)
                set_word_vertical(x, board, word2)
                words_on_board += 1

            else:
                # OTHER ROWS
                # set horizontal, all rows are the same
                word_start = set_word_start_horizontal(x, board)
                possible_words = find_possible_words(word_start, words)
                try:
                    word = find_random_word(possible_words)
                    set_word_horizontal(x, board, word)
                    words_on_board += 1
                except:
                    break

                # set vertical
                word_start = set_word_start_vertical(x, board)
                possible_words = find_possible_words(word_start, words)

                # last row down is different
                # if the last letters makes a word, board is ready
                if x == (len(board) - 1):
                    try:
                        if len(possible_words) != 0:
                            words_on_board += 1
                    except:
                        break
                else:
                    try:
                        # find the word with the right start and place it
                        word2 = find_random_word(possible_words)
                        set_word_vertical(x, board, word2)
                        words_on_board += 1
                    except:
                        break

    return board


def print_board():
    board = draw_board()
    for line in board:
        print(line)


def main():
    print_board()


if __name__ == '__main__':
    main()
