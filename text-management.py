#compare text  use upper() ,lower() method

resident  = "Room"
resident1 = "room"

print(resident.lower() == resident1)

#text connection
language  = "python"
language1 = "Java"
language2 = "HTML"
print(language + " "+language1 + " "+language2)

#List connection
animal = ["Hen","Dog","Bat","Cat"]
print("My animal example is "+ " " .join(animal))

#Split word using split(),splitline() method
sentence = "Sam is running into the rooom"
paragraph ="""Sam is running into the rooom.\nSam is running into the wp.\nSam is running into the garden.\nSam is running into the table.\nSam is running into the forest."""
print(paragraph.splitlines())