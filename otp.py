import pyotp
import time
import qrcode

b = pyotp.random_base32()
print(b)
totp=pyotp.TOTP(b)
a=totp.now()
print(a)
print(totp.verify(a))
#time.sleep(30)
print(totp.verify(a))

hotp = pyotp.HOTP(b)
h1=hotp.at(1)
print(h1)
h2 = hotp.at(2)
print(h2)


ua = pyotp.TOTP('JBSWY3DPEHPK3PXP').provisioning_uri("alice@google.com", issuer_name="Secure App")
print(ua)
totp.provisioning_uri()

img = qrcode.make(totp.provisioning_uri("alice@google.com", issuer_name="Secure App"))
img.save('test.png')
time.sleep(10)
print(totp.now())
time.sleep(30)
print(totp.now())
time.sleep(30)
print(totp.now())

