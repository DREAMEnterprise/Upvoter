import os, re, pdb, praw
from time import sleep
import winsound

# Create the Reddit instance
reddit = praw.Reddit('bot1')

subs = ["free_karma", "learnpython", "python", "wholesomememes"]

terms = ["pls", "plz", "please", "thank you", "thanks"]

count = 20

run_count = 0

log_file = "upvoted.txt"
width = 50
lines = 40

#define cosole size and color
os.system("mode con: cols=" + str(width) + " lines=" + str(lines))
os.system("color F")
os.system("cls")
os.system("echo off")

def logo():
    print ()
    print("UPVOTER".center(width-1))
    print()
    print("David Ray".center(width-1))
    print("David@DREAM-Enterprise.com".center(width-1))
        
    print()
    print()
        
    

def count_votes():
    global total_votes
    f = open(log_file, "r")
    upvoted = f.read()
    upvoted = upvoted.split("\n")
    upvoted = list(filter(None, upvoted))
    total_votes = str(len(upvoted))
    #print ("Total Upvotes Given: "+str(len(upvoted)))
    
def show_count():
    count_votes()  
    print()          
    print("*****************************".center(width-1))
    #print("Upvotes Complete".center(width-1))
    print(("Total Votes: "+total_votes.zfill(7)).center(width-1))
    print("*****************************".center(width-1))
    print()

def start_upvotes():    
    if not os.path.isfile(log_file):
        upvoted = []
    
    else:
        f = open(log_file, "r")
        upvoted = f.read()
        upvoted = upvoted.split("\n")
        upvoted = list(filter(None, upvoted))
    
    f = open(log_file,"a")
    for sub in subs:    
        print(("r/"+sub.capitalize()+" - Upvoting Commenced!").center(width-1))
        subreddit = reddit.subreddit(sub)
        for submission in subreddit.hot(limit=count):
        	
            if submission.id not in upvoted:
                
                for term in terms:
                    if re.search(term, submission.title, re.IGNORECASE):
                        
                        #upvoting
                        submission.upvote()
                        upvoted.append(submission.id)
                        print(("Upvote "+str(len(upvoted)).zfill(7)+": "+
                               sub.capitalize()).center(width-1))
                        beep()
                        #print("Upvote "+str(len(upvoted)).zfill(7)+": "+
                        #      str(subreddit)+" - "+submission.title)
                            
                        f.write(submission.id + "\n")
        
                        f.flush() 
        
        print(("r/"+sub.capitalize()+" - Upvoted!").center(width-1))
        print()
        
def take_break():
    global run_count
    run_count+=1

    print()
    print(("Total Run Count: "+str(run_count)).center(width-1))
    print("Taking a Break.".center(width-1))
    sleep(600)
    print()
    print()
    
def beep():
    winsound.Beep(1000,50)
    winsound.Beep(900,50)
    winsound.Beep(800,50)
    winsound.Beep(900,50)
    winsound.Beep(1000,50)    
    
if __name__ =="__main__":
    logo()
    while True:    
        start_upvotes()
        show_count()
        take_break()
    