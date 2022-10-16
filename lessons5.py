# Задание 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# line = 'Удалим из текста абвгдеежз, все слова) ""абв"".'
# print(f"Введенный текст: {line}")
# text = line.split(' ')
# word = 'абв'
# new_words = []
# for words in text:
#     if word not in words:
#         new_words.append(words)
# new_words = ' '.join(new_words)
# print(f"Входной текст: {new_words}")





# board = list(range(1,10))

# def draw_board(board):
#    for i in range(3):
#       print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")

# def take_input(player_token):
#    valid = False
#    while not valid:
#       player_answer = input("Куда поставим " + player_token + "? ")
#       try:
#          player_answer = int(player_answer)
#       except:
#          print("Введенное число корректно?")
#          continue
#       if player_answer >= 1 and player_answer <= 9:
#          if(str(board[player_answer - 1]) not in "XO"):
#             board[player_answer - 1] = player_token
#             valid = True
#          else:
#             print("Эта клетка уже занята!")
#       else:
#         print("Некорректный ввод. Введите число от 1 до 9.")

# def check_win(board):
#    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
#    for each in win_coord:
#        if board[each[0]] == board[each[1]] == board[each[2]]:
#           return board[each[0]]
#    return False

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#            take_input("X")
#         else:
#            take_input("O")
#         counter += 1
#         if counter > 4:
#            tmp = check_win(board)
#            if tmp:
#               print(tmp, "выиграл!")
#               win = True
#               break
#         if counter == 9:
#             print("Ничья!")
#             break
#     draw_board(board)
# main(board)

# input("Нажмите Enter для выхода!")



# with open('file_incod.txt', 'w') as data:
#     data.write('2232wesjeeurye')

# with open('file_incod.txt', 'r') as data:
#     string = data.readline()

# def rle_encode(dec_string):
#     enc_string = ''
#     count = 1
#     char = dec_string[0]
#     for i in range(1, len(dec_string)):
#         if dec_string[i] == char:
#             count += 1
#         else:
#             enc_string = enc_string + str(count) + char
#             char = dec_string[i]
#             count = 1
#             enc_string = enc_string + str(count) + char
#     return enc_string

# def rle_decode(enc_string):
#     dec_string = ''
#     char_amount = ''
#     for i in range(len(enc_string)):
#         if enc_string[i].isdigit():
#             char_amount += enc_string[i]
#         else:
#             dec_string += enc_string[i] * int(char_amount)
#         char_amount = ''
#     print(dec_string)

#     return dec_string

# with open('file_incod.txt', 'r') as file:
#     dec_string = file.read()

# with open('file_deccod.txt', 'w') as file:
#     enc_string = rle_encode(dec_string)
#     file.write(enc_string)

# print('Decoded string: \t' + dec_string)
# print('Encoded string: \t' + rle_encode(dec_string))
# print(f'Compress ratio: \t{round(len(dec_string) / len(enc_string), 1)}')