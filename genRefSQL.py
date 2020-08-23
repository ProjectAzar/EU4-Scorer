import os
import re
import csv
import sqlite3

################################
# Helper Functions for Parsers
################################

# Generic helper to format a name
def getName(line):
    name = ""
    lineList = line.split(':')
    name = lineList[1]
    name = re.sub('\d', '', name)
    name = name.strip()
    name = name.replace('"', '')
    return name

# Helpers for Area Name Parser
def getAreaName(line, delim):
    areaName = ""
    lineList = line.split(delim)
    areaName = lineList[0].strip()
    areaName = areaName.replace("_name", '')
    return areaName

# Helper for Province Name Parser
def getProvID(line):
    provID = ""
    lineList = line.split(':')
    provID = lineList[0]
    provID = provID.strip()
    provID = provID[4:]
    return provID

# Helpers for ProvID2Area Parser
def getProvIDList(line):
    provIDList = []
    line = line.strip()
    if len(line) > 0:
        provIDList = line.split(' ')
    return provIDList

# Helpers for Tag Parser
def getTag(line):
    tag = ""
    tagList = line.split(':')
    tag = tagList[0]
    tag = tag.strip()
    return tag


def getTagNC(line):
    tag = ""
    tagList = line.split('=')
    tag = tagList[0]
    tag = tag.strip()
    return tag


def getNameNC(line):
    name = ""
    nameList = line.split('=')
    name = nameList[1]
    name = name.replace('"', '')
    nameList = name.split('/')
    name = nameList[1]
    nameList = name.split('.')
    name = nameList[0]
    return name

#################################
# Helper Functions for Writer
#################################
def getAreaFromProvID(id, areasWithProvID):
    for area in areasWithProvID:
        provList = areasWithProvID[area]
        if id in provList:
            return area

def convertAreaName(areaName):
    areaName = areaName.replace("_area", '')
    areaName = areaName.replace('_',' ')
    areaName = areaName.title()
    return areaName
#################################
# Main
#################################

# Define path to reference files. Update this if scorer breaks or if updates change reference data
# The Emperor DLC added an additional "map" file which needs to be parsed separately as it contains areas not found
# in the area_regions document.
localAreaNamesName = "D:\SteamLibrary\steamapps\common\Europa Universalis IV\localisation\\areas_regions_l_english.yml"
localEmperorAreaName = "D:\SteamLibrary\steamapps\common\Europa Universalis IV\localisation\\emperor_map_l_english.yml"
localProvincesName = "D:\SteamLibrary\steamapps\common\Europa Universalis IV\localisation\prov_names_l_english.yml"
localProvID2Area = "D:\SteamLibrary\steamapps\common\Europa Universalis IV\map\\area.txt"

# !!!!!!!!!!!!!!! Rewrite Parser With Country Tags File !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
localNationTags = "D:\SteamLibrary\steamapps\common\Europa Universalis IV\localisation\countries_l_english.yml"
rawNationTags = "D:\\SteamLibrary\\steamapps\\common\\Europa Universalis IV\\common\\country_tags\\00_countries.txt"

# Open the reference files
if os.path.exists(localAreaNamesName):
    areaNamesFile = open(localAreaNamesName, 'r', encoding="utf8")
else:
    print("No area names file.")
    exit(2)

if os.path.exists(localProvincesName):
    provinceNameFile = open(localProvincesName, 'r', encoding="utf8")
else:
    print("No provinces name file")
    exit(2)

if os.path.exists(localProvID2Area):
    provID2AreaFile = open(localProvID2Area, 'r', encoding="utf8")
else:
    print("No provinces id file.")
    exit(2)

if os.path.exists(localEmperorAreaName):
    emperorNamesFile = open(localEmperorAreaName, 'r', encoding="utf8")
else:
    print("No emperor names")
    exit(2)

if os.path.exists(localNationTags):
    nationTagsFile = open(localNationTags, 'r', encoding="utf8")
else:
    print("No local nation tags")
    exit(2)

if os.path.exists(rawNationTags):
    rawTagsFile = open(rawNationTags, 'r', encoding="utf8")
else:
    print("No raw nation tags")
    exit(2)

# Create dicts to store data from reference files. This data will later be used to add to/update
# referecne table
areaNames = {}
provinceNames = {}
provID2Area = {}
areasWithProvIDs = {}
nationTags = {}

#############
# Parsers
#############

# Area Names Parser
for line in areaNamesFile:
    areaName = ""
    stateName = ""
    if "area_area:" in line:
        continue
    if "_adj" in line:
        continue
    if "_name" in line:
        continue
    else:
        areaName = getAreaName(line, ':')
        stateName = getName(line)
        areaNames[areaName] = stateName

# Emperor Area Parser
for line in emperorNamesFile:
    areaName = ""
    stateName = ""
    if "_area:" in line:
        areaName = getAreaName(line, ':')
        stateName = getName(line)
        areaNames[areaName] = stateName
emperorNamesFile.seek(0)

# Emperor Provinces Parser
for line in emperorNamesFile:
    provID = ""
    provName = ""
    if "PROV_ADJ" in line:
        continue
    elif "PROV" in line:
        provID = getProvID(line)
        provName = getName(line)
        provinceNames[provID] = provName
emperorNamesFile.seek(0)

# Province Names Parser
for line in provinceNameFile:
    provID = ""
    provName = ""
    if "PROV" in line:
        provID = getProvID(line)
        provName = getName(line)
        provinceNames[provID] = provName

# Province IDs to Area Names Parser
for line in provID2AreaFile:   # Advance file to the Land Areas, ignoring sea areas
    if "Land Areas:" in line:
        break
for line in provID2AreaFile:
    areaName = ""
    stack = 0
    if "Deprecated" in line:
        break
    elif "_" in line:
        areaName = getAreaName(line, '=')
        nextLine = provID2AreaFile.readline()
        provIDList = []
        stack = stack + 1
        while stack > 0:
            if "color = " in nextLine:
                nextLine = provID2AreaFile.readline()
                continue
            elif "}" in nextLine:
                stack = stack - 1
            elif len(nextLine) > 0:
                if len(getProvIDList(nextLine)) > 0:
                    provIDList = getProvIDList(nextLine)
                nextLine = provID2AreaFile.readline()

        areasWithProvIDs[areaName]=provIDList

# Nation Tags Parser
for line in nationTagsFile:
    tag = ""
    nationName = ""
    patTag = re.search("[^_][A-Z][A-Z][A-Z]:", line)
    if patTag:
        tag = getTag(line)
        nationName = getName(line)
        nationTags[tag] = nationName

for line in emperorNamesFile:
    tag = ""
    nationName = ""
    patTag = re.search("[^_][A-Z][A-Z][A-Z]:", line)
    if patTag:
        tag = getTag(line)
        nationName = getName(line)
        nationTags[tag] = nationName

for line in rawTagsFile:
    tag = ""
    nationName = ""
    patTag = re.search("^[A-Z][A-Z][A-Z]", line)
    if patTag:
        tag = getTagNC(line)
        nationName = getNameNC(line)
        if tag not in nationTags.keys():
            nationTags[tag] = nationName



#############
# Build provID2Area dict
#############
for key in provinceNames:
    areaName = getAreaFromProvID(key, areasWithProvIDs)
    if areaName:
        provID2Area[key] = areaName

#############
# Add Missing AreaNames
#############
for area in areasWithProvIDs:
    if area not in areaNames:
        stateNameTemp = convertAreaName(area)
        areaNames[area] = stateNameTemp

#############
# Output Results of Parsers to CSV
#############
with open('scorerRefTable.csv', 'w', newline='') as scorerCSV:
    scoreWriter = csv.writer(scorerCSV, delimiter=',')
    scoreWriter.writerow(['provinceID','provinceName','areaName','stateName'])
    provinceID = ""
    provinceName = ""
    areaName = ""
    stateName = ""
    for id in provinceNames:
        provinceID = id
        provinceName = provinceNames[id]
        if id in provID2Area:
            areaName = provID2Area[id]
            stateName = areaNames[areaName]
        scoreWriter.writerow([provinceID, provinceName, areaName, stateName])

#############
# Output Results of Parser to SQLLite DB
#############
# Initialize the SQL Lite Connection
connection = sqlite3.connect("EU4scorer.db")
cursor = connection.cursor()

# Delete Reference Data

# Create providence_reference if it does not exist
sql_command = """
    CREATE TABLE IF NOT EXISTS province_reference (
    provinceID TEXT PRIMARY KEY,
    provinceName TEXT,
    areaName TEXT,
    stateName TEXT);"""
cursor.execute(sql_command)

sql_command = """
    CREATE TABLE IF NOT EXISTS tags_reference (
    tag TEXT PRIMARY KEY,
    nationName TEXT);"""
cursor.execute(sql_command)

#Initialize variables for each row
provinceID = ""
provinceName = ""
areaName = ""
stateName = ""
nationName = ""

#Insert data into providence_reference
for id in provinceNames:
    provinceID = id
    provinceName = provinceNames[id]
    if id in provID2Area:
        areaName = provID2Area[id]
        if"slovakia_area" == areaName:
            print(id)
        stateName = areaNames[areaName]
        cursor.execute("INSERT OR REPLACE INTO province_reference (provinceID, provinceName, areaName, stateName) VALUES (?, ?, ?, ?)",
                  (provinceID, provinceName, areaName, stateName))

#Insert data into tags_reference
for tag in nationTags:
    nationName = nationTags[tag]
    cursor.execute("INSERT OR REPLACE INTO tags_reference (tag, nationName) VALUES (?, ?)",
                   (tag, nationName))

cursor.execute("SELECT * FROM tags_reference")
tagsList = cursor.fetchall()

# Close out of database
connection.commit()
connection.close()

#############
# Close Files
#############

scorerCSV.close()
areaNamesFile.close()
emperorNamesFile.close()
provID2AreaFile.close()
provinceNameFile.close()
