PROMPT: str = "what do you want?"
JOKE:str = "What’s a coder’s favorite hangout spot? The Git hub 🎯😎"
sorry:str = " i only tell joke:"

def main():
  user_input = input(PROMPT)
  user_input = user_input.strrip().lower()

  if "joke" in user_input:
    print("JoKE")
  else:
    print("SORRY")

  if __name__ == "__main__":
    main()