# Raspberry Pi Gaming Station

Raspberry Pi Gaming Station - RetroPie alternative based on RetroArch CLI and libretro.

## Contribution
This repository uses GitHub flow https://guides.github.com/introduction/flow/
- develop in your own feature branch named as "Feature/XXX"
  - for fixes use branches named as "Fix/XXX"
  - make sure to include any additional python dependencies in requirements.txt
- when you complete your feature/fix, open a pull request
  - have a contributor approve it for you (pushing directly to master is disabled)
- pull request convention example: feat(game): add start button
  - game is the name of the component the PR affects (leave it empty '()' if multiple)
  - include additional description, using present tense (f.ex. 'add new class in game.py')

## Repository structure
```
   .            # LICENSE, README, .gitignore, start.sh Bash script
   |-install    # Installation files
   |-src        # Main source directory
   |---config   # Configuration files directory
   |---docs     # Additional documentation directory
   |---images   # Images directory
   |---test     # Unit tests directory
```
