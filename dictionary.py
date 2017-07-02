"""Dictionary เก็บข้อมูลได้หลาย ๆ ค่าในตัวแปรเดียวกัน แต่คุณสมบัติพิเศษของดิกชันนารีคือมีข้อมูลตั้งแต่ 2 ค่าขึ้นไปและมีความสัมพันธ์กัน
  การประกาศตัวแปร  การเพิ่มข้อมูล การแสดงผลข้อมูล การกำหนดตำแหน่งที่ต้องการ และการสลับตำแหน่งคีย์ของข้อมูล

"""

#INSERT
people = {'boy':'gonge','girl':'minnie','animal':'dog','natural':'rain'}
people['socialnetwork'] =   'facebook' #added
#print(people)
#result run after : {'boy': 'gonge', 'girl': 'minnie', 'animal': 'dog', 'natural': 'rain', 'socialnetwork': 'facebook'}

#UPDATE
people['animal'] = 'rabbit'  #updated
#print(people)
#result run after : {'boy': 'gonge', 'girl': 'minnie', 'animal': 'rabbit', 'natural': 'rain', 'socialnetwork': 'facebook'}


#DISPLAY DATA IN DICTIONARY
company = {'silicon valley':['facebook','yahoo','microsoft','google','apple','instagram','happy'],'facebook':'mark suckerberg','apple':'stave job'}
#print(company.keys())
#result run after :  dict_keys(['silicon valley', 'facebook', 'apple'])
#print(company.values())
#result run after : dict_values([['facebook', 'yahoo', 'microsoft', 'google', 'apple', 'instagram', 'happy'], 'mark suckerberg', 'stave job'])
#print(company.items())
#result run after : dict_items([('silicon valley', ['facebook', 'yahoo', 'microsoft', 'google', 'apple', 'instagram', 'happy']), ('facebook', 'mark suckerberg'), ('apple', 'stave job')])

# print(company)
#result run after : {'silicon valley': ['facebook', 'yahoo', 'microsoft', 'google', 'apple', 'instagram', 'happy'], 'facebook': 'mark suckerberg', 'apple': 'stave job'}


day = {'1':'monday','2':'tuesday','3':'wednesday','4':'thursday','5':'friday','6':'saturday','7':'sunday'}

number = day.keys()
day_pop = day.pop('2')

print(day_pop)  #delete '2':'tuesday'

print(day)
#result run after :  {'1': 'monday', '3': 'wednesday', '4': 'thursday', '5': 'friday', '6': 'saturday', '7': 'sunday'}
