###### Power Shell usefull file Commands #########
Set-Location C:\Local\PythonGit-J

$loc = Get-Location
# $dir = Get-ChildItem
# If Neccesary:
$loc

Set-Location $Env:USERPROFILE
$loc = Get-Location

Clear-Host
# cls
# Get-Alias cls  # Clear-Host

<#
# Commented block For examples:
#   Get-CimInstance -ClassName Win32_Desktop
#   Get-CimInstance -ClassName Win32_LocalTime
#   Get-ChildItem -Path C:\WINDOWS\System32 | Out-Host -Paging
#>

$loc
# $dir

### First lest create the file:
### cd ~  # Alias of Set-Location set it before
### touch .gitignore_global # equivalent is New Item so:

# New-Item .gitignore_global  ## Finally Succeded SUCCESSSSSSS

# Lets try to create the git global ignore file:
# git config --global core.excludesfile "$Env:USERPROFILE\.gitignore_global" # It configures succesfully
# Test if create it:
git config --global core.excludesfile


