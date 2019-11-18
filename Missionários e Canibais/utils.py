def check_type(_type, data):
    if type(_type) != type:
        raise ValueError('In processing the function, wrong parameters were found.')
    elif type(data) != _type:
        raise ValueError('Attribute has unexpected type for operation!'
                         'Arguments must be of type: ' + str(_type))
