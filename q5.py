import csv
import matplotlib.pyplot as plt


def calculate(matches):
    '''function for calculating'''
    seasons = set()

    for details in matches:

        seasons.add(details['season'])

    seasons = sorted(list((seasons)))
    print(seasons)
    matchcount = [0]*len(seasons)
    seasons_and_matches = dict(zip(seasons, matchcount))
    for details in matches:
        if details['season'] in seasons_and_matches.keys():
            seasons_and_matches[details['season']] += 1

    return seasons_and_matches


def plot(seasons, matches):
    '''function for plotting'''
    _, ax = plt.subplots()

    blabels = seasons

    ax.bar(blabels, matches, label=blabels, color='red')

    ax.set_ylabel('Total matches')
    ax.set_title(
        '5. Number of matches played per year for all the years in IPL.')
    # ax.legend(title='Teams')

    plt.show()


match_data = []
deliveries_data = []
with open("matches.csv", 'r', encoding='utf-8') as file:
    matche_reader = csv.DictReader(file)

    for match in matche_reader:
        match_data.append(match)

with open("deliveries.csv", 'r', encoding='utf-8') as file:
    deliveries = csv.DictReader(file)
    for delivery in deliveries:
        deliveries_data.append((delivery))

seasonsandmatches = calculate(match_data)
print(seasonsandmatches)
players = list(seasonsandmatches.keys())
runs = list(seasonsandmatches.values())
plot(players, runs)
