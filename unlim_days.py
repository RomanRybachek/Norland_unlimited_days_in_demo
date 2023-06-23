import re
import sys
import codecs

FIRST_DAY = -10000

# get current day in old save file
def get_current_day(file_body):
    day_occur = re.findall("\"day_current\":-?[0-9]{1,9}\.[0-9]", file_body)[0]
    result = re.findall(r'\d+', day_occur)
    return int(result[0])

if len(sys.argv) == 1:
    print("Give me a save file")
    print("Usage: python unlim_days.py save_file_name.save")
    print("WARNING: DO NOT RUN THE SCRIPT TWICE ON THE SAME SAVE!")
    exit(1)

file_name = sys.argv[1]

file_fd = codecs.open(file_name, "r", encoding="utf_8")
file_body = file_fd.read()
DAY_CURRENT = get_current_day(file_body)

def change_borns():
    all_borns_values = re.findall("\"born\":-?[0-9]{1,9}\.[0-9],", file_body)
    parts_of_file = re.split("\"born\":-?[0-9]{1,9}\.[0-9],", file_body)
    new_file_body = ""

    parts_iter = 0
    for i in all_borns_values:
        born_val = int(re.findall("-?[0-9]{1,9}\.", i)[0][:-1])
        new_born_val = str(FIRST_DAY + born_val)
        new_substr = "\"born\":" + new_born_val + ".0,"

        new_file_body += parts_of_file[parts_iter] + new_substr
        parts_iter += 1
    new_file_body += parts_of_file[parts_iter]
    return new_file_body
# "day_current":-20.0
def change_day_current(file_body):
    day_current_occur = re.findall("\"day_current\":-?[0-9]{1,9}\.[0-9]", file_body)[0]
    parts_of_file = re.split("\"day_current\":-?[0-9]{1,9}\.[0-9]", file_body)
    new_file_body = ""
    new_file_body = parts_of_file[0] + "\"day_current\":" + str(FIRST_DAY + DAY_CURRENT) + ".0" + parts_of_file[1]
    return new_file_body

# "player_data":{"day":-20.0
def change_day_in_player_data(file_body):
    day_occur = re.findall("\"day\":-?[0-9]{1,9}\.[0-9]", file_body)[0]
    parts_of_file = re.split("\"day\":-?[0-9]{1,9}\.[0-9]", file_body)
    new_file_body = parts_of_file[0] + "\"day\":"+ str(FIRST_DAY + DAY_CURRENT) + ".0" + parts_of_file[1]
    return new_file_body

new_file_body = change_borns()
new_file_body = change_day_current(new_file_body)
new_file_body = change_day_in_player_data(new_file_body)

new_save_file_fd = codecs.open("unlim_days.save", "w", encoding="utf_8")
new_save_file_fd.write(new_file_body)
print("Your new save is unlim_days.save. Rename it if you want.")
print("WARNING: DO NOT RUN THE SCRIPT TWICE ON THE SAME SAVE!")
new_save_file_fd.close()

file_fd.close()
