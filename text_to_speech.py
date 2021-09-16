#gtts is the module responsible for the text to speech procedure.
#install gtts using:
# > pip install gtts
#before using this program
from gtts import gTTS #importing gtts

print("Welcome to text to speech,\n Enter your text here: ")
Text = input() #Taking text as input.
language = "en" #language of the text (ENGLISH)
print("Enter mp3 file name: ")
out_name = input() # taking input of the file name.

output = gTTS(text=Text, lang=language, slow=False) #conversion of text to speech 

#save speech into audio file
output.save( out_name +".mp3")

#Exit message
print("Text is succesfully converted to speech")

