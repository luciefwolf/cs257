#!/usr/bin/env python3
#Written by Lucie Wolf

import sys
import psycopg2
import config


def get_results(title_header, strings_between_row_values, query, parameters):
	'''
	this function takes the parsed information and gets the results using the database

	title_header: the first element in the list, the header for each column of data
	strings_between_row_values: the commands all output different numbers of values, and the final
								format for each row's string will have different amounts of spaces 
								between different values depending on the function and outputs
	query: the query that the function uses on the database
	parameters: the pre-defined second part of cursor.execute() after query that has all the variables 
				used in the query in order
	'''
	
	results = [f'{title_header}\n'] #makes the first element in the list the header

	try:
		#connects to the database
		try:
			connection = psycopg2.connect(database=config.database, user=config.user, password=config.password)
		except Exception as e:
			print(e, file=sys.stderr)
			exit()
		cursor = connection.cursor()

		#execute predefined query
		cursor.execute(query, parameters)

		#loop through rows and create a string from the data, then add each string to the results
		for row in cursor:
			s = ''
			for i in range(len(row)):
				s += f'{row[i]}{strings_between_row_values[i]}' #put the proper space after the given value
			results.append(s)

	except Exception as e:
		print(e, file=sys.stderr)

	connection.close()
	return results


def run_command(args):
	#this function takes the command line arguments and sends them through a series of functions, at which 
	#point this either returns None, which will in tern display the help page, or returns a list of results

	if len(args) >= 2: #check if at least one parameter in addition to olympics.py, otherwise return None
		#checks which function is meant to run and runs that function
		if args[1] == 'athletes_in_NOC':
			return run_athletes_in_NOC(args)
		if args[1] == 'NOC_medals':
			return run_NOC_medals(args)
		if args[1] == 'athlete_medals':
			return run_athlete_medals(args)


def run_athletes_in_NOC(args):
	#run the first command, to print the names of all athletes in a given NOC
	if len(args) == 3: #if too many or too few arguments, return None

		title_header = 'ATHLETE'
		strings_between_row_values = [' ', ''] #space goes between given name and surname, then empty string for the end of the row
		
		query = '''SELECT DISTINCT athletes.given_name, athletes.surname 
				   FROM athletes, teams, event_results
				   WHERE event_results.athlete = athletes.id
				   AND event_results.team = teams.id
				   AND teams.noc = %s
				   ORDER BY athletes.surname;'''
		parameters = (args[2], )

		return get_results(title_header, strings_between_row_values, query, parameters)


def run_NOC_medals(args):
	if len(args) == 2:

		title_header = 'NUM GOLD MEDALS	NOC'
		strings_between_row_values = ['		', '']

		query = '''SELECT SUM(CASE WHEN medals.type = 'Gold' THEN 1 ELSE 0 END), teams.noc
				   FROM teams, medals, event_results
				   WHERE event_results.team = teams.id
				   AND event_results.medal = medals.id
				   GROUP BY teams.noc
				   ORDER BY SUM(CASE WHEN medals.type = 'Gold' THEN 1 ELSE 0 END) DESC, teams.noc;'''
		parameters = ()

		return get_results(title_header, strings_between_row_values, query, parameters)


def run_athlete_medals(args):
	if len(args) == 5:

		title_header = 'NUM MEDALS	ATHLETE'
		strings_between_row_values = [' 		', ' ', '']

		query = '''SELECT SUM(CASE WHEN medals.type = 'NA' THEN 0 ELSE 1 END), athletes.given_name, athletes.surname 
				   FROM athletes, medals, event_results, games, sports, events
				   WHERE event_results.athlete = athletes.id
				   AND event_results.medal = medals.id
				   AND event_results.game = games.id
				   AND event_results.event = events.id
				   AND events.sport = sports.id\n'''
		
		#set initial versions of the three parameters and the parameter tuple
		sport = args[2]
		start_date = args[3]
		end_date = args[4]
		parameters = ()

		#if sport, start, and/or end date are valid parameters, add the relevant line to the query and variable to the parameters tuple
		if sport == '_': #_ indicates in usage.txt that this argument has been skipped, so this turns sport to an empty string
			query += 'AND sports.name ILIKE CONCAT(\'%%\', %s, \'%%\')\n'
			parameters = (*parameters, sport)
		
		if start_date != '_':
			try:
				start_date = int(start_date)
			except:
				return
			query += 'AND games.year >= %s\n'
			parameters = (*parameters, start_date)
		
		if end_date != '_':
			try:
				end_date = int(end_date)
			except:
				return
			query += 'AND games.year <= %s\n'
			parameters = (*parameters, end_date)

		#add the final two lines to the query
		query += '''GROUP BY athletes.surname, athletes.given_name
					ORDER BY SUM(CASE WHEN medals.type = 'NA' THEN 0 ELSE 1 END) DESC, athletes.surname, athletes.given_name;'''

		return get_results(title_header, strings_between_row_values, query, parameters)


def main(args):
	results = run_command(args)

	if not results: #if results == None, there was an issue along the way or the user asked for help, print usage.txt
		usage = open('usage.txt', 'r')
		print(usage.read())
		usage.close()


	elif len(results) <= 1: #if the only item in the results list is the header string, no results were found
		print('No results found.')

	else:
		for result in results:
			print(result)


if __name__ == '__main__':
	main(sys.argv)


