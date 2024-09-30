from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import (BaseUserManager,
                                        AbstractBaseUser,
                                        PermissionsMixin,)


class AllUser(BaseUserManager):
    def create_user(self, username, email, phone, password=None, first_name=None, last_name=None):
        if not phone:
            raise ValueError("Need Phone")
        
        if not email:
            raise ValueError("Need Email")
        
        if not username:
            raise ValueError("Need Username")
        
        if not first_name:
            raise ValueError("Need Name")
        
        if not last_name:
            raise ValueError("Need Family Name")
        
        email = self.normalize_email(email)

        user = self.model(
            email=email,
            phone=phone,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staff(self, username, email, phone, password, first_name, last_name):
        user = self.create_user(
            phone=phone,
            email=email,
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_staff = True
        user.is_active  = True
        user.is_superuser = False        
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, phone, password, first_name, last_name):
        user = self.create_user(
            phone=phone,
            email=email,
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_staff = True
        user.is_active  = True
        user.is_superuser = True        
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    numbers      = RegexValidator(r'^[0-9]*$', message="Numbers")
    phone        = models.CharField(unique=True, max_length=11, validators=[numbers])
    email        = models.EmailField(unique=True)
    username     = models.CharField(max_length=255, unique=True)
    first_name   = models.CharField(max_length=127, null=True, blank=True)
    last_name    = models.CharField(max_length=127, null=True, blank=True)
    is_active    = models.BooleanField(default=True, null=False)
    is_staff     = models.BooleanField(default=False, null=False)
    is_superuser = models.BooleanField(default=False, null=False)

    # TODO: Private account status
    is_private   = models.BooleanField(default=False, null=False)

    objects = AllUser()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username', 'phone', 'first_name', 'last_name']
    
    def __str__(self):
        return f"{self.email}"
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'



class Profile(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    email           = models.EmailField(unique=True)
    phone           = models.CharField(unique=True, max_length=11)
    username        = models.CharField(max_length=255, unique=True)
    first_name      = models.CharField(max_length=127, null=True, blank=True)
    last_name       = models.CharField(max_length=127, null=True, blank=True)
    bio             = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    website         = models.URLField(blank=True, null=True)
    location        = models.CharField(max_length=144, blank=True, null=True)
    birth_date      = models.DateField(blank=True, null=True)
    is_private      = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
