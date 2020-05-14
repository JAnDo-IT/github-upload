
# create a .gitignore file or global file
###### https://git-scm.com/docs/gitignore
###### https://gist.github.com/octocat/9257657
###### https://github.com/github/gitignore
###### https://help.github.com/en/github/using-git/ignoring-files
###### https://github.com/JAnDo-IT/github-upload.git

### If Needed create your global ignore file, in PowerShell Everything in single Q is a command
'Set-Location $Env:USERPROFILE' \
'$loc = Get-Location \
'$loc' \
First lest create the file: \
'New-Item .gitignore_global'

Lets try to create the git global ignore file: \
'git config --global core.excludesfile "$Env:USERPROFILE\.gitignore_global' # It configures succesfully \
Test if create it: \
'git config --global core.excludesfile' \
Finally Configure the Global File, my example is General an for Python


# …or create a new repository on the command line
git config --global user.email "youruser@yourdomain.ext" \
git config --global user.user "your user at github" \
echo "# github-upload" >> README.md \
git init \
git add README.md \
git commit -m "Initial The Way Projectcommit" \
git remote add origin https://github.com/JAnDo-IT/github-upload.git \
git push -u origin master

# …or push an existing repository from the command line
git remote add origin https://github.com/JAnDo-IT/github-upload.git \
git push -u origin master \

#…or import code from another repository
You can initialize this repository with code from a Subversion, Mercurial, or TFS project. \
https://github.com/JAnDo-IT/github-upload/import 

# Using the command line

In your command line, navigate to your project directory. Type git init to initialize the directory as a Git repository. \
Type git remote add origin https://github.com/JAnDo-IT/github-upload.git \
Type git add . \
Type git commit -m "initializing repository" \
Type git push -u origin master to push the files you have locally to the remote on GitHub. (You may be asked to log in.) \

# Using Visual Studio Code
1. In Visual Studio Code, open the folder for your project.
2. Click the icon on the left for Source Control.
3. On the top of the Source Control panel, click the Git icon.
4. If the files you see match the repository you want to create, click Initialize Repository.
5. Next to the word CHANGES, click the symbol of the plus sign to stage all of the changes.
	This is part of the two stage commit. You can use this staging function to create meaningful commits throughout the development process.
6. In the box in the Source Control panel, type a commit message. Something like "initial commit - moving project" could work.
7. Click the checkmark at the top of the Source Control panel.
8. Open the integrated terminal found under View > Integrated Terminal.
9. In your command line, type git remote add origin https://github.com/JAnDo-IT/github-upload
10. In the Source Control Panel, click the expandable three dots that open a menu of options.
11. When asked if you'd like to publish the branch, click Okay.

