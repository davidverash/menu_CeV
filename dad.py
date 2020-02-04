import pyperclip,re



urlRegex = re.compile(r'https?://(www\.)?(\w+)+(\.\w+)')

phoneRegex = re.compile(r'''(
(\d{2,3}|\(\d{2,3}\))? 
(\s|-|\.)? 
(\d{5}) 
(\s|-|\.)  
(\d{4}) 
)''', re.VERBOSE)

emailRegex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

url = 'https://www.facebook.com'
phone = '86 99966-7232'
print(urlRegex.search(url).group())
print(phoneRegex.search(phone).group())

