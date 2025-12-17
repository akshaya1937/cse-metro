import streamlit as st
import qrcode
from io import BytesIO
import uuid
from PIL import Image
from gtts import gTTS
import base64


def generate_qr(data):
    qr= qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img
st.set_page_config(page_title="Metro Ticket Booking",page_icon=" ")
st.title("metro ticket booking with QRcode + Auto Voice")
stations = ["Ameerpet", "Miyapur", "LB Nagar", "KPHB"]
name = st.text_input("passenger name")
source = st.selectbox("source station", stations)
destination = st.selectbox("destination station", stations)
no_tickets = st.number_input("number of tickets", min_value=1, value=1)
price_per_ticket = 30
total_amount = no_tickets*price_per_ticket
st.info(f" total amount: {total_amount}")


if st.button ("book ticket"):
    if name.strip() =="":
        st.error("please enter passeng name.")
    elif source == destination:
        st.error("source and destination cannot be the same")
    else:
        booking_id = str(uuid.uuid4())[:8]
        qr_data = (
            f"bookingID: {booking_id}\n"
            f"Name: {name}\nFrom: {source}\nTo: {destination}\n Tickets: {no_tickets}"
            )
        qr_img = generate_qr(qr_data)

        buf = BytesIO()
        qr_img.save(buf, format="PNG")
        qr_bytes = buf.getvalue()

        st.success("Ticket Booked Successfully!")

        st.write("ticket details")
        st.write(f"**booking ID:** {booking_id}")
        st.write(f"**passenger:** {name}")
        st.write(f"**from:** {source}")
        st.write(f"**to:** {destination}")
        st.write(f"**tickets:** {no_tickets}")
        st.write(f"**amount paid:** {total_amount}")
        st.image(qr_bytes, width=250)
