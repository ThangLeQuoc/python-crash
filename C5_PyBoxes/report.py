def get_description(): # see the docstring below ?
    """ Return random weather, just like the pros """
    from random import choice
    possibilites = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilites)
