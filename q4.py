import csv
import matplotlib.pyplot as plt


def calculate(matches):
    '''for calculating'''
    seasons = set()
    teams = set()
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
    played = [0]*len(teams)
    seasons.sort()
    # print(seasons,teams)
    teams_played = dict(zip(teams, played))
    print(teams_played)
    year_team_played = {}
    for year in seasons:
        year_team_played[year] = teams_played.copy()
    print(year_team_played)

    for match in match_data:

        year_team_played[match['season']][match['team1']] += 1
        year_team_played[match['season']][match['team2']] += 1

    year_wise_games = []
    for year in seasons:
        year_wise_games.append(list(year_team_played[year].values()))

    print(year_wise_games)
    return [seasons, year_wise_games]


def tranform(seasons_and_teams_matches):
    '''To trasform'''
    transformed_data = [[row[i] for row in seasons_and_teams_matches]
                        for i in range(len(seasons_and_teams_matches[0]))]

    return transformed_data


def plot(teams, seasons):
    '''for plotting graph'''
    _, aux = plt.subplots()

    teamstart = [teams[0], teams[1]]

    for k in range(2, 14):

        teams_to_consider = [teams[j] for j in range(0, k)]
        valuesof_last_appended_team_ongraph = [sum(group) for group in zip(*teams_to_consider)]
        teamstart.append(valuesof_last_appended_team_ongraph)

    print(teamstart)

    colors = ['yellow', 'black', 'pink', 'gold', 'tomato', 'purple', 'red',
              'cyan', 'brown', 'bisque', 'lime', 'slategrey',
              'forestgreen', 'green']
    labels = ['csk', 'dc', 'dd', 'gl', 'kxip', 'ktk', 'kkr',
              'mi', 'pwi', 'rr', 'rpsgs', 'rpsg', 'rcb', 'srh']
    aux.bar(seasons, teams[0], width=0.2, color=colors[0], label=labels[0])
    aux.bar(seasons, teams[1], bottom=teams[0],
            width=0.2, color=colors[1], label=labels[1])
    for values in range(2, 13):
        aux.bar(seasons, teams[values], bottom=teamstart[values],
                width=0.2, color=colors[values], label=labels[values])
    plt.legend(title='teams', loc='upper right')
    plt.show()


seasons_and_teams_matches_played = calculate("matches.csv")
seasons_and_teams_total = tranform(seasons_and_teams_matches_played[1])
print(seasons_and_teams_total)
plot(seasons_and_teams_total, seasons_and_teams_matches_played[0])
