# SEATWORK 1
from pyscript import document, display

club_members = ["Johanna Ramos", "Kailey Gayas", "Hope Benitez", "Mhicaela Belen", "Angel Canino"]

# verifying member name
def verify(e):
    document.getElementById("message").innerHTML = ""

    firstname = document.getElementById("Fname").value
    surname = document.getElementById("Sname").value
    fullname_ = (firstname + " " + surname).title()

    # verifies if typed name is a member of the club
    #.lower to make it case-insensitive
    result = fullname_.lower() in [name.lower() for name in club_members]

    messages = {
        True: "Congratulations " + fullname_ + "! You are now part of OBFV GIRLS' VOLLEYBALL CLUB.",
        False: "Sorry " + fullname_ + ", your name is not on the list."
    }

    # displays the result
    display(messages[result], target="message")


# clears the boxes
def clear(e):
    document.getElementById("Fname").value = ""
    document.getElementById("Sname").value = ""
    document.getElementById("message").innerHTML = ""