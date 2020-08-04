import requests
import matplotlib.pyplot as plt

lobby_type_ranked = 7
account_id = '16767197'

queries = {'limit': 20, 'lobby_type': 7} #lobby type 7 = ranked

res = requests.get(f'https://api.opendota.com/api/players/{account_id}/Matches', params = queries)

data = res.json()

def check_wins(data):
    match_results = []
    for matches in data:
        if matches['radiant_win'] == True and matches['player_slot'] <=127:
            match_results.append('Win')
        elif matches['radiant_win'] == False and matches['player_slot'] >127:
            match_results.append('Win')
        else:
            match_results.append('Loss')
    match_results.reverse() #reverses list to set origin from furthest back requested match
    return match_results

wins = check_wins(data)

def wins_numerically(match_results): #converts list with history of win loss into plot points for scatter plot +1 for a win, -1 for a loss
    match_history = [0]
    for results in match_results:
        if results == 'Win':
            match_history.append(match_history[-1]+1)
        else:
            match_history.append(match_history[-1] -1)
    return match_history

results = wins_numerically(wins)

plt.scatter(range(len(results)), results)
plt.plot(range(len(results)), results)

plt.show()
