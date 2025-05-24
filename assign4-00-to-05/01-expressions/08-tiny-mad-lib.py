def mad_lib():
    noun:str(input("enter a noun: "))
    adjective:str(input("enter an adjective: "))
    verbs:str = str(input("enter a verb: "))
    adverb:str = str(input("enter an adverb: "))
    print(f"do you {verbs} your {adjective} {noun} {adverb} ? that\'s hilarious")  # noqa: F821
    
if __name__ == "__main__":
    mad_lib()