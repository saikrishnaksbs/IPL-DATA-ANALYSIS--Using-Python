import csv
import matplotlib.pyplot as plt


def calculate(matches, deliveries):
    '''For calculating'''

    matchids = []
    for match in matches:
        if match['season'] == '2015':
            matchids.append(match['id'])

    print(matchids)
    bowlerslist = set()
    for delivery in deliveries:

        if delivery['match_id'] in matchids:
            bowlerslist.add(delivery['bowler'])
    bowlerslist = sorted(list(bowlerslist))
    runsgiven = [0]*len(bowlerslist)
    bowler_runs = dict(zip(bowlerslist, runsgiven))
    print(bowler_runs)

    for delivery in deliveries_data:
        if (delivery['bowler'] in bowler_runs.keys()
                and delivery['match_id'] in matchids):
            bowler_runs[delivery['bowler']] += int(delivery['total_runs'])
    print(bowler_runs)

    sorted_bowler_runs_given = {key: value for key, value in sorted(
        bowler_runs.items(), key=lambda item: item[1])}

    print(sorted_bowler_runs_given)
    return sorted_bowler_runs_given

    # worstbowlers=(list(sorted_dict.values()))
    # totalruns=(list(sorted_dict.keys()))
    # print( worstbowlers.reverse() , totalruns.reverse())


def plot(players, runsgiven):
    '''function for plotting'''
    _, aux = plt.subplots()

    blabels = players[-10:]

    aux.bar(blabels,    runsgiven[-10:], label=blabels, color='red')

    aux.set_ylabel('Total runs')
    aux.set_title('Top 10 economical bowlers in the year 2015')
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


sorted_bowler_runs = calculate(match_data, deliveries_data)
players_name = list(sorted_bowler_runs.keys())
runs = list(sorted_bowler_runs.values())
plot(players_name, runs)
