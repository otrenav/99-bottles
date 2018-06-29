
| [Website](http://links.otrenav.com/website) | [Twitter](http://links.otrenav.com/twitter) | [LinkedIn](http://links.otrenav.com/linkedin)  | [GitHub](http://links.otrenav.com/github) | [GitLab](http://links.otrenav.com/gitlab) | [CodeMentor](http://links.otrenav.com/codementor) |

---

# Exercise from 99 Bottles of OOP

- Omar Trejo
- March, 2017

## Overview

This repository contains an exercise from the excellent book "99 Bottles
of OOP" by Metz & Orwen (2017). It's a book that aims to teach basic
object-oriented techniques through an example that is worked on
throughout the book (the one in this repository).

To understand the evolution of the example you may throught the commits
in this repository and see how code was changed along the explanatory
comments in the commit messages. To understand the concepts and
techniques used I'd highly recommend to read the entire book (you can
read it in a single sitting).

## Tests

The idea is that you have an initial specification in the form of unit
tests (that later turn into functional tests) and you need to make all
of them pass. Chances are that you did not start with an OOP solution
but the book shows you how to achieve one.

The tests require the `py.test` package. You may execute the tests with
`$ pytest` in the root of the project.

## Compare solutions

Compare:
- [Initial, non-OOP solution](https://github.com/otrenav/bottles/blob/b271edac6d5c2114c7aa6b15569244801d4247dc/bottles.py)
- [Final, OOP solution](https://github.com/otrenav/bottles/blob/master/bottles.py)

and try to imagine how hard or easy would each of them be to change
when new requirements come in. ;)

---

> "The best ideas are common property."
>
> —Seneca
