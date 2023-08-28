# ----------------------------
# -- Simple Password Guess --
# ----------------------------

tries = 3

mainPassword = "Yusuf1"

inputPassword = input("Enter Your Password: ")

while inputPassword != mainPassword:  # True

  tries -= 1  # tries = tries - 1

  print(f"Wrong Password, { 'Last' if tries == 0 else tries } Chance Left")

  inputPassword = input("Enter Your Password: ")

  if tries == 0:

    print("All attempts are over.")

    break

else:

  print("Correct Password Welcome Back")