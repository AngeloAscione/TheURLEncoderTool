#Importing section
from time import sleep
#Trying to import "termcolor", if not installed the except section will install it
try:
    from termcolor import colored
except ImportError:
        import os
        ret_code = os.system('pip install termcolor')
        if(ret_code != 0):
            print('termcolor installation failed.')
            exit()
        from termcolor import colored
        print (colored('termcolor has been installed','green'))
        
#Defining encode function
def encode(url, dic):
    encoded_string = ""
    words = url.split(' ')
    for word in words:
        for letter in word:
            if letter in dic.keys():
                encoded_string += dic[letter]
            else:
                encoded_string += letter
        encoded_string += '%20'
    return encoded_string[:-3]

#Defining decode function
def decode(url, dic):
    for value in dic.values():
        if value in url:
            key = [k for k, v in dic.items() if v == value][0]
            url = url.replace(value, key)
    return url

#Dictionary used for encoding and decoding
char_dict = {' ': '%20', '!': '%21', '"': '%22', '#': '%23', '$': '%24', '%': '%25', '&': '%26', "'": '%27', '(': '%28', ')': '%29', '*': '%2A', '+': '%2B', ',': '%2C', '-': '%2D', '.': '%2E', '/': '%2F', ':': '%3A', ';': '%3B', '<': '%3C', '=': '%3D', '>': '%3E', '?': '%3F', '@': '%40', '[': '%5B', '\\': '%5C', ']': '%5D', '^': '%5E', '_': '%5F', '`': '%60', '{': '%7B', '|': '%7C', '}': '%7D', '~': '%7E'}


#Defining menu function
def menu():
    print(colored("***************************************", 'blue'))
    print(colored("* Welcome in The URL Encoder Tool     *", 'blue'))
    print(colored("* Choose which option you want to use *", 'blue'))
    print(colored("* [1]Encode                           *", 'blue'))
    print(colored("* [2]Decode                           *", 'blue'))
    print(colored("* [0]Quit                             *", 'blue'))
    print(colored("*               By ZhOm & Snap v(1.1) *", 'blue'))
    print(colored("***************************************", 'blue'))
    return int(input(colored("**--> ", 'blue')))

#Defining main function
def main():
    choise = 0
    while True:
        choise = menu()
        print('')
        
        if choise == 1:
            print(colored("**Paste the URL to encode**", 'blue'))
            encoded_url = encode(input(colored("**--> ", 'blue')), char_dict)
            print(colored('**Here is your encoded URL --> ', 'blue') + colored(encoded_url, 'green') + colored('**', 'blue'))
            sleep(3)
        elif choise == 2:
            print(colored("**Paste the URL to decode**", 'blue'))
            decoded_url = decode(input(colored("**--> ", 'blue')), char_dict)
            print(colored('**Here is your decoded URL --> ', 'blue') + colored(decoded_url, 'green') + colored('**', 'blue'))
            sleep(3)
        elif choise == 0:
            exit()
        else:
            print(colored("**Not Valid**", 'red'))
            sleep(1)

        print('')

#Starting of the program
if __name__ == '__main__':
    print('')
    main()
