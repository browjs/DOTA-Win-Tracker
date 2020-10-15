import requests
import matplotlib.pyplot as plt

match_input = input(
    'How many previous matches would you like to see? enter 0 for maximum  ')

account_id = '' #Enter account ID here
queries = {'limit': match_input, 'lobby_type': 7}  # lobby type 7 = ranked

res = requests.get(
    f'https://api.opendota.com/api/players/{account_id}/Matches', params=queries)
data = res.json()


def check_wins(data):
    match_results = []
    for matches in data:
        if matches['radiant_win'] == True and matches['player_slot'] <= 127:
            match_results.append('Win')
        elif matches['radiant_win'] == False and matches['player_slot'] > 127:
            match_results.append('Win')
        else:
            match_results.append('Loss')
    # reverses list to set origin from furthest back requested match
    match_results.reverse()
    return match_results


wins = check_wins(data)


# converts list with history of win loss into plot points for scatter plot +1 for a win, -1 for a loss
def wins_numerically(match_results):
    match_history = [0]
    for results in match_results:
        if results == 'Win':
            match_history.append(match_history[-1]+1)
        else:
            match_history.append(match_history[-1] - 1)
    return match_history


results = wins_numerically(wins)

plt.scatter(range(len(results)), results)
plt.plot(range(len(results)), results)

plt.show()
