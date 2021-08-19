# O(N) time | O(T) space - where T is the number of teams
def tournamentWinner(competitions, results):
	
	teams = {}
	
	for team in competitions:
		teams[team[0]] = 0
		teams[team[1]] = 0
		
	for i in range(len(results)):
		if results[i] == 0:
			winner = competitions[i][1]
			teams[winner] += 3
		else:
			winner = competitions[i][0]
			teams[winner] += 3
	
	tournament_winner = max(teams, key=teams.get)
	
	return tournament_winner