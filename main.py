# import requests
#
# responce = requests.get(url="http://api.open-notify.org/iss-now.json")
# responce.raise_for_status()
#
# data = responce.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)


# from tkinter import *
# import requests
#
#
# def get_quote():
#     responce = requests.get("https://api.kanye.rest/#")
#     quote = responce.json()
#     canvas.itemconfig(quote_text, text=quote["quote"])
#
#
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)
#
# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
#
# window.mainloop()


import requests
import datetime as dt
import smtplib
from email.mime.text import MIMEText


MY_LATITUDE = 41.336736
MY_LONGITUDE = 69.173898


def is_iss_overhead():
    iss_responce = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_responce.raise_for_status()
    iss_data = iss_responce.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    return MY_LATITUDE-5 <= iss_latitude <= MY_LATITUDE+5 and MY_LONGITUDE-5 <= iss_longitude <= MY_LONGITUDE+5


def is_night():
    parametrs = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0
    }

    responce = requests.get("https://api.sunrise-sunset.org/json", params=parametrs)
    responce.raise_for_status()

    data = responce.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    now = dt.datetime.now().hour

    return now <= sunrise or now >= sunset


def send_email():
    email =
    password =

    msg = MIMEText("The (ISS) International Space Station is above you")
    msg["Subject"] = "Look up for ISS"
    msg["From"] = email
    msg["To"] = email

    with smtplib.SMTP("smtp.mail.me.com", 587) as server:
        server.starttls()
        server.login(user=email, password=password)
        server.sendmail(from_addr=email, to_addrs=email, msg=msg.as_string())


if is_iss_overhead() and is_night():
    send_email()
