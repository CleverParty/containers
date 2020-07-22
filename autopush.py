import subprocess
import time
s = subprocess.getstatusoutput(f'git status')
if (s[0] == 0):
    one = subprocess.getstatusoutput(f'git add .')
    time.sleep(20)
    prnt = input("Enter the commit text\n")
    two = subprocess.getstatusoutput(f'git commit -m \"{prnt}\"')
    time.sleep(20)
    print(two)
    three = subprocess.getstatusoutput(f'git status')
    time.sleep(5)
else :
    print("Commit something first thalaiva")

# brnch = input("Enter the branch name\n")
four = subprocess.getstatusoutput(f'git push') # test with origin later
print(four)