import sqlite3
from prettytable import PrettyTable

#################################
# Open SQL Connection
#################################
connection = sqlite3.connect("EU4scorer.db")
cursor = connection.cursor()

#################################
# Output Player Scores
#################################
cursor.execute("SELECT * FROM player_scores")
playerScores = cursor.fetchall()

print("Score Update: ")
t = PrettyTable(['Name', 'Nation', 'Score'])
for row in playerScores:
    playerName = row[0]
    playerTag = row[1]
    playerNation = row[2]
    playerScore = row[3]
    t.add_row([playerName, playerNation, playerScore])

print(t)

#################################
# Output Scored Areas
#################################

cursor.execute("SELECT * FROM scored_areas")
scoredAreas = cursor.fetchall()

print("\n")
print("Scored Areas:")

t = PrettyTable(['State Name', 'Player'])
for area in scoredAreas:
    areaName = area[0]
    stateName = area[1]
    controllerTag = area[2]
    controllerName = area[3]
    t.add_row([stateName, controllerName])

print(t)