CREATE TABLE athletes (
    id SERIAL,
    given_name TEXT,
    surname TEXT
);

CREATE TABLE sexes (
    id SERIAL,
    sex TEXT
);

CREATE TABLE teams (
    id SERIAL,
    name TEXT,
    noc TEXT,
    region TEXT,
    region_note TEXT
);

CREATE TABLE sports (
    id SERIAL,
    name TEXT
);

CREATE TABLE events (
    id SERIAL,
    sport INT,
    name TEXT
);

CREATE TABLE seasons (
    id SERIAL,
    season TEXT
);

CREATE TABLE games (
    id SERIAL,
    year INT,
    season INT,
    city TEXT
);

CREATE TABLE medals (
    id SERIAL,
    type TEXT
);

CREATE TABLE event_results (
	athlete INT,
    athlete_sex INT,
    athlete_age TEXT, 
    athlete_height TEXT, 
    athlete_weight TEXT, 

    team INT,
	event INT,
    game INT,
	medal INT
);