# Write code using find() and string slicing (see section 6.10) to extract the number,
# at the end of the line below.
# Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"
number = text.find("0")
second_number = text.find("5")
full_number_str = text[number:second_number+1]
fff = float(full_number_str)
print(fff)
