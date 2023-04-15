import subprocess, json, time
# for each gear set,
# load the request json
baseInput = open('./inputs/P2PresetBase.json')
baseInputDict = json.load(baseInput)
iterInputDict = baseInputDict
# for each haste value,
for haste in range(-1000, 1000):
    # modify its bonus haste
    iterInputDict['raid']['parties'][0]['players'][0]['bonusStats']['stats'][9] = haste
    # write to the temp json
    iterInputJSON = json.dumps(iterInputDict, indent=0)
    with open("./inputs/CLIInput.json", "w") as outfile:
        outfile.write(iterInputJSON)
        outfile.close()
    # run the sim cli
    process = subprocess.run(['../paradigm72-wotlk/wowsimcli-amd64-darwin',
                          '-input',
                          './inputs/CLIInput.json',
                          '--replace='''],
                         stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         universal_newlines=True)
    # time.sleep(2)
    # get the output
    output = process.stderr  # why on stderr? :)
    # parse the json into a python dictionary
    outputDict = json.loads(output)
    # extract the DPS value
    dps = outputDict['raidMetrics']['dps']['avg']
    # store the DPS value in the output dictionary
    print(dps)