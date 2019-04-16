letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {x: y for x, y in zip(letters, points)}
letter_to_points[" "] = 0


def score_word(word):
    point_total = 0
    for x in word:
        point_total += letter_to_points.get(x, 0)

    return point_total


brownie_points = score_word("BROWNIE")
# print(brownie_points)

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"],
                   "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
player_to_points = {}

for x in player_to_words:
    # print(x)
    # print(player_to_words.get(x))
    player_points = 0
    for y in player_to_words.get(x):
        player_points += score_word(y)
    player_to_points[x] = player_points

print(player_to_points)

# TODO: letters[] should handle lowercase
# TODO: play_word() should take input and store it to player's used words
# TODO: put loops into a function
