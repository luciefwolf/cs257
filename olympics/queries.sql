SELECT DISTINCT noc FROM teams
	ORDER BY noc;


SELECT DISTINCT athletes.given_name, athletes.surname
	FROM athletes, event_results, teams
	WHERE athletes.id = event_results.athlete
	AND event_results.team = teams.id
	AND teams.region = 'Jamaica'
	ORDER BY athletes.surname;


SELECT athletes.given_name, athletes.surname, sexes.sex, teams.name, sports.name, events.name, seasons.season, games.year, games.city, medals.type, event_results.athlete_age, event_results.athlete_height, event_results.athlete_weight
	FROM athletes, sexes, teams, sports, events, seasons, games, medals, event_results
	WHERE event_results.athlete = athletes.id
	AND event_results.athlete_sex = sexes.id
	AND event_results.team = teams.id
	AND event_results.event = events.id
	AND event_results.game = games.id
	AND event_results.medal = medals.id
	AND events.sport = sports.id 
	AND games.season = seasons.id
	AND athletes.given_name LIKE '%Greg%'
	AND athletes.surname = 'Louganis'
	AND NOT medals.type = 'NA'
	ORDER BY games.year;


SELECT teams.noc, SUM(CASE WHEN medals.type = 'Gold' THEN 1 ELSE 0 END) 
	FROM teams, medals, event_results
	WHERE event_results.team = teams.id
	AND event_results.medal = medals.id
	GROUP BY teams.noc
	ORDER BY SUM(CASE WHEN medals.type = 'Gold' THEN 1 ELSE 0 END) DESC;