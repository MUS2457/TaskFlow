import json
from datetime import datetime

File = "task_summary.json"

def save_json(summary):
    try:
        with open(File) as outfile:
            data = json.load(outfile)
    except (FileNotFoundError, PermissionError, UnicodeDecodeError, OSError):
        data = {}

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data[timestamp] = summary

    with open(File, 'w') as outfile:
        json.dump(data, outfile, indent=4)


def load_json():
    try:
        with open(File) as outfile:
            data = json.load(outfile)
            return data
    except (FileNotFoundError, PermissionError, UnicodeDecodeError, OSError):
        return {}
