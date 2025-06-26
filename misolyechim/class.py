class User:
    """"Web sahifa foydalanuvchisi klass"""
    def __init__(self, ism, fism, email):
        """"user xususiyatlari"""
        self.name = ism
        self.user = fism
        self.email = email

    def get_name(self):
        """"ism qaytaradi"""
        return f"Foydalanuvchi ismi: {self.name.title()}"
    
    def get_uname(self):
        """"user name qaytaradi"""
        return f"Username: {self.user}"
    
    def get_email(self):
        """"email qaytaradi"""
        return f"Foydlanvchi emaili: {self.email}"

    def get_info(self):
        return f"User name {self.user}, ismi: {self.name.title()}, emaili: {self.email}"

user1 = User("alijon valiyev", "Alijon001", "alijon@gmail.com")
user2 = User("olim qobilov", "olim1313", "olim2313@gmail.com")
user3 = User("hasan husanov", "h@s@n", "hasan2323@gmail.com")

print(user3.get_info())
print(user3.get_name())
print(user2.get_email())
        