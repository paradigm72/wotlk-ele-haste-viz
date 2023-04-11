# for each haste value,
## load the request json
## modify its bonus haste
## write to the temp json
## run the sim cli
import os, json
#stream = os.popen('~/Code/paradigm72-wotlk/wowsimcli-amd64-darwin -input ~/Code/paradigm72-wotlk/eleHaste/P2Ele.json --replace=""')
stream = os.popen('echo test')
output = stream.read()
outputDict = json.loads(output)
print(outputDict['raidMetrics'])
## get the output
## parse the json into a python dictionary
## extract the DPS value
## store the DPS value in the output dictionary