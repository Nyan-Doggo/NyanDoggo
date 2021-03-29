textToConvert = ""
with open("input.txt", "r") as file:
    textToConvert = file.read()


textToConvert = textToConvert.replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;")
textToConvert = textToConvert.replace("&", "&amp")
textToConvert = textToConvert.replace("<", "&lt")
textToConvert = textToConvert.replace(">", "&gt")
textToConvert = textToConvert.replace("\n", "<br/>")

with open("output.txt", "w") as file:
    file.write(textToConvert)