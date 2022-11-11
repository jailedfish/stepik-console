import subprocess
dict = {'ls':['/','-a','l']}
print(dict.keys())
print(dict['ls'])
for x in dict:
    subprocess.run([x,dict[x]])