from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from django.db.models import  Q

class EmailBaccend(ModelBackend):
    
    def authenticate(self,request,username=None,password=None,**kwargs):
        try:
            user=User.objects.get(
                Q(username__iexact=username) |
                Q(email__iexact=username)
            )
        except User.DoesNotExist:
            return None
        except User.MultipleObjectsReturned:
            return User.objects.filter(email=username).order_by().first
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
              return user
            
    