import itertools
# teams = ['Best-ever', 'Not-so-good', 'Amateurs']
bouquets = itertools.combinations(teams, 2)

for bouquet in bouquets:
    print(bouquet)

