
############ Git commands

Get the latest updates
    git pull voodoo <branch name, usually "master">
    
    NOTE : Possible that there will be merge conflicts, in which case
    you will need to go into the file and fix them it.
    

Push your changes to the server 
    git add <changed_file>
    git commit -m 'message explaining what you did'
    git push voodoo <branch name>


I suggest that if you want to add something, and are
uncomfortable with merging code, follow this procedure

1) git pull voodoo master
    *gets latest changes from master

NOTE : if for example you fucked up your local branch beyond repair and
just want a clean copy of what is on github without doing any merging
    git fetch voodoo <branch name>
    git reset --hard voodoo/<branch name>
WARNING : this will wipe out any changes you have that are not in github

2) git checkout -b <desired branch name>
    *creates a new branch and switches to it
    *think of it as saving your game before a boss fight

3) develop freely

4) git add <all_files that need adding>
    *to see what files need adding : git status

5) git commit -m "message describing what you did"

6) git push voodoo <your branch name>
    *if you dont remember the branch name : git branch


This will allow you to push the code onto github on a separate branch
and I can merge it in to the master code later.


############# Python Setup (Casey)

Setting up python
    alias py='/Users/cc/python34/python.exe"

    Note : you will need to do this every time you open the terminal
    until we figure out how to get your Linux to remember it. 

Running a python module
    py -m <module name>



############## Running the scheduler

Assumptions :
    your python is configured correctly
    you are in the project's home directory


Instructions :
    python -m bin.run 
        runs the scheduler with a default of 4 hours
    python -m bin.run --hours x 
        where x is the number of hours you want


############## Running the tests

Assumptions :
    your python is configured correctly
    you are in the project's home directory


Instructions :
    python -m test.tests 
