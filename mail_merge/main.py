names = []

with open("mail_merge/Input/Names/invited_names.txt", mode="r") as filename:
    line = filename.readline()
    while line:
        names.append(line.strip())
        line = filename.readline()
    
for each_name in names:
    current_file_path = f"mail_merge/Output/ReadyToSend/letter_for_{each_name}.txt"
    with open('mail_merge/Input/Letters/starting_letter.txt', 'r') as f:
        data = f.readlines() # read all lines as a list
        data[0] = data[0].replace('[name]', each_name) 

    with open(current_file_path, 'w') as f:
        f.writelines(data)