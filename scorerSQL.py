import os
import re
import sqlite3

#############################
# Helper Functions
#############################

#############
# Parser Helpers
#############
from typing import Dict, Any


def formatLine(line):
    line = line.strip()
    line = line.replace('"', '')
    return line


def getProvID(line):
    id = line.strip()
    id = id.replace('-', '')
    id = id.replace('={', '')
    return id


def getProvOwner(line):
    owner = line.strip()
    owner = owner.replace("owner=", '')
    owner = owner.replace('"', '')
    return owner


def getDiploValue(line):
    valueList = line.split('=')
    value = valueList[1]
    value = value.strip()
    value = value.replace('"', '')
    return value


def updateSubjectList(nationSubjects, firstNation, secondNation):
    if firstNation in nationSubjects and (len(nationSubjects[firstNation]) > 1):
        subjectList = nationSubjects[firstNation]
        subjectList.append(secondNation)
        return subjectList
    elif firstNation in nationSubjects:
        subjectList = nationSubjects[firstNation]
        subjectList.append(secondNation)
        return subjectList
    else:
        subjectList = []
        subjectList.append(secondNation)
        return subjectList


#############
# Scoring Helpers
#############
def formatCountryTuples(countryList):
    tagNations: Dict[Any, Any] = {}
    for country in countryList:
        tag = country[0]
        nation = country[1]
        tagNations[tag] = nation
    return tagNations


def isOverlord(nationSubjects, owner, subject):
    for nation in nationSubjects:
        if (nation == owner) and (subject in nationSubjects[owner]):
            return True
    return False


def formatTuple(t):
    t = str(t)
    t = t.replace('(','')
    t = t.replace(')','')
    t = t.replace(',','')
    t = t.replace('\'','')
    return t


def getOverlord(nation, nationSubjects):
    for tag in nationSubjects:
        if nation == tag:
            return nation
        elif nation in nationSubjects[tag]:
            return tag
    return nation


def updateControllerList(owner, nationSubjects, controllerList):
    if len(controllerList) == 0:
        controllerList.append(getOverlord(owner, nationSubjects))
        return controllerList
    elif "None" in owner:
        controllerList.append(owner)
        return controllerList
    else:
        overlord = getOverlord(owner, nationSubjects)
        if overlord not in controllerList:
            controllerList.append(overlord)
            return controllerList
    return controllerList


#############################
# File Management
#############################
saveFileName = "C:\\Users\proje\\Documents\Paradox Interactive\Europa Universalis IV\save games\mp_Savoy1508_01_13.eu4"
victoryCardsName = "victory_cards.txt"

if os.path.exists(saveFileName):
    saveFile = open(saveFileName, 'r')
else:
    print("Failed to Open Save File.")
    exit(2)

if os.path.exists(victoryCardsName):
    victoryCardsFile = open(victoryCardsName, 'r', encoding="utf8")
else:
    print("Failed to open victory cards.")
    exit(2)

#############################
# Parsers
#############################
playerNations = {}
provinceOwner = {}
nationSubjects = {}
victoryCards = []

#############
# Player Nation Parser
#############
for line in saveFile:
    if "players_countries=" in line:
        break
while 1:
    line = saveFile.readline()
    if "}" in line:
        break
    else:
        playerName = formatLine(line)
        line = saveFile.readline()
        playerCountry = formatLine(line)
        playerNations[playerName] = playerCountry
saveFile.seek(0)

#############
# Province Parser
#############

for line in saveFile:
    shouldStop = re.search("^provinces={$", line)
    if shouldStop:
        break
stack = 1
id = ""
owner = ""
while stack > 0:
    line = saveFile.readline()
    if "{" in line:
        stack = stack + 1
    if "}" in line:
        stack = stack - 1
    patProvID = re.search("^-[0-9]+={$", line)
    patOwner = re.search("owner=\"[A-Z]{3}\"$", line)
    if stack == 2:
        if patProvID:
            id = getProvID(line)
        if patOwner:
            owner = getProvOwner(line)
            provinceOwner[id] = owner
    if stack == 1:
        if id not in provinceOwner:
            provinceOwner[id] = "None"
id = ""
owner = ""
saveFile.seek(0)

#############
# Subjects Parser
#############
for line in saveFile:
    patDiplo = re.search("^diplomacy={$", line)
    if patDiplo:
        break
stack = 1
firstNation = ""
secondNation = ""
subjectType = ""
subjectNations = []
while stack > 0:
    line = saveFile.readline()
    if "{" in line:
        stack = stack + 1
    if "}" in line:
        stack = stack - 1
    patDepend = re.search("dependency={$", line)
    if patDepend:
        line = saveFile.readline()
        firstNation = getDiploValue(line)
        line = saveFile.readline()
        secondNation = getDiploValue(line)
        line = saveFile.readline()
        if "end_date" in line:
            firstNation = ""
            secondNation = ""
            continue
        else:
            line = saveFile.readline()
            subjectType = getDiploValue(line)
        patSubject = re.search("tributary", subjectType)
        if not patSubject:
            nationSubjects[firstNation] = updateSubjectList(nationSubjects, firstNation, secondNation)

#############
# Victory Card Parser
#############
for line in victoryCardsFile:
    line = line.strip()
    victoryCards.append(line)

#############################
# SQL Setup
#############################
connection = sqlite3.connect("EU4scorer.db")
cursor = connection.cursor()

#############################
# Score Calculation
#############################

#############
# Scorer Setup
#############

# Initialize some variables
playerTag = ""
playerSubjects = ""
playerControlledProvinces = {}
playerControlledAreas = {}
scorePerPlayer = {}
areasAndProvinces = {}
provinceList = []
areaOwners = {}
areaController = {}

# Read in Areas and Provinces from reference DB
cursor.execute("SELECT DISTINCT areaName FROM province_reference")
areas = cursor.fetchall()

for area in areas:
    cursor.execute("SELECT provinceID FROM province_reference WHERE areaName=?",(area))
    provinces = cursor.fetchall()
    area = formatTuple(area)
    provinceList = []
    for province in provinces:
        provinceList.append(formatTuple(province))
    areasAndProvinces[area] = provinceList

# Read in Nation Tags and Nation Names from Reference DB
cursor.execute("SELECT * FROM tags_reference")
countryList = cursor.fetchall()
tagNations = formatCountryTuples(countryList)

#############
# Determine What Nation Controls Each Area
#############

for area in areasAndProvinces:
    provinceList = areasAndProvinces[area]
    owners = []
    for province in provinceList:
        owner = provinceOwner[province]
        owners.append(owner)
    areaOwners[area] = owners

for area in areaOwners:
    ownersList = areaOwners[area]
    controllerList = []
    for owner in ownersList:
        controllerList = updateControllerList(owner, nationSubjects, controllerList)
    if "None" in controllerList:
        areaController[area] = "None"
    elif len(controllerList) > 1:
        areaController[area] = "None"
    else:
        areaController[area] = controllerList[0]

#############
# Score Calculation Per Player
#############
playerTagList = []

for player in playerNations:
    playerTagList.append(playerNations[player])

for tag in playerTagList:
    score = 0
    for area in areaController:
        if (areaController[area] == tag) and (area in victoryCards):
            score = score + 1
    scorePerPlayer[tag] = score

#############################
# Output to Database
#############################

# Output scores to terminal
print("Score Update: ")
for player in playerNations:
    tag = playerNations[player]
    print("Player: " + player + " Country: " + tag + " Score: " + str(scorePerPlayer[tag]))

#############
# Setup Score Tables
#############
# Setup Player Score Table. As scores are dynamic, and historic scores are unnecessary, we can recreate the table with
# each update
cursor.execute("DROP TABLE IF EXISTS player_scores;")
cursor.execute("CREATE TABLE IF NOT EXISTS player_scores(playerName TEXT PRIMARY KEY, tag TEXT, nation TEXT, score INT);")
# Setup Area Controller Table. As scores are dynamic, and historic scores are unnecessary, we can recreate the table
# with each update
cursor.execute("DROP TABLE IF EXISTS scored_areas;")
cursor.execute("CREATE TABLE IF NOT EXISTS scored_areas(areaName TEXT PRIMARY KEY, stateName TEXT, controllerTag TEXT, playerName TEXT);")


#############
# Output Player Info and Scores to player_scores table
#############
for player in playerNations:
    playerName = player
    playerTag = playerNations[player]
    playerNation = tagNations[playerTag]
    playerScore = scorePerPlayer[playerTag]

    cursor.execute("INSERT OR REPLACE INTO player_scores (playerName, tag, nation, score) VALUES(?,?,?,?)",
                   (playerName, playerTag, playerNation, playerScore))

#############
# Output scoring area info to areas_scored table
#############

for player in playerNations:
    playerName = player
    playerTag = playerNations[player]
    for area in areaController:
        if (areaController[area] == playerTag) and (area in victoryCards):
            cursor.execute("SELECT DISTINCT stateName FROM province_reference WHERE areaName=?",(area,))
            stateName = cursor.fetchall()
            stateName = formatTuple(stateName[0])
            cursor.execute("INSERT OR REPLACE INTO scored_areas(areaName, stateName, controllerTag, playerName) VALUES (?,?,?,?)",
                          (area, stateName, playerTag, playerName))

#############################
# Cleanup
#############################
# Cleanup SQL
connection.commit()
connection.close()

# Cleanup Files
saveFile.close()
victoryCardsFile.close()
