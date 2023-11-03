
import qrcode
first_name="Vasanth"
last_name="Kumar"
email="vasi@gmail.com"
phone_number="8106941512"
vcar=f"BEGIN:VCARD\nVERSION:3.0\nN:{first_name};{last_name};;;\nFN:{first_name}\nEMAIL:{email};TYPE=INTERNET:{email}" \
     f"\nTEL;TYPE=CELL:{phone_number}\nEND:VCARDE"
img=qrcode.make(vcar)
img.save('contact.png')