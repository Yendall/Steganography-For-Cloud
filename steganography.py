from stegano import lsb
secret = lsb.hide("./test.png", "This is a test This is a testThis is a testThis is a testThis is a testThis is a test"
                                "This is a testThis is a testThis is a testThis is a testThis is a testThis is a test"
                                "This is a testThis is a testThis is a testThis is a testThis is a testThis is a test")
secret.save("./Lenna-secret.png")
print(lsb.reveal("./Lenna-secret.png"))