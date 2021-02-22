def bottles_of_beer(bob):
    """ prints bottles of beer on the wall lyrics.
    :param bob: must be a positive integer.
    """
    if bob < 1:
        print("""No more bottles of beer on the wall.
                 no more bottles of beer.""")
        return

    tmp = bob
    bob -= 1
    print("""{} bottles of beer on the wall.
             {} bottles of beer.
             Take one down, pass it around,
             {} bottles of beer on the wall.
          """.format(tmp, tmp, bob))
    bottles_of_beer(bob)
bottles_of_beer(99)
