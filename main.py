# for each haste value,
# load the request json
# modify its bonus haste
# write to the temp json
# run the sim cli
import subprocess, json
process = subprocess.run(['/Users/paradigm72/Code/paradigm72-wotlk/wowsimcli-amd64-darwin',
                          '-input',
                          '/Users/paradigm72/Code/paradigm72-wotlk/eleHaste/P2Ele.json',
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