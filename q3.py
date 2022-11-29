import csv
import matplotlib.pyplot as plt


def calculate(matches):
    '''function for calculating'''
    totalcountries = []
    noofumpires = []
    umpires1 = set()
    for umpires in matches:

        umpires1.add(umpires['umpire1'])
        umpires1.add(umpires['umpire2'])

    umpires1 = list((umpires1))
    umpires1.sort()
    del umpires1[0]
    nationality = ['ind', 'ind', 'ind', 'nz', 'ind', 'ind', 'ind', 'pak',
                   'pak', 'aus', 'aus', 'aus', 'wi', 'ind', 'nz', 'ind',
                   'aus', 'ind', 'aus', 'sl', 'ind', 'sa', 'sa', 'ind',
                   'ind', 'ind', 'ind', 'ind', 'sa', 'eng', 'aus', 'ind',
                   'ind', 'aus', 'zim', 'aus', 'eng', 'ind', 'ind', 'ind',
                   'ind', 'aus', 'ind', 'ind', 'ind', 'ind', 'ind', 'ind',
                   'ind', 'ind', 'sl', 'ind', 'ind', 'ind']

    totalcountries = list(set(nationality))
    totalcountries.remove('ind')
    print(totalcountries)
    noofumpires = []
    for i in totalcountries:
        noofumpires.append(nationality.count(i))
    print(noofumpires)
    umpires_with_nationality_finallist = dict(zip(totalcountries, noofumpires))
    return umpires_with_nationality_finallist


def plot(totalcountries, noofumpires):
    '''function for plotting'''
    _, aux = plt.subplots()

    blabels = totalcountries

    aux.bar(blabels,  noofumpires, label=blabels, color='red')

    aux.set_ylabel(' Foreign umpire analysis')
    aux.set_title('no umpires')
    # ax.legend(title='Teams')

    plt.show()


match_data = []

with open("matches.csv", 'r', encoding='utf-8') as file:
    matche_reader = csv.DictReader(file)

    for match in matche_reader:
        match_data.append(match)


umpire_with_nationality_finallist = calculate(match_data)
print(umpire_with_nationality_finallist)

players = list(umpire_with_nationality_finallist.keys())
runs = list(umpire_with_nationality_finallist.values())

plot(players, runs)
