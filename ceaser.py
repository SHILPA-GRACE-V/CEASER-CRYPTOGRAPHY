def caesar_encrypt(realText, step):
    outText = []
    cryptText = []
	
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    punct=[' ','!','.']
    
    for eachLetter in realText:
            if eachLetter in uppercase:
                index = uppercase.index(eachLetter)
                crypting = (index + step) % 26
                cryptText.append(crypting)
                newLetter = uppercase[crypting]
                outText.append(newLetter)
            elif eachLetter in lowercase:
                index = lowercase.index(eachLetter)
                crypting = (index + step) % 26
                cryptText.append(crypting)
                newLetter = lowercase[crypting]
                outText.append(newLetter)
            elif eachLetter in punct:
                outText.append(eachLetter)
    return outText
s=3
print("1.ENCRYPTION  2.DECRYPTION")
ch=int(input("Enter a choice:"))
if ch==1:
    code = input("Enter tne message:")
    encrypt=caesar_encrypt(code,s)
    print("encrypted code is:\t")
    for i in encrypt:
        print(i,end='')
elif ch==2:
    code=input("Enter the decrypted code:")
    decrypt=caesar_encrypt(code,26-s)
    print("Orginal messsage is:\t")
    for i in decrypt:
        print(i,end='')

