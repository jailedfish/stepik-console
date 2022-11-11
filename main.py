import subprocess

class shell():
    def mkfile(self,fname):                        #creating file
        with open(fname,'w') as f:pass             #magic

    def fillfile(self,name,data,tp):
        tp = tp                                    #use 'a' to append or 'w' to write
        data = data                                #array next cell--next line
        with open(name,tp) as f:
            f.writelines(data)                     #filling line

    def runshell(self,cmd={}):            
        if cmd == {}:cmd=self.cmd                  #if no args inputted, using class init args
        
        for x in cmd:                              #parsing args
            if cmd[x] ==-1:
                subprocess.run(x)
            else:
                subprocess.run([x,cmd[x]])    

shell().mkfile('p.txt')
shell().mkfile('example.py')

data = ['import time\n', 'time.sleep(90)\n', 'with open(\'created_out.txt\',\'w\'):pass']
shell().fillfile('example.py', data, 'w')

comands = {
    'uname':-1,                                    #struct 'command':'args and target file'                                
}
shell().runshell(comands)