class EmailMasker:
    def __init__(self, mask_char='x'):
        self.mask_char = mask_char

    def mask(self, email: str):
        mail, domain = email.split('@')
        masked_mail = self.mask_char * len(mail)
        return f"{masked_mail}@{domain}"

class PhoneMasker:
    def __init__(self, mask_char='x', mask_length=3):
        self.mask_char = mask_char
        self.mask_length = mask_length

    def mask(self, phone: str):
        phone_clear = ' '.join(phone.split())
        mask_start_index = len(phone_clear) - self.mask_length
        return ''.join(
            self.mask_char if i >= mask_start_index and not c.isspace() else c
            for i, c in enumerate(phone_clear)
        )

class SkypeMasker:
    def __init__(self, mask_char='x'):
        self.mask_char = mask_char
    
    def mask_login(self, login: str):
        return f'{login[:login.find(':')+1].rstrip()}{self.mask_char*3}'
    
    def mask_html(self, html_login: str):
        return f'{html_login[:html_login.find('skype:')+6].rstrip()}{self.mask_char*3}{html_login[html_login.find('?call'):]}'
    

a = EmailMasker()
a_email = a.mask(email='aaaa@aaa.com')

b = PhoneMasker(mask_length=5)
b_phone = b.mask(phone='+7 666 888 999')

c = SkypeMasker()
c_skype_login = c.mask_login("skype:alex.max")
c_skype_html = c.mask_html("<a href=\"skype:alex.max?call\">skype</a>")

print(a_email, b_phone, c_skype_login, c_skype_html, sep='\n')




