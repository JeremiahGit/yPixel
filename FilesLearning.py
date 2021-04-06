class FilesLearning: 

    def owo():
        print ("hi")

stringy = "embededFileName"

_file = open(f".\\tempPlayerJsons\\newTextFile_with_{stringy}.json","w+")

for i in range(11):
     _file.write("This is line %d\r\n" % (i+1))

_file.close()