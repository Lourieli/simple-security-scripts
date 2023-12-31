import os
import datetime

# Example: Delete log files older than 7 days
log_directory = "/var/log"
threshold_days = 7

current_time = datetime.datetime.now()

for file in os.listdir(log_directory):
    file_path = os.path.join(log_directory, file)
    if os.path.isfile(file_path):
        modified_time = os.path.getmtime(file_path)
        modified_datetime = datetime.datetime.fromtimestamp(modified_time)
        file_age_days = (current_time - modified_datetime).days
        if file_age_days > threshold_days:
            os.remove(file_path)
            print(f"Deleted file: {file_path} (Modified: {modified_datetime})")
