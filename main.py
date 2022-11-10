import os
#import evil_module
class shell():
    def __init__(self,cmd_in=[]):
        self.cmd = cmd_in
    def mkfile(fname):
        with open(fname,'w') as f:
            pass
    def runshell(self,cmd=[]):
        if cmd == []:cmd=self.cmd
        filename = 'return.txt' #const str
        self.mkfile(filename)
        c = 0
        for x in cmd:
            if c==0:
                os.system(x +' >> '+filename)
            else:
                os.system(x +' > '+filename)
            c+=1
        with open(filename,'r') as f:print(f.read())

shell().mkfile('p.txt')
shell().runshell(['cat main.py>>p.txt'])