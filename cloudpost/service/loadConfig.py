import os
import json


current_dir =  os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'config', 'logConfig.json')

def readStartConfig(self):
    with open(file_path, 'r') as f:
        start =json.load(f)


        self.ui.urlInput.setText(str(start["data"][-1]["url"]))
        self.ui.postInput.setText(str(start["data"][-1]["postData"]))

def loadsConfig(url, postdata):
    with open(file_path, 'r') as f:
        start =json.load(f)
        start["data"].append({"url": url, "postData": postdata})

    with open(file_path, 'w') as f:
        json.dump(start, f, indent=4)