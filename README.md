"# github-upload" 
As First Step
Create the Global File was kind of confuse so try:

You need to set up your global core.excludesfile configuration file to point to this global ignore file.

e.g.

*nix or Windows git bash:
git config --global core.excludesfile '~/.gitignore' #did not worked at first

Windows cmd:
git config --global core.excludesfile "%USERPROFILE%\.gitignore"

Since PS is the next gen cmd so will try:

Windows PowerShell:
git config --global core.excludesfile "$Env:USERPROFILE\.gitignore"
You can do it from vs Code once the PS extension is configured.

For Windows it set to the location C:\Users\{myusername}\.gitignore. 
You can verify that the config value is correct by doing:

git config --global core.excludesfile
