#---------------------------------------------------> Regular Expressions <----------------------------------------------

# P-1 : Write program to find if a string has only octal digits, given string ['789','123','004']

"""import re
a=['789','123','004']
for i in a :
    if re.fullmatch(r'[0-7]+',i):
        print(f"{i} is octal")
    else:
        print(f"{i} is Not octal")"""

########################################################

# P-2 : Extract user id , domain name and suffix from the email addresses
# emails: zuck@facebook.com
# sunder33@google.com
# jeff42@amazon.com

# import re

# emails = ['zuck@facebook.com', 'sunder33@google.com', 'jeff42@amazon.com']
# patterns = r"(\w+)@(\w+)\.(\w+)"

# for email in emails:
#     match = re.match(patterns, email)
#     if match:
#         user_id, domain, suffix = match.groups()
#         print(f"Email   : {email}")
#         print(f"  User ID: {user_id}")
#         print(f"  Domain : {domain}")
#         print(f"  Suffix : {suffix}")
#         print()

##########################################################################

# Split the following irregular sentence into proper words

# sentence = """A, very very; irregular_sentence"""

# ## expected outout: A very very irregular

# import re
# sentence = "A, very very; irregular_sentence"
# cleaned = re.sub(r'[^\w\s]', ' ', sentence)  
# cleaned = cleaned.replace('_', ' ')
# final = re.sub(r'\s+', ' ', cleaned).strip()
# print(final)

########################################################################

# Clean up the following tweet so that it contains only the user's message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.

# #tweet'Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0px0d cc: @garybernhardt #rstats''"

# Regular Expression

# ##desired_output = 'Good advice What I would do differently if I was learning to code today'

# import re

# tweet = "Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0px0d cc: @garybernhardt #rstats"

# # Remove RTs, CCs
# tweet = re.sub(r'\b(RT|cc)\b', '', tweet)

# # Remove mentions
# tweet = re.sub(r'@\w+', '', tweet)

# # Remove hashtags
# tweet = re.sub(r'#\w+', '', tweet)

# # Remove URLs
# tweet = re.sub(r'http\S+', '', tweet)

# # Remove punctuation
# tweet = re.sub(r'[^\w\s]', '', tweet)

# # Remove extra spaces
# tweet = re.sub(r'\s+', ' ', tweet).strip()

# print(tweet)

##############################################################################################

# Extract all the text portions between the tags from the following HTML page
# https://raw.githubusercontent.com/selva86/datasets/master/sample.html
# Code to retrieve the HTML page is given below:
# import requests
# r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
# r.text # html text is contained here
# Regular Expression
# desired_output = ['Your Title Here', 'Link Name', 'This is a Header', 
#                   'This is a Medium Header', 'This is a new paragraph!', 
#                   'This is a another paragraph!', 'This is a new sentence without a paragraph break, in bold italics.']


# import requests
# import re

# url = "https://raw.githubusercontent.com/selva86/datasets/master/sample.html"
# r = requests.get(url)
# html = r.text
# # Get all text between HTML tags using regular expression
# text_list = re.findall(r'>([^<]+)<', html)

# # Clean and filter
# text_list = [text.strip() for text in text_list if text.strip()]

# print(text_list)

###############################################################################################

# Given below list of words, identify the words that begin and end with the same character.

# civic
# trust
# widows
# maximum
# museums
# aa
# as

import re

words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']

pattern = r'^(.).*\1$'

for word in words:
    if re.match(pattern, word, re.IGNORECASE):  # case-insensitive match
        print(word)


