# ----------------------------------
# -- Practical Membership Control --
# ----------------------------------

# List Contains Admins
admins = ["Ahmed", "Osama","Yusuf", "Sameh", "Manal", "Rahma", "Mahmoud", "Enas"]

# Login
name = input("Please Enter Your Name: ").strip().capitalize()

# If Name is In Admin
if name in admins:

  print(f"Hello {name} Welcome Back")

  option = input("Do You Need To Delete Or Update Your Name ? ").strip().capitalize()

  # Update Option
  if option == "Update" or option == "U":

    theNewName = input("Please Enter Your New Name: ").strip().capitalize()

    admins[admins.index(name)] = theNewName

    print("Name Is Updated.")

    print(admins)

  # Delete Option
  elif option == "Delete" or option == "D":

    admins.remove(name)

    print("Name Deleted")

    print(admins)

  # Wrong Option
  else:

    print("Wrong choice")

else:

  status = input("Not An Admin, Do You Need To Add A New Admin Y, N ? ").strip().capitalize()

  if status == "Yes" or status == "Y":

    print("You Have Been Added")

    admins.append(name)

    print(admins)

  else:

    print("You Are Not Admin.")