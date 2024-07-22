from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import  BaseUserManager, AbstractBaseUser, PermissionsMixin


class AllUser(BaseUserManager):
    def create_user(self, phone, email=None, password=None, first_name=None, last_name=None):
        if not phone:
            raise ValueError('')

        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staff(self, phone, email, password, first_name, last_name):
        user = self.create_user(
            email=email,
            phone=phone,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_staff = True
        user.is_active  = True
        user.is_superuser = False        
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, email, password, first_name, last_name):
        user = self.create_user(
            email=email,
            phone=phone,
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
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', message='Only ASCII characters')
    numbers      = RegexValidator(r'^[0-9a]*$', message='Only Numbers')
    phone        = models.CharField(max_length=11, unique=True, validators=[numbers])
    email        = models.EmailField(unique=True, max_length=244, blank=True, null=True)
    first_name   = models.CharField(max_length=30, null=True, blank=True)
    last_name    = models.CharField(max_length=50, null=True, blank=True)
    is_active    = models.BooleanField(default=True, null=False)
    is_staff     = models.BooleanField(default=False, null=False)
    is_superuser = models.BooleanField(default=False, null=False)

    objects = AllUser()

    USERNAME_FIELD  = 'phone'
    REQUIRED_FIELDS = ['email', 'username', 'first_name', 'last_name']
    
    @property
    def fullName(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.phone}"
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    class Meta:
        managed = True
        ordering = ['id']
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class OTP(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    counter    = models.PositiveSmallIntegerField(default=3)
    otp        = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} {self.otp}'


class Profile(models.Model):
    user       = models.OneToOneField(User, on_delete=models.CASCADE)
    phone      = models.CharField(max_length=11)
    email      = models.EmailField(blank=True, null=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name  = models.CharField(max_length=50, null=True, blank=True)
    
    @property
    def fullName(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self) -> str:
        return f"{self.pk} {self.user} {self.email}"
    
    class Meta:
        managed = True
        ordering = ['last_name']
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
