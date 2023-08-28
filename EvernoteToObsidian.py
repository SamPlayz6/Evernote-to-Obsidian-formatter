import os
import markdown
import math

# --Takes Evernote(.enex) files and converts to markdown using Yarle.
# --https://github.com/akosbalasko/yarle

# --My code then alters the files to add generated tags, based off the other obsidian tag names. 
# --After this it moves them into the Obsidian.

#LinkWeightFunction - Feel free to Calibrate for your own use
def linkFunc(cnt, length, noteNum):
    if cnt == 0:
        return 0
    return (math.log(cnt,2)*200)/(length*noteNum)

files = []
names = []
filter = open('C:\\Users\\SamDunning\\Desktop\\EvernoteToObsidian\\FilterWords.txt', 'r').read().split("\n")

# --Replace with directory of yarle exported markdown files
exportedDirectory = 'C:\\Users\\SamDunning\\Desktop\\EvernoteToObsidian\\Yarle Output\\notes\\Example'
for filename in os.listdir(exportedDirectory):
    f = os.path.join(exportedDirectory, filename)
    if os.path.isfile(f):
        #File name , File contents
        files.append([filename[:-3], open(f, "r+", encoding="utf8").read()])

# --Replace directory with Obsidian Directory
ObsidianDirectory = "C:\\Users\\SamDunning\\Desktop\\EvernoteToObsidian\\NoteArchive\\"
for filename in os.listdir(ObsidianDirectory):
    f = os.path.join(ObsidianDirectory, filename)
    if os.path.isfile(f):
        #FileName , [Name Broken by Spaces]
        names.append([filename[:-3], filename[:-3].split(" ")])

#Want to add tags for each file
for b in files:
    #Comparing File names to contents of file b. Creating & Adding file
    f = open(ObsidianDirectory + "= " + b[1][16:26] + " "  + b[0] + ".md", "x", encoding="utf8")
    f.write(b[1] + "\n\n")
    for i in range(len(names)):
        #Check not comparing a file to itself
        if b[0] != names[i][0]:
            cnt = 0
            #Iterate through the words broken in a title
            for k in names[i][1]:
                if k.lower() in list(map(lambda x: x.lower() ,b[1].split(" "))) and k.lower() not in filter:
                    cnt += 1
            if linkFunc(cnt, len(names[i][0]),len(names)) > 0.03:
                input = "[[" + names[i][0] + "]]"
                f.write(input)
f.close()