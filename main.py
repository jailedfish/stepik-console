import os
class shell():
    def mkfile(fname):                    #creating file
        with open(fname,'w') as f:pass    #magic
    def runshell(self,cmd=[]):            
        if cmd == []:cmd=self.cmd         #if no args inputed, using class init args
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
shell().runshell(['cat main.py>>p.txt'])