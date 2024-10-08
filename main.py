from Tools.demo.spreadsheet import ljust

def Open(file_name,mode):
    try:
        file=open(file_name,mode)
    except:
        print("File",file_name,"does not opened")
    else:
        print("File",file_name,"opened")
        return file

file1_name="TF9_1.txt"
file2_name="TF9_2.txt"

file_1_w=Open(file1_name,"w")

if (file_1_w!=None):
    file_1_w.write("First line\n")
    file_1_w.write("Second line longer\n")
    file_1_w.write("I don't buy an apple at the shop\n")
    file_1_w.write("Fourth\n")
    file_1_w.write("1235678901234567890\n")
    print("Information succesfuly added to TF9_1.txt")
    file_1_w.close()

file_1_r=Open(file1_name,"r")
file_2_w=Open(file2_name,"w")

if file_1_r is not None and file_2_w is not None:
    for line in file_1_r:
        line=line.strip()
        if len(line)<20:
            line=line.ljust(20)
        elif len(line)>20:
            line=line[:20]
        file_2_w.write(line+"\n")
    file_1_r.close()
    file_2_w.close()

print("Information succesfuly added to TF9_2.txt")

print("New sequence")

file_2_r=Open(file2_name,"r")
if file_2_r is not None:
    for line in file_2_r:
        print(line.strip())
    file_2_r.close()
