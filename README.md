# fountain-template

A copy of my workflow for working on my fountain scripts.

Some notes:

 - 0_0.md is the title page, for title page stuffs.
 - The files are sorted act_scene.md.
    - You can have up to 99 scenes in an act (100 if you start from 0) before things get screwy with the sorting.
 - To change the name of the script output, change the NAME var at the top of the Makefile.
    - You should also change the .gitignore file so you don't commit your built script to the repo by accident.

To build the .fountain:

```
make
```

It's that simple!

## PDF export ##

This requires the afterwriting CLI.

```
make pdf
```

This will also make the fountain script if it is out of date.
