import csv 
from Friday_voice_12 import voice
def memory():

    with open('memory.txt', mode='r') as csv_file: # With this you open the file
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(f'\t{row["name"]} {row["lastname"]} is {row["status"]}.')
            line_count += 1
        print(f'Processed {line_count} lines.')

def database(message):

    with open('database.txt', mode='r') as csv_file: #the same here
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row["message"]==message:
                answer=row["answer"]
        return answer

init=0
while True:
    if init==0:
        print('Friday: Hey') 
    init += 1
    
    message=input('You: ')
    ans=database(message)
    print('Friday: '+ans)
    voice(ans)
