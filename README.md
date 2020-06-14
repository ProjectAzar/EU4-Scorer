# EU4-Scorer
## Purpose
EU4 Scorer is a Python3 script used to calculate the score of each nation in a custom EU4 game. Score is determined by awarding one point to a nation that controls and full cores a state on the custom victory cards list. The script outputs a CSV document titled "scoreList.csv" which can be used in another program to visualize the scores. The score file is saved with a time stamp, and is overwritten with each run. Be sure to save any backups should you wish to keep old scores. 

## Requirements
* Python 3.3 or later
* An uncompressed EU4 save. Note: Scorer will not work on Ironman saves. 
* A list of areas to act as victory cards. Areas must be named as they appear in the save file, without "_area" on the end of the string. Ex. "An Nafud" is "nafud".

## Usage

`python3 scorecount.py <save>.txt <victory_cards>.txt

## TODO
* Add error checking 
* Implement all nation tags in the nation table 
* Add better comments
* Pipe output to a shareable Google Sheets document 
* Avoid overwritting score output
