from File import * 
from Directory import * 

dir1 = Directory("Movie")
mov1 = File("Avengers")
dir2 = Directory("Comedy Movies")
mov2 = File("HulChul")

dir1.add(mov1)
dir2.add(mov2)
dir1.add(dir2)

dir1.ls()