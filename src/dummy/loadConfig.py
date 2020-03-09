import json 

def loadConfig(path='.config/brokerConfig.json'): 
    # read config and return, print for debug 
    with open(path) as f: 
        config = json.load(f)
    print(config['data_topic'])
    return config

loadConfig()

