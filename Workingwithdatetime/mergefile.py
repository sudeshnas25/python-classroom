import glob2
import datetime
filenames=glob2.glob("*.txt")
with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt",'w')as file:
    for i in filenames:
        with open(i,'r')as f:
            #content=f.read()
            file.write(i+"\n")
