# Install the QR code library using pip:
# pip install qrcode
import qrcode

# Define the link for the QR code
link = input("Enter destination link: ")

# Generate QR code
qr_code = qrcode.make(link)

# Save QR code
qr_code.save("qrcode.png")

# Print confirmation message
print("QR code generated successfully!")

