text = "X-DSPAM-Confidence:    0.8475"
numtext1 = text.find('0')
numtext2 = text.find('5')

numtext3 = text[numtext1 : numtext2+1]
print(float(numtext3))