def add_score(difficulty):
    score_file = open("scores.txt", "r+")
    current_score = score_file.readline()

    new_score = int(current_score)
    new_score = (new_score*3)+5
    new_score = str(new_score)

    score_file.seek(0)
    score_file.truncate()

    score_file.writelines(new_score)
    score_file.close()

add_score(3)

