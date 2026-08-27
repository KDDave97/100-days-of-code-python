

with open("Input/Letters/starting_letter.txt") as file:
    text = file.read()

with open("Input/Names/invited_names.txt") as file:
    names = file.read()

for name in names.split():
    replaced = text.replace("[name]", name)
    with open(f"Output/ReadyToSend/{name}.txt", "w") as saved_text:
        saved_text.write(replaced)



#Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".