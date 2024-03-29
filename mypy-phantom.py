#! /usr/bin/env python3

# Illustration of using phantom types with Python and mypy
# Inspired by https://james-iry.blogspot.com/2010/10/phantom-types-in-haskell-and-scala.html
#
# Type check this script: `mypy mypy-phantom.py`


from typing import TypeVar, Generic


Fuel = TypeVar('Fuel')
O2 = TypeVar('O2')

# None of these classes are meant to be instantiated.
# These are the "phantom" types.

class NoFuel: pass
class Fueled: pass

class NoO2: pass
class HasO2: pass

# The Rocket data type takes two type parameters but its constructor doesn't
# touch them. Only functions in this module should construct Rocket instances!

class Rocket(Generic[Fuel, O2]): pass

# Produces a rocket with no fuel and no o2. This is the factory for new
# rockets.

def createRocket() -> Rocket[NoFuel, NoO2]:
  return Rocket()

# These functions only take rockets with certain types and produce rockets with
# different types to signify how they've changed.

def addFuel(rocket: Rocket[NoFuel, O2]) -> Rocket[Fueled, O2]:
  return Rocket()

def addO2(rocket: Rocket[Fuel, NoO2]) -> Rocket[Fuel, HasO2]:
  return Rocket()

# Launch will only launch a rocket with both fuel and o2

def launch(rocket: Rocket[Fueled, HasO2]) -> None:
  print("blastoff")


def main() -> None:
  # These work, and fueling/adding o2 in any order
  launch(addO2(addFuel(createRocket())))
  launch(addFuel(addO2(createRocket())))

  # No fuel or O2, won't typecheck
  launch(createRocket())

  # No fuel, won't typecheck
  launch(addO2(createRocket()))

  # No O2, won't typecheck
  launch(addFuel(createRocket()))

  # Adding fuel twice is not allowed
  launch(addO2(addFuel(addFuel(createRocket()))))


if __name__ == '__main__': main()
