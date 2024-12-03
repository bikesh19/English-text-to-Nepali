import dict
def search(text):
    if text in dict.roman_to_nepali_dict:
        return True
    else:
        return False

def broken_text(text):
    global length
    if search(text[:4]):
        length=4
        return dict.roman_to_nepali_dict[text[:4]]
    elif search(text[:3]):
        length=3
        return dict.roman_to_nepali_dict[text[:3]]
    elif search(text[:2]):
        length=2
        return dict.roman_to_nepali_dict[text[:2]]
    elif search(text[:1]):
        length=1
        return dict.roman_to_nepali_dict[text[:1]]
    else:
        length=0
        return ""

def check(text):
    nepali_text=""
    while(text):
        nep_text=broken_text(text)
        if length==0:
            break
        nepali_text+=nep_text
        text=text[length:]
    return nepali_text


text=input("enter text in nepali: ")
copy=text;
print(check(copy))



