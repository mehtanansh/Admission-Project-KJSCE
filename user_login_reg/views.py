from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm, OTPForm, VerifierRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User, auth
from django.core.mail import EmailMessage
from django.db import models
from twilio.rest import Client
import random
from .models import Applicant
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.conf import settings




from django.shortcuts import render
from django.shortcuts import  redirect
from django.http import HttpResponse
from django.contrib import messages


from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from django.contrib.auth.models import User, auth
from django.core.mail import EmailMessage
from django.db import models
from twilio.rest import Client
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import Seatallo


# Create your views here.
def login(request):
    return render(request, 'user_login_reg/login.html')

def appl_id():
    file1 = open(r"C:\Users\Lenovo\Studies UG + PG\Internship\Umang Patel\admission version 21\appl_ids.txt","r")
    count = int(file1.read())
    file1.close()
    year = 2020
    appl_id = str(year) + '0'*(6 - len(str(count))) + str(count)
    count += 1
    file1 = open(r"C:\Users\Lenovo\Studies UG + PG\Internship\Umang Patel\admission version 21\appl_ids.txt","w")
    file1.write(str(count))
    file1.close()
    return appl_id


def random_username(sender, instance, **kwargs):
    global username
    if not instance.username:
        instance.username = appl_id()
        username = instance.username
models.signals.pre_save.connect(random_username, sender=settings.AUTH_USER_MODEL)


email_otp = str(random.randint(100000, 999999))
mobile_otp = str(random.randint(100000, 999999))


def applicant_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None and user.is_student:
            auth.login(request,user)
            return redirect("applicant-home")
        else:
            messages.info(request,'Invalid credentials')
            return redirect("applicant-login")
    else:
        return render(request,'user_login_reg/applicant_login.html')

def verifier_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None and user.is_verifier:
            auth.login(request,user)
            return redirect("verifier-home")
        else:
            messages.info(request,'Invalid credentials')
            return redirect("verifier-login")
    else:
        return render(request,'user_login_reg/verifier_login.html')

def v_register(request):
    if request.method == 'POST':
        form = VerifierRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for Verifier {username}!')
            return redirect('login')
    else:
        form = VerifierRegisterForm()
    return render(request, 'user_login_reg/v_register.html', {'form':form})


def register(request):
    global email_otp
    global mobile_otp
    global user
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False

            mobileNum = form.cleaned_data.get('mobilenum')
            username = form.cleaned_data.get('username')

            current_site = get_current_site(request)
            mail_subject = 'Activate your admission account.'
            message = render_to_string('user_login_reg/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'otp':email_otp,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user)
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            sendOTP(mobileNum, mobile_otp)
            print('HOME FUNC', request)
            return redirect('verification')
        else:
            return render(request, 'user_login_reg/register.html', {'form':form})
    else:
        form = UserRegisterForm()
        return render(request, 'user_login_reg/register.html', {'form':form})

def otp(request):
    print('OTP FUNC', request)
    global user
    if request.method == 'POST':
        global email_otp
        global mobile_otp
        form = OTPForm(request.POST)
        if mobile_otp == form.data['mob_otp'] and email_otp == form.data['email_otp']:
            user.is_active = True
            user.save()
            username = user.username
            messages.success(request, f'Account for { username } has been created.\nYou can now login with your specified credentials.')
            return redirect('student-login')
        else:
            messages.warning(request, f'OTP did not match')
            return render(request, 'user_login_reg/sendOTP.html', {'form':form})
    else:
        form = OTPForm()
        return render(request, 'user_login_reg/sendOTP.html', {'form':form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        login(request, user)
        return HttpResponse(r'''Thank you for your email confirmation.
            Now you can <a href = "{% url 'login' %}">login</a> to your account.''')
    else:
        return HttpResponse('Activation link is invalid!')


def sendOTP(mobileNum, mobile_otp):
        account_sid = 'ACecc61fad2258c531fc9ad80e5c55b845'
        auth_token = 'f9616905fe1a588098ec836cd7678537'

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='+12564826393',
            body = 'KJSCE ADMISSION PORTAL.\nYour OTP is : ' + str(mobile_otp) + '. Do not share your OTP with anyone.',
            to ='+91' + mobileNum
            )

def main(request):
    return render(request, 'user_login_reg/home.html')


def mainlogin(request):
    return render(request, 'user_login_reg/main_login.html')

def payment(request):
    global user
    if request.method == 'POST':
        form = paymentform(request.POST)
        current_site = get_current_site(request)
        mail_subject = 'Login Credentials for your Account.'
        message = render_to_string('user_login_reg/appid_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'appl_id':appl_id,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':account_activation_token.make_token(user)
                })
        to_email = user.email
        email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
        email.send()

        return redirect('login')
    else:
        return render(request, 'user_login_reg/payment.html')

@login_required
def applicant_home(request):
    users = [item.applId for item in Applicant.objects.all()]
    attemptedExams = []
    if request.user not in users:
        candidate = Applicant(applId = request.user)
    else:
        candidate = Applicant.objects.filter(applId = request.user)[0]
    if request.method == 'POST':
        # firstname = request.POST['firstname']
        # lastname = request.POST['lastname']
        DOB = request.POST['DOB'] if request.POST['DOB'] else None
        # print(DOB)
        emailId = request.POST['emailId']
        parentGuardianName = request.POST['parentGuardianName']
        parentGuardianEmailId = request.POST['parentGuardianEmailId']
        # motherTongue = request.POST['motherTongue']
        addressLine1 = request.POST['addressLine1']
        State = request.POST['State']
        Country = request.POST['Country']
        Nationality = request.POST['Nationality'] if request.POST.get('Nationality', False) else True
        mobile = request.POST['mobile']
        Relation = request.POST['Relation']
        Religion = request.POST['Religion']
        parentGuardianMobile = request.POST['parentGuardianMobile']
        District = request.POST['District']
        Pincode = request.POST['Pincode']
        # board = request.POST['Board']
        # board1 = request.POST['Board1']
        SSCPassingYear = request.POST['SSCPassingYear']
        SSCAggregateMarks = request.POST['SSCAggregateMarks']
        SSCMarksOutOf = request.POST['SSCMarksOutOf']
        HSCMarksOutOf = request.POST['HSCMarksOutOf']
        HSCPassingYear = request.POST['HSCPassingYear']
        HSCAggregateMarks = request.POST['HSCAggregateMarks']
        gender = request.POST.get('gender', False) if request.POST.get('gender', False) else ''
        pwd = True if request.POST.get('pwd', False) else False
        ssc_marksheet = request.FILES['SSCMarksheet'] if 'SSCMarksheet' in request.FILES else None
        hsc_marksheet = request.FILES['HSCMarksheet'] if 'HSCMarksheet' in request.FILES else None
        leaving_domicile = request.FILES['leavingCertificate_Domicile'] if 'leavingCertificate_Domicile' in request.FILES else None
        birth_bonafide_leaving = request.FILES['birthCertificate_Bonafide_LeavingCerificate'] if 'birthCertificate_Bonafide_LeavingCerificate' in request.FILES else None
        signature = request.FILES['signature'] if 'signature' in request.FILES else None
        candidate_photo = request.FILES['candidatePhoto'] if 'candidatePhoto' in request.FILES else None
        cet_marksheet = request.FILES['cet_marksheet'] if 'cet_marksheet' in request.FILES else None
        jee_mains_markssheet = request.FILES['jee_mains_markssheet'] if 'jee_mains_markssheet' in request.FILES else None
        jee_adv_markssheet = request.FILES['jee_adv_markssheet'] if 'jee_adv_markssheet' in request.FILES else None
        HSCPhysicsMarks = request.POST['HSCPhysicsMarks']
        HSCChemistryMarks = request.POST['HSCChemistryMarks']
        HSCMathMarks = request.POST['HSCMathematicsMarks']
        SET = request.POST['SET'] if request.POST.get('SET', False) else None
        jee_mains = request.POST['JEEMainsMarks'] if request.POST.get('JEEMainsMarks', False) else None
        jee_adv = request.POST['JEEAdvanceMarks'] if request.POST.get('JEEAdvanceMarks', False) else None
        cet = request.POST['cetmarks'] if request.POST.get('cetmarks', False) else 22
        cet_physics = request.POST['CETPhysicsMarks'] if request.POST.get('CETPhysicsMarks', False) else None
        cet_maths = request.POST["CETMathematicsMarks"] if request.POST.get("CETMathematicsMarks", False) else None
        cet_chemistry = request.POST['CETChemistryMarks'] if request.POST.get('CETChemistryMarks', False) else None
        # print(cet)
        has_given_cet = True if request.POST.get('mhtcet', False) else False
        has_given_jee_main = True if request.POST.get('jeeM', False) else False
        has_given_jee_adv = True if request.POST.get('jeeA', False) else False
        # dob = DOB.strftime("%Y-%m-%d") if DOB else None
        attemptedExams = [has_given_cet, has_given_jee_main, has_given_jee_adv, DOB]
        # annualIncome = request.POST['annualIncome']

        candidate.applId = request.user
        candidate.DOB = DOB
        candidate.mobile = mobile
        candidate.parent_guardianName = parentGuardianName
        candidate.parent_guardianEmail = parentGuardianEmailId
        candidate.parent_guardianMobile = parentGuardianMobile
        # candidate.mother_tongue = motherTongue
        candidate.relation = Relation
        candidate.religion = Religion
        candidate.addr_line_1 = addressLine1
        candidate.state = State
        candidate.country = Country if Country else 'India'
        candidate.district = District
        candidate.pincode = Pincode
        candidate.nationality = Nationality
        candidate.ssc_aggregate_marks = float(SSCAggregateMarks) if SSCAggregateMarks else None
        candidate.ssc_marks_out_of = float(SSCMarksOutOf) if SSCMarksOutOf else None
        candidate.hsc_marks_out_of = float(HSCMarksOutOf) if HSCMarksOutOf else None
        candidate.ssc_year = SSCPassingYear
        # candidate.ssc_board = board
        # candidate.hsc_board = board1
        candidate.hsc_physics_marks = float(HSCPhysicsMarks) if HSCPhysicsMarks else None
        candidate.hsc_math_marks = float(HSCMathMarks) if HSCMathMarks else None
        candidate.hsc_chemistry_marks = float(HSCChemistryMarks) if HSCChemistryMarks else None
        candidate.gender = gender
        candidate.hsc_aggregate_marks = float(HSCAggregateMarks) if HSCAggregateMarks else None
        candidate.hsc_year = HSCPassingYear
        candidate.ssc_result = ssc_marksheet
        candidate.pwd = pwd
        candidate.hsc_result = hsc_marksheet
        candidate.leaving_domicile = leaving_domicile
        candidate.birth_bonafide_leaving = birth_bonafide_leaving
        candidate.candidate_photo = candidate_photo
        candidate.jee_mains_markssheet = jee_mains_markssheet
        candidate.jee_adv_markssheet = jee_adv_markssheet
        candidate.cet_marksheet = cet_marksheet
        candidate.signature = signature
        candidate.SET = float(SET) if SET else None
        candidate.cet = int(cet) if cet else None
        candidate.cet_physics = int(cet_physics) if cet_physics else None
        candidate.cet_maths = int(cet_maths) if cet_maths else None
        candidate.cet_chemistry = int(cet_chemistry) if cet_chemistry else None
        candidate.jee_mains = int(jee_mains) if jee_mains else None
        candidate.jee_adv = int(jee_adv) if jee_adv else None
        # candidate.domicile = domicile
        # candidate.birth_cert = birth_cert
        candidate.save()
    return render(request, 'user_login_reg/applicant_home.html', {'candidate' : candidate, 'attemptedExams': attemptedExams})


@login_required
def display(request):
    users = [item.applId for item in Normal_User.objects.all()]
    if request.user not in users:
        candidate = Normal_User(applId = request.user)
    else:
        candidate = Normal_User.objects.filter(applId = request.user)[0]


    return render(request, 'user/display.html',{'candidate' : candidate})



def applicant_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None and user.is_student:
            auth.login(request,user)
            return redirect("applicant-home")
        else:
            messages.info(request,'Invalid credentials')
            return redirect("applicant-login")
    else:
        return render(request,'user_login_reg/applicant_login.html')



# Create your views here.
def logi(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None and user.is_admin:

            auth.login(request,user)
            return redirect("adm")
        else:

            messages.info(request,'Invalid credentials')
            return redirect("logi")
    else:

        return render(request,'user_login_reg/logi.html')

@login_required
def adm(request):
        return render(request,'user_login_reg/naya.html')

@login_required
def seat(request):
    if request.method=='POST':
        seatallo=Seatallo()
        seatallo.glce=request.POST['c1'] if request.POST.get('c1', False) else None
        seatallo.capce= request.POST['c2']if request.POST.get('c2', False) else None
        seatallo.ilsce=request.POST['c3']if request.POST.get('c3', False) else None
        seatallo.nrice=request.POST['c4']if request.POST.get('c4', False) else None
        seatallo.ciwgcce=request.POST['c5']if request.POST.get('c5', False) else None
        seatallo.pioce=request.POST['c6']if request.POST.get('c6', False) else None
        seatallo.fnce=request.POST['c7']if request.POST.get('c7', False) else None

        seatallo.glee=request.POST['e1']if request.POST.get('e1', False) else None
        seatallo.capee= request.POST['e2']if request.POST.get('e2', False) else None
        seatallo.ilsee=request.POST['e3']if request.POST.get('e3', False) else None
        seatallo.nriee=request.POST['e4']if request.POST.get('e4', False) else None
        seatallo.ciwgcee=request.POST['e5']if request.POST.get('e5', False) else None
        seatallo.pioee=request.POST['e6']if request.POST.get('e6', False) else None
        seatallo.fnee=request.POST['e7']if request.POST.get('e7', False) else None



        seatallo.glete=request.POST['t1']if request.POST.get('t1', False) else None
        seatallo.capete= request.POST['t2']if request.POST.get('t2', False) else None
        seatallo.ilsete=request.POST['t3']if request.POST.get('t3', False) else None
        seatallo.nriete=request.POST['t4']if request.POST.get('t4', False) else None
        seatallo.ciwgcete=request.POST['t5']if request.POST.get('t5', False) else None
        seatallo.pioete=request.POST['t6']if request.POST.get('t6', False) else None
        seatallo.fnete=request.POST['t7']if request.POST.get('t7', False) else None


        seatallo.glit=request.POST['i1']if request.POST.get('i1', False) else None
        seatallo.capit= request.POST['i2']if request.POST.get('i2', False) else None
        seatallo.ilsit=request.POST['i3']if request.POST.get('i3', False) else None
        seatallo.nriit=request.POST['i4']if request.POST.get('i4', False) else None
        seatallo.ciwgcit=request.POST['i5']if request.POST.get('i5', False) else None
        seatallo.pioit=request.POST['i6']if request.POST.get('i6', False) else None
        seatallo.fnit=request.POST['i7']if request.POST.get('i7', False) else None


        seatallo.glme=request.POST['m1']if request.POST.get('m1', False) else None
        seatallo.capme= request.POST['m2']if request.POST.get('m2', False) else None
        seatallo.ilsme=request.POST['m3']if request.POST.get('m3', False) else None
        seatallo.nrime=request.POST['m4']if request.POST.get('m4', False) else None
        seatallo.ciwgcme=request.POST['m5']if request.POST.get('m5', False) else None
        seatallo.piome=request.POST['m6']if request.POST.get('m6', False) else None
        seatallo.fnme=request.POST['m7']if request.POST.get('m7', False) else None
        seatallo.save()
        return redirect("adm")

    else:
        return render(request,'user_login_reg/seat.html')


def logo(request):
    logout(request)
    return render(request,'user_login_reg/logo.html')

@login_required
def verifier_home(request):
    if request.method == 'POST':
        A_ID = request.POST['Application_ID']
        sc=Applicant.objects.filter(applId=int(A_ID)).exists()
        if sc:
            if A_ID.is_student:
               # auth.login(request,user)
                return redirect("verifier-verify",{A_ID})
        else:
            messages.info(request,f'Invalid Application ID')
            return redirect("verifier-home")
    else:
        return render(request,"user_login_reg/verifier_home.html")

@login_required 
def verifier_Verify(request):
    pass


@login_required 
def Ranklist_CET(request):
    Rank_List1=Applicant.objects.all().order_by('-cet', '-cet_maths','-cet_physics','-cet_chemistry')
    return redirect ("Ranklist-CET",{Rank_List1})

@login_required 
def Ranklist_JEE(request):
    Rank_List2=Applicant.objects.all().order_by('-jee_mains','-jee_adv')
    return redirect ("Ranklist-JEE",{Rank_List2})

@login_required 
def Ranklist_SET(request):
    Rank_List3=Applicant.objects.all().order_by('-SET')
    return redirect ("Ranklist-SET",{Rank_List3})

# def applicant_Verifier_login(request):
#     return render(request,'user_login_reg/verifier_Verify.html')