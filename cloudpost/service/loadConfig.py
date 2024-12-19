import os
import json


getDir =  os.path.dirname(os.path.dirname(__file__))
configDir = os.path.join(getDir, 'config', 'logConfig.json')

def readStartConfig(self):
    with open(configDir, 'r') as f:
        start =json.load(f)


        self.ui.urlInput.setText(str(start["data"][-1]["url"]))
        self.ui.postInput.setText(str(start["data"][-1]["postData"]))

def loadsConfig(url, postdata):
    with open(configDir, 'r') as f:
        start =json.load(f)
        start["data"].append({"url": url, "postData": postdata})

    with open(file_path, 'w') as f:
        json.dump(start, f, indent=4)
