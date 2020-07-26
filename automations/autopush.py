import subprocess
import time
s = subprocess.getstatusoutput(f'git status')
print(s)
uptodate = "Your branch is up to date with 'origin/master'"
tobestaged = "Changes not staged for commit:"

def autoPush():
    if(tobestaged in s[1]) :
        one = subprocess.getstatusoutput(f'git add -A')
        print("\nStage 1 : Changes added \n")
        print(one[1])
        prnt = input("Enter the commit text \n")
        two = subprocess.getstatusoutput(f'git commit -m \"{prnt}\"')
        time.sleep(5) # if a larger commit, change sleep time
        print("\nStage 2 : Changes commited \n")
        print(two[1])
        three = subprocess.getstatusoutput(f'git status')
        print(three[1])
        time.sleep(5)
    else :
        print("Commit something first thalaiva\n")
    """ else :
        print("Everything is up to date don't worry") """


# brnch = input("Enter the branch name \n")
brnch = "master"
autoPush()
four = subprocess.getstatusoutput(f'git push origin {brnch}') # test with origin later
print("\nStage 3 : git pushed changes \n")
print(four[1])