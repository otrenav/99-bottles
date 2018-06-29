#
# 99 bottles exercise personal solution
#
# Exercise from: Metz & Owern, 99 Bottles of OOP (2017)
#
# Omar Trejo
# March, 2017
#


class Bottles(object):

    START = 99
    END = 0

    @property
    def song(self):
        return(self.verses(self.START, self.END))

    def verses(self, start, end):
        verses = [
            self.verse(i)
            for i in reversed(range(end, start + 1))
        ]
        return("\n".join(verses))

    def verse(self, number):
        bottle_number = BottleNumber.for_verse(number)
        text = (
            "{} of beer on the wall, {} of beer.\n".format(
                str(bottle_number).capitalize(),
                bottle_number
            ) +
            "{}, {} of beer on the wall.\n".format(
                bottle_number.action,
                bottle_number.successor
            )
        )
        return(text)


class BottleNumber(object):

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return(str(self.quantity + " " + self.container))

    @property
    def container(self):
        return("bottles")

    @property
    def pronoun(self):
        return("one")

    @property
    def quantity(self):
        return(str(self.number))

    @property
    def action(self):
        return("Take " + self.pronoun + " down and pass it around")

    @property
    def successor(self):
        return(self.for_verse(self.number - 1))

    @staticmethod
    def for_verse(number):
        if number == 0:
            return(BottleNumber0(number))
        elif number == 1:
            return(BottleNumber1(number))
        elif number == 6:
            return(BottleNumber6(number))
        else:
            return(BottleNumber(number))


class BottleNumber1(BottleNumber):

    @property
    def container(self):
        return("bottle")

    @property
    def pronoun(self):
        return("it")


class BottleNumber0(BottleNumber):

    START = 99

    @property
    def quantity(self):
        return("no more")

    @property
    def action(self):
        return("Go to the store and buy some more")

    @property
    def successor(self):
        return(self.for_verse(self.START))


class BottleNumber6(BottleNumber):

    @property
    def quantity(self):
        return("1")

    @property
    def container(self):
        return("six-pack")
