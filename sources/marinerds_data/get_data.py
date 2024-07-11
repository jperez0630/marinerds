from pybaseball import statcast, pitching_stats, batting_stats, team_game_logs, team_batting, team_pitching, schedule_and_record, cache
import time, datetime
import pandas as pd
import os
from pathlib import Path
import duckdb


#Part 1: Establish connection to duckdb database, wich is stored in a file named marinerds_data.duckdb 
# This file contains a database with multiple tables that are uploaded to the evidence.app through VSCode

con = duckdb.connect(f'{Path.cwd()}/marinerds_data.duckdb')
local_con = con.cursor()



def get_date_yesterday():
    '''
    This function provides previous day's date in string format
    '''
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    yesterday = yesterday.strftime("%Y-%m-%d")
    return yesterday

yesterday = get_date_yesterday()


def get_team_pitching_stats():
    '''
    Function that pulls in data regarding MLB team pitching statistics
    '''
    data = team_pitching(2024)
    return data

df_team_pitching_stats =  get_team_pitching_stats()


def get_team_pitching_columns():
    '''
    This function returns a list of columns from df_team_pitching_stats data frame. 
    This is used in a drop-down for Team Pitching Stats
    '''
    data = df_team_pitching_stats.columns.to_frame().reset_index()
    truncated_data = data[['index']].copy()
    return truncated_data

df_team_pitching_stats_columns = get_team_pitching_columns()



def get_team_batting_stats():
    '''
    Pulls in data regarding MLB team batting
    '''
    data = team_batting(2024)
    return data

df_team_batting_stats = get_team_batting_stats()


def get_team_batting_columns():
    '''
    This function returns a list of columns from df_team_batting_stats data frame. 
    This is used in a drop-down for Team Batting Stats
    '''
    data = df_team_batting_stats.columns.to_frame().reset_index()
    truncated_data = data[['index']].copy()
    return truncated_data

df_team_batting_stats_columns = get_team_batting_columns()


# def get_rolling_avg(stat):
#     '''
#     This takes the data from the mariners game logs and calculates the
#     5 day rolling average of Runs Batted In.
#     '''
#     batting_logs = team_game_logs(2024, "SEA")
#     batting_logs['Date'] = batting_logs['Date'].str.replace(r'\s\(\d+\)', '', regex=True)
#     batting_logs['Date'] = pd.to_datetime(batting_logs['Date'] + ' 2024')
#     batting_logs['rbi_rolling_avg'] = batting_logs[stat].rolling(window=5).mean()
#     data = batting_logs[['Date','rbi_rolling_avg']]
#     return data

# df_rbi_rolling_avg = get_rolling_avg('RBI')
# df_obp_rolling_avg = get_rolling_avg('OBP')


def get_mariner_game_logs():
    game_logs = team_game_logs(2024, "SEA")
    game_logs['Date'] = game_logs['Date'].str.replace(r'\s\(\d+\)', '', regex=True)
    game_logs['Date'] = pd.to_datetime(game_logs['Date'] + ' 2024')
    game_logs.insert(4, 'Rslt_Outcome', game_logs['Rslt'].str.split(',', expand=True)[0])
    game_logs.insert(5, 'Rslt_Score', game_logs['Rslt'].str.split(',', expand=True)[1])
    game_logs.insert(5, 'Rslt_Score_A', game_logs['Rslt_Score'].str.split('-', expand=True)[0])
    game_logs.insert(6, 'Rslt_Score_B', game_logs['Rslt_Score'].str.split('-', expand=True)[1])
    game_logs[['Rslt_Score_A', 'Rslt_Score_B']] = game_logs[['Rslt_Score_A', 'Rslt_Score_B']].astype(int)
    game_logs.insert(9, 'Run_Differential', '') 
    game_logs['Run_Differential'] = game_logs['Rslt_Score_A'] - game_logs['Rslt_Score_B']

    return game_logs

df_mariner_game_logs = get_mariner_game_logs()


df_mariner_game_logs.loc[(
    df_mariner_game_logs[
        'Rslt_Outcome'
    ] == 'W'
)
&(
    df_mariner_game_logs[
        'Rslt_Score_A'
    ] <= 3
)
]


def get_rolling_avg(df, stat):
    '''
    This takes the data from the mariners game logs and calculates the
    5 day rolling average of Runs Batted In.
    '''
    
    df['rbi_rolling_avg'] = df[stat].rolling(window=5).mean()
    data = df[['Date','rbi_rolling_avg']].copy()
    return data

df_rbi_rolling_avg = get_rolling_avg(df_mariner_game_logs, 'RBI')
df_obp_rolling_avg = get_rolling_avg(df_mariner_game_logs, 'OBP')


def get_pitch_name_columns():
    data = df_mariner_game_logs.columns.to_frame().reset_index()
    truncated_data = data[['index']].copy()
    return truncated_data

df_pitch_name_columns = get_pitch_name_columns()


def get_pitching_stats():
    data = pitching_stats(2024)
    filtered_data = data[['Name','Team','WHIP','ERA','xERA','HardHit%','H/9','BB/9','BABIP']].copy()
    filtered_data.rename(columns={'HardHit%':'Hard_Hit_Percent','H/9':'H_per_9','BB/9':'BB_per_9'},inplace=True)
    return filtered_data

df_filtered_pitching_stats = get_pitching_stats()

def get_league_median_stats():
    league_median_era = df_filtered_pitching_stats.ERA.median()
    league_median_xera = df_filtered_pitching_stats.xERA.median()
    league_median_whip = df_filtered_pitching_stats.WHIP.median()
    league_median_hits_per_9 = df_filtered_pitching_stats.H_per_9.median()
    league_median_bb_per_9 = df_filtered_pitching_stats.BB_per_9.median()
    league_median_hard_hit_percent = df_filtered_pitching_stats.Hard_Hit_Percent.median()
    league_median_babip = df_filtered_pitching_stats.BABIP.median()
    league_median_dict = {
        'Name':'League Median',
        'Team':'N/A',
        'WHIP':league_median_whip,
        'ERA':league_median_era,
        'xERA':league_median_xera,
        'H_per_9':league_median_hits_per_9,
        'BB_per_9':league_median_bb_per_9,
        'Hard_Hit_Percent':league_median_hard_hit_percent,
        'BABIP':league_median_babip
    }
    return league_median_dict

def get_league_best_stats():    
    league_best_whip = df_filtered_pitching_stats.WHIP.min()
    league_best_era = df_filtered_pitching_stats.ERA.min()
    league_best_xera = df_filtered_pitching_stats.xERA.min()
    league_best_hits_per_9 = df_filtered_pitching_stats.H_per_9.min()
    league_best_bb_per_9 = df_filtered_pitching_stats.BB_per_9.min()
    league_best_hard_hit_percent = df_filtered_pitching_stats.Hard_Hit_Percent.min()
    league_best_babip = df_filtered_pitching_stats.BABIP.min()
    league_best_dict = {
        'Name':'League Best',
        'Team':'N/A',
        'WHIP':league_best_whip,
        'ERA':league_best_era,
        'xERA':league_best_xera,
        'H_per_9':league_best_hits_per_9,
        'BB_per_9':league_best_bb_per_9,
        'Hard_Hit_Percent':league_best_hard_hit_percent,
        'BABIP':league_best_babip
    }
    return league_best_dict

def get_league_worst_stats():    
    league_worst_whip = df_filtered_pitching_stats.WHIP.max()
    league_worst_era = df_filtered_pitching_stats.ERA.max()
    league_worst_xera = df_filtered_pitching_stats.xERA.max()
    league_worst_hits_per_9 = df_filtered_pitching_stats.H_per_9.max()
    league_worst_bb_per_9 = df_filtered_pitching_stats.BB_per_9.max()
    league_worst_hard_hit_percent = df_filtered_pitching_stats.Hard_Hit_Percent.max()
    league_worst_babip = df_filtered_pitching_stats.BABIP.max()
    league_worst_dict = {
        'Name':'League Worst',
        'Team':'N/A',
        'WHIP':league_worst_whip,
        'ERA':league_worst_era,
        'xERA':league_worst_xera,
        'H_per_9':league_worst_hits_per_9,
        'BB_per_9':league_worst_bb_per_9,
        'Hard_Hit_Percent':league_worst_hard_hit_percent,
        'BABIP':league_worst_babip
    }
    return league_worst_dict


df_filtered_pitching_stats = get_pitching_stats()

def add_league_stats(df_filtered_pitching_stats):
    df_filtered_pitching_stats = pd.concat([df_filtered_pitching_stats, pd.DataFrame([get_league_median_stats()])], ignore_index=True)
    df_filtered_pitching_stats = pd.concat([df_filtered_pitching_stats, pd.DataFrame([get_league_best_stats()])], ignore_index=True)
    df_filtered_pitching_stats = pd.concat([df_filtered_pitching_stats, pd.DataFrame([get_league_worst_stats()])], ignore_index=True)
    return df_filtered_pitching_stats

df_filtered_pitching_stats = add_league_stats(df_filtered_pitching_stats)

def add_rank():
    df_filtered_pitching_stats['ERA_Rank'] = df_filtered_pitching_stats['ERA'].rank()
    df_filtered_pitching_stats['xERA_Rank'] = df_filtered_pitching_stats['xERA'].rank()
    df_filtered_pitching_stats['WHIP_Rank'] = df_filtered_pitching_stats['WHIP'].rank()
    df_filtered_pitching_stats['H_per_9_Rank'] = df_filtered_pitching_stats['H_per_9'].rank()
    df_filtered_pitching_stats['BB_per_9_Rank'] = df_filtered_pitching_stats['BB_per_9'].rank()
    df_filtered_pitching_stats['Hard_Hit_Percent_Rank'] = df_filtered_pitching_stats['Hard_Hit_Percent'].rank()
    df_filtered_pitching_stats['BABIP_Rank'] = df_filtered_pitching_stats['BABIP'].rank()
    return df_filtered_pitching_stats

add_rank()

def get_mariners_staff_data():
    mariners_staff_data = df_filtered_pitching_stats.loc[df_filtered_pitching_stats['Team'].str.contains('SEA')| df_filtered_pitching_stats['Team'].str.contains('N/A')]
    return mariners_staff_data

df_mariners_staff = get_mariners_staff_data()

def get_game_data():
    data = statcast(start_dt='2024-03-28', end_dt='2024-06-29', team='SEA')
    return data

df_game_data = get_game_data()


def get_zone_results_data():
    groupby_zone = df_game_data.loc[df_game_data['pitch_name'] == '4-Seam Fastball'].groupby(['player_name', 'pitch_name', 'zone']).size().reset_index(name='zone_percentage')
    groupby_zone['zone_percentage'] = groupby_zone['zone_percentage'] / groupby_zone.groupby(['player_name', 'pitch_name'])['zone_percentage'].transform('sum')
    groupby_zone.sort_values(by=['player_name', 'pitch_name', 'zone_percentage'], ascending=False, inplace=True)
    groupby_zone['zone_percentage'] = groupby_zone['zone_percentage'].map('{:.2%}'.format)
    groupby_zone_events = df_game_data.loc[df_game_data['pitch_name'] == '4-Seam Fastball'].groupby(['player_name', 'pitch_name', 'zone'])['events'].value_counts(normalize=True).reset_index(name='events_result')
    groupby_zone_events['events_result'] = groupby_zone_events['events_result'].astype(float).map('{:.2%}'.format)
    merge_zone_results = pd.merge(groupby_zone, groupby_zone_events, on=['player_name', 'pitch_name', 'zone'])
    return merge_zone_results
 
df_groupby_zone_result = get_zone_results_data()

def get_gb_bb_type():
    data = df_game_data.loc[df_game_data['pitch_name'] == '4-Seam Fastball'].groupby(['player_name', 'pitch_name'])['bb_type'].value_counts(normalize=True).reset_index(name='pitch_result')
    data['pitch_result'] = data['pitch_result'].astype(float).map('{:.2%}'.format)
    return data

df_gb_player_bb_type = get_gb_bb_type()

def get_gb_player_events():
    data = df_game_data.loc[df_game_data['pitch_name'] == '4-Seam Fastball'].groupby(['player_name', 'pitch_name'])['events'].value_counts(normalize=True).reset_index(name='result_percent')
    data['result_percent'] = data['result_percent'].astype(float).map('{:.2%}'.format)
    return data

df_gb_player_events = get_gb_player_events()

local_con.sql('''
CREATE OR REPLACE TABLE mariners_pitching_data AS
SELECT * FROM df_mariners_staff
''')

local_con.sql('''
CREATE OR REPLACE TABLE league_pitching_data AS
SELECT * FROM df_filtered_pitching_stats
''')

local_con.sql('''
CREATE OR REPLACE TABLE rbi_rolling_average_data AS
SELECT * FROM df_rbi_rolling_avg
''')

local_con.sql('''
CREATE OR REPLACE TABLE team_batting_data AS
SELECT * FROM df_team_batting_stats
''')

local_con.sql('''
CREATE OR REPLACE TABLE team_batting_data_columns AS
SELECT * FROM df_team_batting_stats_columns
''')

local_con.sql('''
CREATE OR REPLACE TABLE mariner_game_logs AS
SELECT * FROM df_mariner_game_logs
''')

local_con.sql('''
CREATE OR REPLACE TABLE team_pitching_data AS
SELECT * FROM df_team_pitching_stats
''')

local_con.sql('''
CREATE OR REPLACE TABLE team_pitching_data_columns AS
SELECT * FROM df_team_pitching_stats_columns
''')

local_con.sql('''
CREATE OR REPLACE TABLE game_data AS
SELECT * FROM df_game_data
''')

local_con.sql('''
CREATE OR REPLACE TABLE pitch_name_columns AS
SELECT * FROM df_pitch_name_columns
''')

local_con.sql('''
CREATE OR REPLACE TABLE zone_results AS
SELECT * FROM df_groupby_zone_result
''')

local_con.sql('''
CREATE OR REPLACE TABLE gb_player_bb_type AS
SELECT * FROM df_gb_player_bb_type
''')

local_con.sql('''
CREATE OR REPLACE TABLE gb_player_events AS
SELECT * FROM df_gb_player_events
''')