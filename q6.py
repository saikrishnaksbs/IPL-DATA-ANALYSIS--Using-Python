import csv
import matplotlib.pyplot as plt


def calculate(matches):
    '''for calculating'''
    match_data = []
    with open(matches, 'r', encoding='utf-8') as file:
        matches = csv.DictReader(file)

        for match in matches:
            match_data.append(match)

    seasons = set()
    teams = set()
    for match in match_data:

        seasons.add(match['season'])
        teams.add(match['team1'])

    seasons = list((seasons))
    teams = list((teams))
    teams.sort()
    seasons.sort()
    seasons_and_teams = {}

    for match in match_data:

        year = match['season']
        team1 = match['team1']
        team2 = match['team2']

        if year in seasons:

            if year not in seasons_and_teams:
                seasons_and_teams[year] = {}
                winner = match['winner']
                if (team1 not in seasons_and_teams[year] and winner == team1):
                    seasons_and_teams[year][team1] = 1
                elif team1 in seasons_and_teams[year] and winner == team1:
                    seasons_and_teams[year][team1] += 1
                else:
                    pass
                if team2 not in seasons_and_teams[year] and winner == team2:
                    seasons_and_teams[year][team2] = 1
                elif team1 in seasons_and_teams[year] and winner == team2:
                    seasons_and_teams[year][team2] += 1
            else:
                if team1 not in seasons_and_teams[year] and winner == team1:
                    seasons_and_teams[year][team1] = 1
                elif team1 in seasons_and_teams[year] and winner == team1:
                    seasons_and_teams[year][team1] += 1
                else:
                    pass
                if team2 not in seasons_and_teams[year] and winner == team2:
                    seasons_and_teams[year][team2] = 1
                elif team1 in seasons_and_teams[year] and winner == team2:
                    seasons_and_teams[year][team2] += 1
                else:
                    pass

    for year in seasons:
        for team in teams:
            if team not in seasons_and_teams[year]:
                seasons_and_teams[year][team] = 0
    return seasons_and_teams


def tranform(seasons_and_teams_matches):
    '''for transforming'''
    final = list(seasons_and_teams_matches.values())
    match_count = []
    for year in range(10):
        count = list(final[year].values())
        match_count.append(count)

    print(match_count)
    seasons_and_teams_matches_final = list(map(list, zip(*match_count)))

    return seasons_and_teams_matches_final


def plot(teams, seasons):

    _, ax = plt.subplots()
    team2start = [teams[0][i]+teams[1][i] for i in range(len(teams[0]))]
    team3start = [teams[0][i]+teams[1][i]+teams[2][i]
                  for i in range(len(teams[0]))]
    team4start = [teams[0][i]+teams[1][i]+teams[2][i]+teams[3][i]
                  for i in range(len(teams[0]))]
    team5start = [teams[0][i]+teams[1][i]+teams[2][i] +
                  teams[3][i]+teams[4][i] for i in range(len(teams[0]))]
    team6start = [teams[0][i]+teams[1][i]+teams[2][i]+teams[3]
                  [i]+teams[4][i]+teams[5][i] for i in range(len(teams[0]))]
    team7start = [teams[0][i]+teams[1][i]+teams[2][i]+teams[3][i] +
                  teams[4][i]+teams[5][i]+teams[6][i]
                  for i in range(len(teams[0]))]
    team8start = [teams[0][i]+teams[1][i]+teams[2][i]+teams[3][i]+teams[4]
                  [i]+teams[5][i]+teams[6][i]+teams[7][i]
                  for i in range(len(teams[0]))]
    team9start = [teams[0][i]+teams[1][i]+teams[2][i]+teams[3][i]+teams[4][i] +
                  teams[5][i]+teams[6][i]+teams[7][i]+teams[8][i]
                  for i in range(len(teams[0]))]
    team10start = [teams[0][i]+teams[1][i]+teams[2][i] +
                   teams[3][i]+teams[4][i] + teams[5][i]+teams[6][i] +
                   teams[7][i]+teams[8][i]+teams[9][i]
                   for i in range(len(teams[0]))]
    team11start = [teams[0][i]+teams[1][i]+teams[2][i] +
                   teams[3][i]+teams[4][i] +
                   teams[5][i]+teams[6][i]+teams[7][i]
                   + teams[8][i]+teams[9][i] +
                   teams[10][i] for i in range(len(teams[0]))]
    team12start = [teams[0][i]+teams[1][i]+teams[2][i]+teams[3][i]+teams[4][i]
                   + teams[5][i]+teams[6][i]+teams[7][i] +
                   teams[8][i]+teams[9][i]+teams[10][i] +
                   teams[11][i] for i in range(len(teams[0]))]
    team13start = [teams[0][i]+teams[1][i]+teams[2][i]+teams[3][i]+teams[4][i]
                   + teams[5][i]+teams[6][i]+teams[7][i]+teams[8][i]
                   + teams[9][i]+teams[10][i]+teams[11][i]+teams[12][i]
                   for i in range(len(teams[0]))]

    ax.bar(seasons, teams[0], width=0.2, color='yellow', label='csk')
    ax.bar(seasons, teams[1], bottom=teams[0],
           width=0.2, color='black', label='dc')
    ax.bar(seasons, teams[2], bottom=team2start,
           width=0.2, color='pink', label='dd')
    ax.bar(seasons, teams[3], bottom=team3start,
           width=0.2, color='gold', label='gl')
    ax.bar(seasons, teams[4], bottom=team4start,
           width=0.2, color='tomato', label='kxip')
    ax.bar(seasons, teams[5], bottom=team5start,
           width=0.2, color='purple', label='ktk')
    ax.bar(seasons, teams[6], bottom=team6start,
           width=0.2, color='darkcyan', label='kkr')
    ax.bar(seasons, teams[7], bottom=team7start,
           width=0.2, color='cyan', label='mi')
    ax.bar(seasons, teams[8], bottom=team8start,
           width=0.2, color='red', label='pwi')
    ax.bar(seasons, teams[9], bottom=team9start,
           width=0.2, color='brown', label='rr')
    ax.bar(seasons, teams[10], bottom=team10start,
           width=0.2, color='bisque', label='rpsgs')
    ax.bar(seasons, teams[11], bottom=team11start,
           width=0.2, color='slategrey', label='rpsg')
    ax.bar(seasons, teams[12], bottom=team12start,
           width=0.2, color='lime', label='rcb')
    ax.bar(seasons, teams[13], bottom=team13start,
           width=0.2, color='forestgreen', label='srh')
    plt.legend(title='teams', loc='upper right')

    plt.show()


seasons_and_teamswins = calculate("matches.csv")
seasons_and_teams_totalwins = tranform(seasons_and_teamswins)
print(seasons_and_teamswins.keys())
print(len(seasons_and_teams_totalwins))
plot(seasons_and_teams_totalwins, list(seasons_and_teamswins.keys()))
