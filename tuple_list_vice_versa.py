""""Data Structure


Tuple  เข้าถึงข้อมูลด้วยดัชนี เก็บข้อมูลคงที่ที่ไม่มีการเปลี่ยนอีกแล้ว และไม่สามารถเพิ่มลบข้อมูลได้โดยตรง
        ข้อดี ข้าถึงข้อมูลได้รวดเร็ว สามารถเปลี่ยนข้อมูลไปมาระหว่าง list กับ Tuple ได้คือ ใช้ list() tuple()
        ทั้งนี้ การที่จะแกไขข้อมูลใน tuple นั้นได้ต้องทำการแปลงข้อมูลจาก tuple ไปเป็น list ก่อนป แล้วค่อยเปลี่ยนกลับคืนเป็น Tuple เหมือนเดิม

        """
name = ("polaris","enigma","torse","nobita","naruto","tusk","involker")
#print(name)
#after run result: ('polaris', 'enigma', 'torse', 'nobita', 'naruto', 'tusk', 'involker')

#name.append("god")
#after run result :  AttributeError: 'tuple' object has no attribute 'append'

new_name = list(name)  #convert tuple to list ,because it must be list before append
#result = type(new_name)
#print(result)
#result after runned : <class 'list'>  is can be use append function.

new_name.append("""peter parker","steam","summer sale 2017""")
#print(new_name)
#result run after " ['polaris', 'enigma', 'torse', 'nobita', 'naruto', 'tusk', 'involker', 'peter parker","steam","summer sale 2017']
#It's list not tuple

new_name_converted = tuple(new_name)
print(new_name_converted)
#result run after : ('polaris', 'enigma', 'torse', 'nobita', 'naruto', 'tusk', 'involker', 'peter parker","steam","summer sale 2017')
