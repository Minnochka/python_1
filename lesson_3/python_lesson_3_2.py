def user_info(name, surname, year, city, email, phone):
    if len(name) < 1 or len(surname) < 1 or len(city) < 1 or year < 1900 or year > 2002 or len(email) < 6 or phone < 1000000:
        print("Wrong data!")
    else:
        print("Your name is {} {}. You were born in {}. You are from {}. Your contacts: {} and {}.".format(name.title(), surname.title(), year, city.title(), email.lower(), phone))

user_info(
    name=input("Enter your name: "),
    surname=input("Enter your surname: "),
    year=int(input("Enter your year of birth: ")),
    city=input("Enter your city: "),
    email=input("Enter your email: "),
    phone=int(input("Enter ypur phone number: ")))
