'''
Lucie Wolf

Source code from:
https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results?resource=download

Data from noc_regions.csv is in the format:
NOC,region,notes

Data from athlete_events.csv is in the format:
"ID","Name","Sex","Age","Height","Weight","Team","NOC","Games","Year","Season","City","Sport","Event","Medal"
'''

import csv


nocs = {}

with open('noc_regions.csv') as noc_regions_data_file:
    reader = csv.reader(noc_regions_data_file)
    next(reader)

    for row in reader:
        noc = row[0]
        region = row[1]
        note = row[2]
        nocs[noc] = [region, note]


athletes = []
sexes = []
teams = []
sports = []
events = []
seasons = []
games = []
medals = []
events = []


with open('athlete_events.csv') as original_data_file,\
        open('athletes.csv', 'w') as athletes_file,\
        open('sexes.csv', 'w') as sexes_file,\
        open('teams.csv', 'w') as teams_file,\
        open('sports.csv', 'w') as sports_file,\
        open('events.csv', 'w') as events_file,\
        open('seasons.csv', 'w') as seasons_file,\
        open('games.csv', 'w') as games_file,\
        open('medals.csv', 'w') as medals_file,\
        open('event_results.csv', 'w') as event_results_file:

    reader = csv.reader(original_data_file)
    athletes_writer = csv.writer(athletes_file)
    sexes_writer = csv.writer(sexes_file)
    teams_writer = csv.writer(teams_file)
    sports_writer = csv.writer(sports_file)
    events_writer = csv.writer(events_file)
    seasons_writer = csv.writer(seasons_file)
    games_writer = csv.writer(games_file)
    medals_writer = csv.writer(medals_file)
    event_results_writer = csv.writer(event_results_file)

    next(reader) # eat up and ignore the heading row of the data file

    for row in reader:
        #athlete information
        athlete_id = int(row[0])
        if athlete_id not in athletes:
            athletes.append(athlete_id)
            athlete_full_name = row[1]
            athlete_names = athlete_full_name.split(' ')
            athlete_surname = athlete_names[-1]
            athlete_given_name = ' '.join(athlete_names[:-1])
            athletes_writer.writerow([athlete_id, athlete_given_name, athlete_surname])


        #sex information
        sex = row[2]
        if sex not in sexes:
            sex_id = len(sexes) + 1
            sexes.append(sex)
            sexes_writer.writerow([sex_id, sex])


        #team information
        team = row[6]
        if team not in teams:
            team_id = len(teams) + 1
            teams.append(team)

            noc = row[7]
            try: #some nocs appear not to appear in the noc_regions csv file
                noc_region_information = nocs[noc]
                noc_region = noc_region_information[0]
                noc_note = noc_region_information[1]
            except:
                noc_region = 'unknown'
                noc_note = ''
            teams_writer.writerow([team_id, team, noc, noc_region, noc_note])


        #sport information
        sport = row[12]
        if sport not in sports:
            sport_id = len(sports) + 1
            sports.append(sport)
            sports_writer.writerow([sport_id, sport])


        #event information
        event = row[13]
        if event not in events:
            event_id = len(events) + 1
            events.append(event)
            event_sport_id = sports.index(sport) + 1
            events_writer.writerow([event_id, event_sport_id, event])


        #season information
        season = row[10]
        if season not in seasons:
            season_id = len(seasons) + 1
            seasons.append(season)
            seasons_writer.writerow([season_id, season])


        #game information
        game = row[8]
        if game not in games:
            game_id = len(games) + 1
            games.append(game)
            year = int(row[9])
            game_season_id = seasons.index(season) + 1
            city = row[11]
            games_writer.writerow([game_id, year, game_season_id, city])


        #medal information
        medal = row[14]
        if medal not in medals:
            medal_id = len(medals) + 1
            medals.append(medal)
            medals_writer.writerow([medal_id, medal])


        #all event result information
        sex = sexes.index(sex) + 1
        age = row[3]
        height = row[4]
        weight = row[5]

        team = teams.index(team) + 1
        event = events.index(event) + 1
        game = games.index(game) + 1
        medal = medals.index(medal) + 1
        event_results_writer.writerow([athlete_id, sex, age, height, weight, team, event, game, medal])
        


