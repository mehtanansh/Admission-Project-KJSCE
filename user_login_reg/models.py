from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField('student status', default=False)
    is_verifier = models.BooleanField('verifier status', default=False)
    is_admin = models.BooleanField('admin status', default=False)

class Applicant(models.Model):
	# user details
	applId = models.ForeignKey(User, on_delete=models.CASCADE, primary_key = True)
	DOB = models.DateField(null = True, default = None)
	mobile = models.CharField(max_length=10, default = '')
	gender = models.CharField(max_length=6, default = '')


	parent_guardianName = models.CharField(max_length=20, default = '')
	parent_guardianEmail = models.EmailField(default = '')
	parent_guardianMobile = models.CharField(max_length = 10, default = '')
	father_occ = models.CharField(max_length=10, default = '')
	mother_occ = models.CharField(max_length=10, default = '')
	family_ann_inc = models.CharField(max_length=20, default = '')
	relation = models.CharField(max_length=10, default = '')
	pwd = models.BooleanField(default=False)
	mother_tongue = models.CharField(max_length=15, default = '')
	defence_type = models.CharField(max_length=15, default = '')
	religion = models.CharField(max_length=15, default = '')

	# address
	addr_line_1 = models.TextField()
	state = models.CharField(max_length=10, default = '')
	country = models.CharField(max_length=10, default = 'India')
	district = models.CharField(max_length=10, default = '')
	pincode = models.CharField(max_length=10, default = '')
	nationality = models.CharField(max_length=10, default = 'Indian')

	# academic details
	ssc_aggregate_marks = models.DecimalField(null = True, decimal_places = 2, max_digits = 5, default = None)
	ssc_marks_out_of = models.DecimalField(null = True, decimal_places = 2, max_digits = 5, default = None)
	ssc_year = models.CharField(max_length=10, default = '')
	ssc_board = models.CharField(max_length=10, default = '')
	hsc_aggregate_marks = models.DecimalField(null = True, decimal_places = 2, max_digits = 5, default = None)
	hsc_marks_out_of = models.DecimalField(null = True, decimal_places = 2, max_digits = 5, default = None)
	hsc_physics_marks = models.DecimalField(null = True, decimal_places = 2, max_digits = 5, default = None)
	hsc_math_marks = models.DecimalField(null = True, decimal_places = 2, max_digits = 5, default = None)
	hsc_chemistry_marks = models.DecimalField(null = True, decimal_places = 2, max_digits = 5, default = None)
	hsc_year = models.CharField(max_length=10, default = '')
	hsc_board =models.CharField(max_length=10, default = '')
	SET = models.IntegerField(null = True, default = None)
	cet = models.IntegerField(null = True, default = None)
	cet_physics = models.IntegerField(null = True, default = None)
	cet_maths = models.IntegerField(null = True, default = None)
	cet_physics = models.IntegerField(null = True, default = None)
	cet_chemistry = models.IntegerField(null = True, default = None)
	jee_mains = models.IntegerField(null = True, default = None)
	jee_adv = models.IntegerField(null = True, default = None)

	# docs
	candidate_photo = models.ImageField(default = None)
	signature = models.ImageField(default = None)
	ssc_result = models.ImageField(default = None)
	hsc_result = models.ImageField(default = None)
	hsc_LC = models.ImageField(default = None)
	cet_result = models.ImageField(default = None)
	jee_mains_result = models.ImageField(default = None)
	jee_adv_result = models.ImageField(default = None)
	set_result = models.ImageField(default = None)
	minority_proof = models.ImageField(default = None)
	nationality_proof = models.ImageField(default = None)
	tfws_proof = models.ImageField(default = None)
	maharashtra_citizen_proof = models.ImageField(default = None)
	address_proof = models.ImageField(default = None)

	# verified docs
	ssc_marksheet_verified = models.BooleanField(default = False)
	hsc_marksheet_verified = models.BooleanField(default = False)
	cet_marksheet_verified = models.BooleanField(default = False)
	jee_mains_markssheet_verified = models.BooleanField(default = False)
	jee_adv_markssheet_verified = models.BooleanField(default = False)
	signature_verified = models.BooleanField(default = False)
	candidate_photo_verified = models.BooleanField(default = False)
	all_verified = models.BooleanField(default = False)

	def __str__(self):
		return self.applId.username

class Verifier(models.Model):
	username = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=True)




# Create your models here.

class Seatallo(models.Model):
    glce = models.IntegerField(null = True, default = None)
    capce = models.IntegerField(null = True, default = None)
    ilsce = models.IntegerField(null = True, default = None)
    nrice = models.IntegerField(null = True, default = None)
    ciwgcce = models.IntegerField(null = True, default = None)
    pioce = models.IntegerField(null = True, default = None)
    fnce = models.IntegerField(null = True, default = None)

    glee = models.IntegerField(null = True, default = None)
    capee = models.IntegerField(null = True, default = None)
    ilsee = models.IntegerField(null = True, default = None)
    nriee = models.IntegerField(null = True, default = None)
    ciwgcee = models.IntegerField(null = True, default = None)
    pioee = models.IntegerField(null = True, default = None)
    fnee = models.IntegerField(null = True, default = None)

    glete = models.IntegerField(null = True, default = None)
    capete = models.IntegerField(null = True, default = None)
    ilsete = models.IntegerField(null = True, default = None)
    nriete = models.IntegerField(null = True, default = None)
    ciwgcete = models.IntegerField(null = True, default = None)
    pioete = models.IntegerField(null = True, default = None)
    fnete = models.IntegerField(null = True, default = None)

    glit = models.IntegerField(null = True, default = None)
    capit = models.IntegerField(null = True, default = None)
    ilsit = models.IntegerField(null = True, default = None)
    nriit = models.IntegerField(null = True, default = None)
    ciwgcit = models.IntegerField(null = True, default = None)
    pioit = models.IntegerField(null = True, default = None)
    fnit = models.IntegerField(null = True, default = None)



    glme = models.IntegerField(null = True, default = None)
    capme = models.IntegerField(null = True, default = None)
    ilsme = models.IntegerField(null = True, default = None)
    nrime = models.IntegerField(null = True, default = None)
    ciwgcme = models.IntegerField(null = True, default = None)
    piome = models.IntegerField(null = True, default = None)
    fnme = models.IntegerField(null = True, default = None)

    # def __str__(self):
    #     return self.applId.username
