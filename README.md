# Confit
A tool to set up config files (dotfiles)

I have no clue how I am gonna implement this...

## Plan or something idk
+ Have a file for dependencies (For stuff which is needed in compilations, not the thing to compile) File name: `DEP`
+ Have a file listing all the stuff which will be compiled/configured, also have links to their respective git repositories hosted on github, gitlab (Basically anywhere accessible directly by `git clone <link>`)
+ All the "stuff" listed in the file must have a `WHATDO` file in the repo which will have instructions for the compilation/configuration. The following things are to be listed in it (This also lists the structure required for the repositories.):
++ Be able to specify wether the thing is to be compiled from scratch (Eg: DWM) or have some config files which are to be placed in a specific directory (Eg: i3)
+ Log all the changes (installing/compiling/configuring)
