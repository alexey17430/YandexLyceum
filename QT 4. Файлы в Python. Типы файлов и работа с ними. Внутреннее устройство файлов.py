def palindrome():
    f = open('input.dat', 'rb')
    data = f.read()
    begin = data[:len(data) // 2]
    end = data[::-1][:len(data) // 2]
    return end == begin
