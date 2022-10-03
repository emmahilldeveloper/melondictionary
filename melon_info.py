"""Print out all the melons in our inventory."""


from melons import melons 


def print_all_melons(melons):
    """Print each melon with corresponding attribute information."""

    for melon, details in melons.items():
        print(f'melon_name: {melon}')

        for details, value in details.items():
            print(f'{details}: {value}')

        print("                 ")

print_all_melons(melons)