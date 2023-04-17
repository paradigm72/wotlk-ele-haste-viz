import subprocess, json
dpsOutputList = []
# for each gear set,
for phase in range(0, 4):
    # load the request json
    filename = './inputs/P' + str(phase) + 'PresetBase.json'
    baseInput = open(filename)
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
        #
        # get the output
        output = process.stderr  # why on stderr? :)
        # parse the json into a python dictionary
        try:
            simOutputDict = json.loads(output)
        except ValueError as e:
            # print("Parse error (1st pass)")
            try:
                secondProcess = subprocess.run(['../paradigm72-wotlk/wowsimcli-amd64-darwin',
                                          '-input',
                                          './inputs/CLIInput.json',
                                          '--replace='''],
                                         stderr=subprocess.PIPE,
                                         stdout=subprocess.PIPE,
                                         universal_newlines=True)
                output = secondProcess.stderr
                simOutputDict = json.loads(output)
            except ValueError as e:
                # print("Retry failed (2nd pass)")
                continue
        # extract the DPS value
        dps = simOutputDict['raidMetrics']['dps']['avg']
        # compose the DPS value in CSV format
        outputLine = str(phase) + "," + str(haste) + "," + str(dps)
        # debug printing
        print(outputLine)
        # store the DPS value in the list
        outputLine += "\n"
        dpsOutputList.append(outputLine)


# json output
with open("./DPSChart.csv", "w") as outfile:
    outfile.writelines(dpsOutputList)
    outfile.close()
