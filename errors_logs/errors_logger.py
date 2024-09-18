import os
import datetime
import json

from settings import ERRORS_LOGS_DIR, ERRORS_LOGS_FILE


def save_error_log(error_text, errors_logs_json=ERRORS_LOGS_FILE):
    cur_time_str = str(datetime.datetime.now())

    if not os.path.exists(errors_logs_json):
        with open(errors_logs_json, 'w') as file:
            file.write(json.dumps({}))

    with open(errors_logs_json, 'r') as file:
        errors_dict = json.load(file)

    errors_dict[cur_time_str] = error_text

    with open(errors_logs_json, 'w') as file:
        new_content = json.dumps(errors_dict, indent=4)
        file.write(new_content)
    print(f'You can see all errors` logs here: {ERRORS_LOGS_FILE}')