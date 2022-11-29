import csv
import matplotlib.pyplot as plt


def calculate(matches, deliveries):
    '''function for calculating'''

    runs_per_team = []
    matchids = []
    for details in matches:
        if details['season'] == '2016':
            matchids.append(details['id'])
    print(matchids)
    teams = set()
    for details in deliveries:
        if details['match_id'] in matchids:
            teams.add(details['bowling_team'])
    teams = sorted(list(teams))
    runs_per_team = [0]*len(teams)
    teams_extraruns = dict(zip(teams, runs_per_team))

    for details in deliveries:
        if (details['bowling_team'] in teams_extraruns.keys()
                and details['match_id'] in matchids):
            teams_extraruns[details['bowling_team']
                            ] += int(details['extra_runs'])

    return teams_extraruns


def plot(teams, runsperteam):
    '''function for plotting'''
    _, aux = plt.subplots()
    blabels = teams
    aux.barh(blabels, runsperteam, label=blabels, color='green')

    aux.set_ylabel('Runsperteam')
    aux.set_title('Teams')
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


seasonsandmatches = calculate(match_data, deliveries_data)
print(seasonsandmatches)

players = list(seasonsandmatches.keys())
runs = list(seasonsandmatches.values())
plot(players, runs)
