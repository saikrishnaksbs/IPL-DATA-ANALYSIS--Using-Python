import csv


def calculate(deliveries):
    '''To calculate'''

    batsman = set()
    matchid = 0
    for delivery in deliveries:
        batsman.add(delivery['batsman'])
        if int(delivery['match_id']) > matchid:
            matchid = int(delivery['match_id'])
    batsmanlist = list(batsman)
    batsmanlist=sorted(batsmanlist)
    batsmanscores = dict.fromkeys(batsmanlist, [0, 0])
    b = list(range(1,matchid+1))
    b=[str(i) for i in b]
    b1={}
    for i in b:
        b1[i]=batsmanscores.copy()
    dic1 = {"player": "a", "balls": 999}

    for delivery in deliveri


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

calculate(deliveries_data)
