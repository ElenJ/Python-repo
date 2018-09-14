# This programm compares the content of 2 folders and adds respectively missing files to each folder
import os,shutil

print("Enter absolute path of directory 1")
Folder1 = input()
Folder1 = Folder1.replace(os.sep, '/')
print("Enter absolute path of directory 2")
Folder2 = input()
Folder2 = Folder2.replace(os.sep, '/')

#creates a list of folder content:
FolderContent1 = os.listdir(Folder1)
#print(FolderContent1)
FolderContent2 = os.listdir(Folder2)
#print(FolderContent2)

#determines difference in folders
DifferenceInFolders = list(set(FolderContent1) - set(FolderContent2))
DifferenceInFolders2 = list(set(FolderContent2) - set(FolderContent1))

#Checks if entry is a file or a folder
FoldersInFolder = []
DifferenceInFoldersFiles = []
for filename in DifferenceInFolders:
   # print(filename)
    if not os.path.isfile(Folder1+"/"+filename):
        FoldersInFolder.append(filename)
    else:
        DifferenceInFoldersFiles.append(filename)

# for loop that copies files
for filename in DifferenceInFoldersFiles:
    shutil.copy(Folder1+"/"+filename, Folder2)
print("Your folder 1 contains "+str(len(FoldersInFolder))+" folders")
print(FoldersInFolder)
#copies subfolder and its content
for dirname in FoldersInFolder:
    shutil.copytree(Folder1+"/"+dirname, Folder2+"/"+dirname)
#repeat for alternate comparison
#Checks if entry is a file or a folder
FoldersInFolder2 = []
DifferenceInFoldersFiles2 = []
for filename in DifferenceInFolders2:
   # print(filename)
    if not os.path.isfile(Folder2+"/"+filename):
        FoldersInFolder2.append(filename)
    else:
        DifferenceInFoldersFiles2.append(filename)

# for loop that copies files
for filename in DifferenceInFoldersFiles2:
    shutil.copy(Folder2+"/"+filename, Folder1)
print("Your folder 2 contains "+str(len(FoldersInFolder2))+" folders")
print(FoldersInFolder2)
#copies subfolder and its content
for dirname in FoldersInFolder2:
    shutil.copytree(Folder2+"/"+dirname, Folder1+"/"+dirname)

print("All done!")