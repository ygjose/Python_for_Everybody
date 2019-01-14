text = "X-DSPAM-Confidence:    0.8475";
space = text.find(' ')
number = text[space+1: ]
f_number = float(number)
print(f_number)
