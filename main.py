import subprocess, json
# for each gear set,
# for each haste value,
# load the request json
baseInput = open('./inputs/P2PresetBase.json')
baseInputDict = json.load(baseInput)
# modify its bonus haste
iterInputDict = baseInputDict
iterInputDict['raid']['parties'][0]['players'][0]['bonusStats']['stats'][9] = 1000
# write to the temp json
iterInputJSON = json.dumps(iterInputDict, indent=0)
with open("./inputs/CLIInput.json", "w") as outfile:
    outfile.write(iterInputJSON)
# run the sim cli
process = subprocess.run(['../paradigm72-wotlk/wowsimcli-amd64-darwin',
                          '-input',
                          './inputs/CLIInput.json',
                          '--replace='''],
                         stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         universal_newlines=True)
# get the output
output = process.stderr  # why on stderr? :)
# parse the json into a python dictionary
outputDict = json.loads(output)
# extract the DPS value
dps = outputDict['raidMetrics']['dps']['avg']
# store the DPS value in the output dictionary
print(dps)