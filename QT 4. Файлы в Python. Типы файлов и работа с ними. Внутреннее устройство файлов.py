def reverse():
    f = open('input.dat', 'rb')
    data = f.read()
    f.close()
    f = open('output.dat', 'wb')
    f.write(data[::-1])
    f.close()