# Norland_unlimited_days_in_demo
This script allows you to bypass 15-days restriction in Norland demo game.
# How to use:
1) Install python 3, during the installation check the "Add to PATH" box
2) Looking for the path to the saves, it's about this:
C:\Users\\%USER%\\AppData\Local\Strategy\saves
4) Open command line and change directory in your command line to saves directory. Example: cd C:\Users\\%USER%\\AppData\Local\Strategy\saves
5) Run from the command line: python unlim_days.py name_your_save.save
6) A new save will appear - unlim_days.save, load from it.
# How it works:
This script finds and changes the day_current, player_data : day, and all born fields to negative values.
The game does not check if current day value is negative and allow you to play from -1000 day to 15.
The "born" values have been changed because otherwise the age of the characters would not be correct
