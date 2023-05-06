import os,sys;

os.system('cls')
# os.system('touch test1.py')
# get desktop location
name = str(os.popen('whoami').read())
# creating path for our folder
value  = name.split('\\');
head = "C:\\Users\\";
tail = "\\Desktop\\";
dir_name = "joker"
path = head + value[1].strip('\n') + tail + dir_name;

# making directory
os.mkdir(path);

#adding file to directory
f = open(f'{path}/rob.txt', 'w')
f.write('u are robbed!!!!!!!!!')

# some assurances
print(path);
print("code executed successfully");

# erasing this file
os.remove(sys.argv[0]);