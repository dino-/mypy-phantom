# mypy-phantom


## Synopsis

Example of using phantom types in Python with mypy


## Description

Phantom types can be used to encode state in the type system and enforce
correct usage of APIs at the type checker level.

This is a contrived phantom types example using the concept of a rocket ship
that must be fueled and contain O2 to launch. These constraints are encoded as
types. Values with the incorrect types won't pass the type checker (mypy).

This code was inspired by [this example](https://james-iry.blogspot.com/2010/10/phantom-types-in-haskell-and-scala.html)
showing the same thing done in Haskell and Scala.


## Getting the project

[From github](https://github.com/dino-/mypy-phantom)


## Using it

Simply type check with mypy:

    $ mypy mypy-phantom


## Contact

Dino Morelli <dino@ui3.info>
