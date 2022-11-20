import csv
import matplotlib.pyplot as plt


def calculate(matches, deliveries):
    '''To calculate'''
    teams = set()
    for match in matches:
        teams.add(match['team1'])
    teams = list(teams)
    runs = [0]*len(teams)
    teamsandscore = dict(zip(teams, runs))
    print(teamsandscore)

    for delivery in deliveries:
        if delivery['batting_team'] in teams:
            teamsandscore[delivery['batting_team']
                          ] += int(delivery['batsman_runs'])

    return teamsandscore


def plot(teams, runs):
    '''To plot'''
    _, aux = plt.subplots()

    blabels = teams

    aux.barh(blabels, runs, label=blabels, color='red')

    aux.set_ylabel('Total runs')
    aux.set_title('max runs scored by each team')
    # ax.legend(title='Teams')

    plt.show()


match_data = []
deliveries_data = []
with open("matches.csv", 'r', encoding='utf-8') as file:
    matche_reader = csv.DictReader(file)

    for matches_data in matche_reader:
        match_data.append(matches_data)

with open("deliveries.csv", 'r', encoding='utf-8') as file:
    deliveries_rerader = csv.DictReader(file)
    for delivery_data in deliveries_rerader:
        deliveries_data.append((delivery_data))

teamsandscore_list = calculate(match_data, deliveries_data)
print(teamsandscore_list)
teams_list = list(teamsandscore_list.keys())
runs_list = list(teamsandscore_list.values())
print(runs_list, teams_list)
plot(teams_list, runs_list)
