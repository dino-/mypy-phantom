# mypy-phantom


## Synopsis

Example of using phantom types in Python with mypy


## Description

Phantom types can be used to encode state in the type system and enforce
correct usage of APIs at the type level.

This is a contrived phantom types example using the concept of a rocket ship
that must be fueled and contain O2 to launch. These states are encoded as
types. By controlling the type transformations as input and output types of
functions we can enforce correct usage of an API. Code that will do something
wrong won't type check.

This code was inspired by [this example](https://james-iry.blogspot.com/2010/10/phantom-types-in-haskell-and-scala.html)
showing the same thing done in Haskell and Scala.


## Getting the project

[From github](https://github.com/dino-/mypy-phantom)


## Using it

Simply type check with mypy:

    $ mypy mypy-phantom.py


## Contact

Dino Morelli <dino@ui3.info>
