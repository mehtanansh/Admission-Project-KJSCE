from django.contrib import admin
from .models import Applicant, Verifier, User

from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Seatallo
# Register your models here.




class SeatalloAdmin(admin.ModelAdmin):
     list_display=['glce','capce','ilsce','nrice','ciwgcce','pioce','fnce','glee','capee','ilsee','nriee','ciwgcee','pioee','fnee','glete','capete','ilsete','nriete','ciwgcete','pioete','fnete','glit','capit','ilsit','nriit','ciwgcit','pioit','fnit','glme','capme','ilsme','nrime','ciwgcme','piome','fnme']



admin.site.register(Seatallo,SeatalloAdmin)

# from .models import Applicant
# Register your models here.


admin.site.register(Applicant)
admin.site.register(Verifier)

admin.site.register(User)
