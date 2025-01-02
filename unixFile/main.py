from file import File
from unixFind import UnixFind
from minSizeFilter import MinSizeFilter
from extensionFilter import ExtensionFilter
f1 = File("root_300", 300)

f2 = File("fiction_100", 100)
f3 = File("action_100", 100)
f4 = File("comedy_100", 100)
f1.children = [f2, f3, f4]

f5 = File("StarTrek_4.txt", 4)
f6 = File("StarWars_10.xml", 10)
f7 = File("JusticeLeague_15.txt", 15)
f8 = File("Spock_1.jpg", 1)
f2.children = [f5, f6, f7, f8]

f9 = File("IronMan_9.txt", 9)
f10 = File("MissionImpossible_10.rar", 10)
f11 = File("TheLordOfRings_3.zip", 3)
f3.children = [f9, f10, f11]

f11 = File("BigBangTheory_4.txt", 4)
f12 = File("AmericanPie_6.mp3", 6)
f4.children = [f11, f12]

greater5_filter = MinSizeFilter(5)
txt_filter = ExtensionFilter("txt")

my_linux_find = UnixFind()
my_linux_find.add_filter(greater5_filter)
my_linux_find.add_filter(txt_filter)

print(my_linux_find.apply_OR_filtering(f1))
print(my_linux_find.apply_AND_filtering(f1))