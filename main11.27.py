#Donald Brown
#1943301
team = {}

i = 1

for i in range(1, 6):
    jersey = int(input('Enter player {}\'s jersey number:\n'.format(i)))
    rating = int(input('Enter player {}\'s rating:\n'.format(i)))
    print('')
    if jersey < 0 and jersey > 99 and rating < 0 and rating > 9:
        print('Invalid number')
        break
    else:
        team[jersey] = rating

print('ROSTER')
sorted_roster = sorted(team.keys())

for jersey in sorted_roster:
    print('Jersey number: %d, Rating: %d' % (jersey, team[jersey]))

print(
    '\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n')


def menu_choice(user_input):
    while True:
        choice = input(user_input)
        if (choice == 'q'):
            print("\n".rstrip("\n"))
            break

        if (choice == 'o'):
            print('\nROSTER')
            sorted_roster = sorted(team.keys())
            for jersey in sorted_roster:
                print('Jersey number: %d, Rating: %d' % (jersey, team[jersey]))
            print(
                '\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n')

        if (choice == 'a'):
            jersey = int(input('\nEnter a new player\'s jersey number:\n'.format(i)))
            rating = int(input('\nEnter the players\'s rating:\n'.format(i)))
            team[jersey] = rating
            sorted_roster = sorted(team.keys())
            print(
                '\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n')

        if (choice == 'd'):
            jersey = int(input('\nEnter a jersey number:'))
            if jersey in team.keys():
                del team[jersey]
                sorted_roster = sorted(team.keys())
                print(
                    '\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n')
        if (choice == 'u'):
            jersey = int(input('\nEnter a jersey number: '))
            if jersey in team.keys():
                rating = int(input('Enter a new rating for player: '))
                team[jersey] = rating
                sorted_roster = sorted(team.keys())
                print(
                    '\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n')

        if (choice == 'r'):
            rating = int(input('\nEnter a rating:\n'))
            sorted_roster = sorted(team.keys())
            print('ABOVE', rating)
            for jersey in sorted_roster:
                if team[jersey] > rating:
                    print('Jersey number: %d, Rating: %d' % (jersey, team[jersey]))
            print(
                '\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n')

        else:
            sorted_roster = sorted(team.keys())


(menu_choice('Choose an option:'))