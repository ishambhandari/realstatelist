from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('users must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name = name)
        name = self.name
        #built in function to hash password
        user.set_password(password)
        user.save() #using = self._db in parameter if using multiple application

        return user 
    
    def create_superuser(self, email, name, password, ):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user 

class UserAccount(AbstractBaseUser, PermissionsMixin):
    '''Model used to create user manager '''
    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length= 255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

#This is the instance of user account manager to manage user accounts.
    object = UserAccountManager()

#changes default pk from user name to email and name as required field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self): 
        return self.name 
    
    def get_short_name(self):
        return self.name 
    
    def __str__(self):
        return self.email
