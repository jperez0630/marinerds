from pybaseball import statcast,pitching_stats,batting_stats, team_game_logs, team_batting, team_pitching, schedule_and_record
import time, datetime
import pandas as pd
import os
from pathlib import Path
import duckdb

con = duckdb.connect(f'{Path.cwd()}/marinerds_data.duckdb')
local_con = con.cursor()


def get_most_recent_date():
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    yesterday = yesterday.strftime("%Y-%m-%d")
    return yesterday

def get_team_pitching_stats():
    data = team_pitching(2024)
    return data

df_team_pitching_stats =   get_team_pitching_stats()

def get_team_pitching_columns():
    data = df_team_pitching_stats.columns.to_frame().reset_index()
    truncated_data = data[['index']].copy()
    return truncated_data

df_team_pitching_stats_columns = get_team_pitching_columns()



def get_team_batting_stats():
    data = team_batting(2024)
    return data

df_team_batting_stats = get_team_batting_stats()


def get_team_batting_columns():
    data = df_team_batting_stats.columns.to_frame().reset_index()
    truncated_data = data[['index']].copy()
    return truncated_data

df_team_batting_stats_columns = get_team_batting_columns()


def get_rolling_avg(stat):
    batting_logs = team_game_logs(2024, "SEA")
    batting_logs['Date'] = batting_logs['Date'].str.replace(r'\s\(\d+\)', '', regex=True)
    batting_logs['Date'] = pd.to_datetime(batting_logs['Date'] + ' 2024')
    batting_logs['rbi_rolling_avg'] = batting_logs[stat].rolling(window=5).mean()
    data = batting_logs[['Date','rbi_rolling_avg']]
    return data

df_rbi_rolling_avg = get_rolling_avg('RBI')
df_obp_rolling_avg = get_rolling_avg('OBP')


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

# def get_obp_rolling_avg():
#     batting_logs = team_game_logs(2024, "SEA")
#     batting_logs['Date'] = batting_logs['Date'].str.replace(r'\s\(\d+\)', '', regex=True)
#     batting_logs['Date'] = pd.to_datetime(batting_logs['Date'] + ' 2024')
#     batting_logs['obp_rolling_avg'] = batting_logs['OBP'].rolling(window=5).mean()
#     data = batting_logs[['Date','rbi_rolling_avg']]
#     return data

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