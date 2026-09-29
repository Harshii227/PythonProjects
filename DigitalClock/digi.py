import qrcode

upi_id = input("ENter your UPI ID = ")

phone_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'


phonepe_qr = qrcode.make(phone_url)
paytm_qr = qrcode.make(paytm_url)
google_qr = qrcode.make(google_url)


phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_qr.save('google_qr.png')


phonepe_qr.show()
paytm_qr.show()
google_qr.show()
