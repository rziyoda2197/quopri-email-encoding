import quopri

def quoted_printable_encoding(matn):
    return quopri.encodestring(matn.encode('utf-8')).decode('utf-8')

matn = "Salam, dunyo!"
print(quoted_printable_encoding(matn))
