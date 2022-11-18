import time
import csv
from pathlib import Path

def main():
    participant = input("Enter participant name >> ")
    sepFilePath = Path(f'separate/logs_{participant}.csv')
    filePath = Path('logs.csv')
    print(":: Welcome to the Text Entry Evaluation terminal ::")
    print(":: Please choose a lesson by inputting a number (0 - 6) ::")

    # select lesson
    valid_lessons = ["0", "1", "2", "3", "4", "5", "6"]
    while True:
        lesson_num = input("Select Lesson >> ")
        if lesson_num in valid_lessons:
            break
        else:
            print("ERROR: Please select a valid lesson")

    # load phrases
    file = open("lessons/lesson" + lesson_num + ".txt", "r")
    lines = file.readlines()
    print("File loaded successfully.\n")
    
    if not filePath.exists():
    	with open(filePath, 'w', newline='') as logs_csv:
    		logs_csv_write = csv.writer(logs_csv)
    		logs_csv_write.writerow(['Participant', 'Lesson','Prompt', 'Start', 'End', 'Time Lapsed (s)', 'Word Count', 'Character Count', 'WPM', 'CPM'])
    		#logs_csv_write.writerow(['Lesson','Prompt', 'Start', 'End', 'Time Lapsed (s)', 'Word Count', 'WPM'])
    		
    if not sepFilePath.exists():
    	with open(sepFilePath, 'w', newline='') as sep_csv:
    		sep_csv_write = csv.writer(sep_csv)
    		sep_csv_write.writerow(['Lesson','Prompt', 'Start', 'End', 'Time Lapsed (s)', 'Word Count', 'Character Count', 'WPM', 'CPM'])

    # perform entry study and calculate WPM each line
    print(":: For each input prompt, please press Enter to start typing ::")
    print(":: and press Enter again to stop typing, WPM metrics will be ::")
    print(":: calculated by using the time between two Enter key press. ::\n")

    for line in lines:
        input("Prompt: " + line.strip())
        start = time.time()
        input(">> ")
        end = time.time()
        time_lapsed = end - start
        word_count = len(line.split())
        str_count = len(line)
        print("Time Lapsed: " + str(round(time_lapsed, 6)) + "s")
        print("WPM: " + str(round(60.0 / time_lapsed * word_count, 6)))
        print("CPM: " + str(round(60.0 / time_lapsed * str_count, 6))+ "\n")
        with open(filePath, 'a', newline='') as logs_csv:
        	logs_csv_append = csv.writer(logs_csv)
        	logs_csv_append.writerow([participant, lesson_num, line.strip(), time.asctime(time.localtime(start)), time.asctime(time.localtime(end)), round(time_lapsed, 6), word_count, str_count, round(60.0 / time_lapsed * word_count, 6), round(60.0 / time_lapsed * str_count, 6)])

        with open(sepFilePath, 'a', newline='') as sep_csv:
        	sep_csv_append = csv.writer(sep_csv)
        	sep_csv_append.writerow([lesson_num, line.strip(), time.asctime(time.localtime(start)), time.asctime(time.localtime(end)), round(time_lapsed, 6), word_count, str_count, round(60.0 / time_lapsed * word_count, 6), round(60.0 / time_lapsed * str_count, 6)])

    # study end
    print(":: Evaluation complete! Press Y/N to continue ::")
    while True:
    	enter = input().lower()
    	if enter == "y":
    		main()
    	elif enter == "n":
    		exit()
    	else:
    		print("Please choose Y/N")

if __name__ == "__main__":
    main()
