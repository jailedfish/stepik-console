import os
class shell():
    def mkfile(self,fname):                    #creating file
        with open(fname,'w') as f:pass     #magic

    def fillfile(self,name,data,tp):
        tp = tp                #use 'a' to append or 'w' to write
        data = data             #array next cell--next line
        with open(name,tp) as f:
            f.writelines(data)

    def runshell(self,cmd=[]):            
        if cmd == []:cmd=self.cmd         #if no args inputted, using class init args
        filename = 'return.txt'           #const str
        self.mkfile(filename)             #creating out file
        c = 0

        for x in cmd:                         #parsing args
            if c==0:                          #if first iteration changing out
                os.system(x +' >> '+filename) #changing output
            else:
                os.system(x +' > '+filename)  #appending output
            c+=1
        with open(filename,'r') as f:print(f.read()) #reading output

            
            

shell().mkfile('p.txt')
shell().mkfile('example.py')
shell().fillfile(['import time','time.sleep(25)','with open(\'created_out.txt\',\'w\'):pass'])
shell().runshell(['bash','cd ..','pwd'])
