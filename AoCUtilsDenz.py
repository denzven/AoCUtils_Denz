import os
import requests
from bs4 import BeautifulSoup


def BoilerPlate(SesssionCookie):
    """
    Setup for the Boilerplate code with Inputs and Questions automatically filled in,
    Using the session-id to login and get all info.
    """
    year_dir = [year for year in range(2015, 2022)]
    day_dir = [f"Day{day}" for day in range(26)]
    files_dir = ["%Input.txt", "%Part1.py", "%Part2.py", "%Ques.txt", "README_%.md"]
    main_dir = "AdventOfCode"
    i = 0
    Part1_Counter = 0
    Part2_Counter = 0

    for year in year_dir:
        for day in day_dir:
            if i > 25:
                i = 0
            if Part1_Counter > 25:
                Part1_Counter = 0
            if Part2_Counter > 25:
                Part2_Counter = 0

            for file in files_dir:
                req_file = f"{main_dir}/{year}/{day}/{file.replace('%',day)}"
                path = f"{main_dir}/{year}/{day}"

                if not os.path.exists(path):
                    os.makedirs(path)
                with open(os.path.join(path, file.replace("%", day)), "w+") as f:

                    # Inputs
                    if f.name.endswith("Input.txt"):

                        print(f"https://adventofcode.com/{year}/day/{i}/input")
                        cookie = {"Cookie": SesssionCookie}
                        Input_txt = requests.get(
                            f"https://adventofcode.com/{year}/day/{i}/input",
                            headers=cookie,
                        )
                        Input_txtQues = requests.get(
                            f"https://adventofcode.com/{year}/day/{i}", headers=cookie
                        )
                        ErrorMsg = "please don't repeatedly request this endpoint before it unlocks! the calendar countdown is synchronized with the server time; the link will be enabled on the calendar the instant this puzzle becomes available."
                        NotFoundMsg = "404 not found"

                        if NotFoundMsg in str(Input_txt.text).lower():
                            print("This puzzle doesnt exist")
                            pass

                        elif ErrorMsg in str(Input_txt.text).lower():
                            print("This Input is not unlocked yet")
                            return

                        else:
                            f.write(Input_txt.text)

                        i += 1

                    # BoilerPlateCode
                    if f.name.endswith("Part1.py"):
                        if Part1_Counter == 0:
                            Part1_Counter += 1
                            pass
                        else:

                            BoilerPlateCode = """
#Part 1 of Day%

import time
StartTime = time.time()
InputFileLines = open('Day%Input.txt').readlines()

#Code

FinalAnswer = 

EndTime = time.time()
print(f"Final score: {FinalAnswer}")
print(f'Execution Time: {EndTime - StartTime}')
"""
                            f.write(BoilerPlateCode.replace("%", str(Part1_Counter)))
                            Part1_Counter += 1

                    # BoilerPlateCode
                    if f.name.endswith("Part2.py"):
                        if Part2_Counter == 0:
                            Part2_Counter += 1
                            pass
                        else:

                            BoilerPlateCode = """
#Part 2 Day%

import time
StartTime = time.time()
InputFileLines = open('Day%Input.txt').readlines()

#Code

FinalAnswer = 

EndTime = time.time()
print(f"Final score: {FinalAnswer}")
print(f'Execution Time: {EndTime - StartTime}')
"""
                            f.write(BoilerPlateCode.replace("%", str(Part2_Counter)))
                            Part2_Counter += 1

                    if f.name.endswith("Ques.txt"):
                        InputContent = Input_txtQues.text
                        InputSoup = BeautifulSoup(InputContent)
                        # print(InputSoup.get_text())
                        try:
                            text = str(InputSoup.body.main.article.text)
                            f.write(text)
                        except Exception as e:
                            print(e)
