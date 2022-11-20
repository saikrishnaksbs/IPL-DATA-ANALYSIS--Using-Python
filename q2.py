import csv
import matplotlib.pyplot as plt


def calculate(matches, deliveries):
    '''A function for calculating'''

    match_data = []
    deliveries_data = []
    with open(matches, 'r', encoding='utf-8') as file:
        matche_reader = csv.DictReader(file)

        for match in matche_reader:
            match_data.append(match)

    with open(deliveries, 'r', encoding='utf-8') as file:
        deliveries = csv.DictReader(file)
        for delivery in deliveries:
            deliveries_data.append((delivery))

    topplayers = set()

    for player in deliveries_data:
        if player['batting_team'] == 'Royal Challengers Bangalore':
            topplayers.add(player['batsman'])
    topplayers = list(topplayers)
    runsscored = [0]*len(topplayers)
    each_players_and_runs = dict(zip(topplayers, runsscored))
    for player in deliveries_data:
        if player['batsman'] in each_players_and_runs.keys():
            each_players_and_runs[player['batsman']
                                  ] += int(player['batsman_runs'])
    print(each_players_and_runs)
    sorted_each_players_and_runs = {key: value for key, value in sorted(
        each_players_and_runs.items(), key=lambda item: item[1])}
    print(sorted_each_players_and_runs)
    return sorted_each_players_and_runs


def transform(players_and_runs_scored):
    '''To transform'''
    players = list(players_and_runs_scored.keys())[-10:]
    runs = list(players_and_runs_scored.values())[-10:]
    return [players, runs]


def plot(players, runs):
    '''for plotting '''
    _, aux = plt.subplots()

    blabels = players

    aux.bar(blabels, runs, label=blabels, color='red')

    aux.set_ylabel('Total runs')
    aux.set_title('max runs scored by a batsman in Ipl for rcb')
    # ax.legend(title='Teams')

    plt.show()


players_and_runs = calculate("matches.csv", "deliveries.csv")
print(players_and_runs)
runs_per_player = transform(players_and_runs)

plot(runs_per_player[0], runs_per_player[1])
