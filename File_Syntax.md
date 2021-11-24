# Syntax for config and other files

## DEP
New line seperated package names, example:
```
firefox
alacritty
neofetch
``` 


## INST
Package name and source (Link/Folder) in a key:value (name:source) format in (JSON).
Example:
``` json
{
"dwm"   :  "https://git.suckless.org/dwm",
"dmenu" :  "https://git.suckless.org/dmenu"
}
```