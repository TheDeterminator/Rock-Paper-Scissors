player_score = 0
comp_score = 0
draw_score = 0
games = 3 #Num of games played Initialized to three to avoid divide by 0 errors and to "normalize" the probablity function
# Number of times player has played each move
r_plays = 0
s_plays = 0
p_plays = 0

#move_record = {'r': r_plays/games, 's': s_plays/games, 'p': p_plays/games}

while (True):
    #Keeps a record of how often the players plays each move and maps it to the defeating move
    move_record = {'p': r_plays/games, 'r': s_plays/games, 's': p_plays/games}
    users_most_played = max(move_record.values())

    #computer chooses the key corresponding to the move that beats players most often played move
    computer_choice = list(move_record.keys())[list(move_record.values()).index(users_most_played)] 
    user_choice = input('Choose a command: ')
    if user_choice == 'q':
        break;
    elif user_choice == 'show dict':
        print(move_record)
    elif user_choice.lower() == 'r' and computer_choice == 'r':
        draw_score += 1
        print(f'Computer chooses {computer_choice} you choose {user_choice}, DRAW W:{player_score}-L:{comp_score}-D:{draw_score}')
        r_plays += 1
        games += 1
    elif user_choice.lower() == 'r' and computer_choice == 's':
        player_score += 1
        print(f'Computer chooses {computer_choice} you choose {user_choice}, YOU WIN  W:{player_score}-L:{comp_score}-D:{draw_score}')
        r_plays += 1
        games += 1
    elif user_choice.lower() == 'r' and computer_choice == 'p':
        comp_score += 1
        print(f'Computer chooses {computer_choice} you choose {user_choice}, YOU LOSE  W:{player_score}-L:{comp_score}-D:{draw_score}')
        r_plays += 1
        games += 1
    elif user_choice.lower() == 's' and computer_choice == 's':
        draw_score += 1
        print(f'Computer chooses {computer_choice} you choose {user_choice}, DRAW W:{player_score}-L:{comp_score}-D:{draw_score}')
        s_plays += 1
        games += 1
    elif user_choice.lower() == 's' and computer_choice == 'r':
        comp_score += 1
        print(f'Computer chooses {computer_choice} you choose {user_choice}, YOU LOSE W:{player_score}-L:{comp_score}-D:{draw_score}')
        s_plays += 1
        games += 1
    elif user_choice.lower() == 's' and computer_choice == 'p':
        player_score += 1
        print(f'Computer chooses {computer_choice} you choose {user_choice}, YOU WIN W:{player_score}-L:{comp_score}-D:{draw_score}')
        s_plays += 1
        games += 1
    elif user_choice.lower() == 'p' and computer_choice == 'p':
        draw_score += 1        
        print(f'Computer chooses {computer_choice} you choose {user_choice}, DRAW W:{player_score}-L:{comp_score}-D:{draw_score}')
        p_plays += 1
        games += 1
    elif user_choice.lower() == 'p' and computer_choice == 'r':
        player_score += 1        
        print(f'Computer chooses {computer_choice} you choose {user_choice}, YOU WIN W:{player_score}-L:{comp_score}-D:{draw_score}')
        p_plays += 1
        games += 1
    elif user_choice.lower() == 'p' and computer_choice == 's':
        comp_score += 1        
        print(f'Computer chooses {computer_choice} you choose {user_choice}, YOU LOSE W:{player_score}-L:{comp_score}-D:{draw_score}')
        p_plays += 1
        games += 1
    else:
        print('Invalid uesr input')
