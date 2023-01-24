# autocell
Autocell is a programming language and a user interface to run and display the evolution of cellular automata.

## Dependencies

* OCAML
* GMake

## To build

	$ make

## To run

In order for the build to run correctly, copy-paste the files stored in a folder previously chosen among those associated with each labwork (labwork-1, labwork-2, labwork-3 or labwork-4)

	$ ./autocell XXX.exe YYY.map

In order to obtain an exe, one has to type:

	$ ./autocc XXX.auto
	$ ./autoas XXX.s
	
## Directories

  * autos -- source code in AutoCell
  * maps -- maps to use to run a program
  * pages -- used by AutoCell


## Tribute to

Techniques:
* [Tiny HTTPD](https://github.com/c-cube/tiny_httpd/) whose sources are included in this project.

Conway's Life Game
* [John Conways's Game Of Life](https://playgameoflife.com/lexicon/135-degree_MWSS-to-G)

Good websites:
* (https://interstices.info/a-la-decouverte-des-automates-cellulaires/)[https://interstices.info/a-la-decouverte-des-automates-cellulaires/]
* (https://www.conwaylife.com/wiki/Cellular_automaton#Life-like_cellular_automata)[https://www.conwaylife.com/wiki/Cellular_automaton#Life-like_cellular_automata]
