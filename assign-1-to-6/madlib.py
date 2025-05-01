def mad_lib():
    print("lets play mad libs! fill in the blanks with your own words.")
    
    name = input("give me a name: ")
    place = input("give me a place:")
    funny_adj = input("give me a funny adjective:")
    random_object = input("give me a random object: ")
    animal = input("give me an animal:")
    action_verb = input("give me an action verb:")
    funny_exclamation = input("give me a funny exclamation:")
    
    story = f"""
    once upon a time, there was a person named {name} who lived in {place}.
    one day, they found a {funny_adj} {random_object} that belonged to a {animal}.
    the {animal} was very upset and started to {action_verb} around 
    name couldn't help but lough and shouted "{funny_exclamation}".
    """
    
    print("\n here is your mad libs story:")
    
    if __name__ == "__main__":
        mad_lib()
    
    
    
    