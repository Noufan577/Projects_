
class User:
    def __init__(self,name):
        self.username = name
        self.is_loggedin = False

    def authenticator(funct):
        def wrapper(self,*args,**kwargs):
            if (self.is_loggedin):
                funct(self,*args,**kwargs)
            else:
                print("User not logged in")
        return wrapper
    def login(self):
        self.is_loggedin=True
    @authenticator
    def create_post(self):
        print(f"Postcreated by {self.username}")


                
u=User("Abhi")
print(u.username)
print(u.is_loggedin)

u.login()
u.create_post()