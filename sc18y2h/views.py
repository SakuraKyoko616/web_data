from django.http import JsonResponse
from django.shortcuts import HttpResponse
from .models import professors, module, module_pro, users, module_pro_score


def rate(request, pro_ID, module_ID, year, semester, rating):
    if request.method == 'POST':
        get_m = module.objects.get(module_ID=module_ID, Year=int(year), Semester=int(semester))
        mID = get_m.ID
        module_pro_score.objects.create(ID_id=mID, score=int(rating), pro_Name_id=pro_ID)
        # return HttpResponse("Successfully rate "+pro_ID+" "+str(rating)+" "+"in"+" "+str(year)+" "+str(semester)+" "+module_ID)
        return JsonResponse({'code': 201,
                             'message': "Successfully rate " + pro_ID + " " + rating + " " + "in" + " " + str(
                                 year) + " " + str(semester) + " " + module_ID,
                             'data': [{'pro_ID': pro_ID, 'module_ID': module_ID
                                          , 'year': year, 'semester': semester, 'rating:': rating}]}, status=201)


def list(request):
    get_m_p = module_pro.objects.all()
    get_m = module.objects.all()
    teachers = ""
    result = ""
    for i in get_m:
        for j in get_m_p:
            if j.ID_id == i.ID:
                teachers = teachers + j.pro_Name_id + " "
        result += "| Module Code: " + i.module_ID + "  Module Name: " + i.module_Name + "  Year: " + str(
            i.Year) + "  Semester: " + str(i.Semester) + "  Taught by: " + teachers + '|\n'
        teachers = ""
    # return HttpResponse(result)
    return JsonResponse({'code': 201, 'message': result}, status=201)


def register(request, username, email, password):
    if request.method == 'POST':
        check = users.objects.filter(Username=username)
        if not check:
            users.objects.create(Username=username, Email=email, Password=password)
            # return HttpResponse("Successfully create a user\n")
            return JsonResponse({'code': 201, 'message': "Successfully create a user",
                                 'data': [{'username': username, 'email': email, 'password': password}]}, status=201)
        # return HttpResponse("Username has existed! please register again\n")
        return JsonResponse({'code': 400, 'message': "Username has existed! please register again."}, status=200)


def login(request, username, password):
    try:
        check = users.objects.get(Username=username, Password=password)
        if check:
            # return HttpResponse("Login succeed! Please continue your operation\n")
            return JsonResponse({'code': 201, 'message': "Login succeed! Please continue your operation.\n"}, status=201)
        # return HttpResponse("Username or password is wrong! Please login again\n")
    except :
        return JsonResponse({'code': 400, 'message': "Username or password is wrong! Please login again.\n"}, status=200)

# display all ratings of all professors
def view(request):
    get_m_p_c = module_pro_score.objects.all()
    get_p = professors.objects.all()
    result = ""
    tempScore = 0
    num = 0
    score = 0
    for i in get_p:
        for j in get_m_p_c:
            if j.pro_Name_id == i.pro_ID:
                pro = module_pro_score.objects.filter(pro_Name_id=j.pro_Name_id)
                for k in pro:
                    num += 1
                    tempScore += k.score
                    score = round(tempScore / num)
                num = 0
                tempScore = 0
        result += "The rating of Professor " + i.pro_Name + "(" + i.pro_ID + ") " + "is " + str(score) + "\n"
        score = 0

    # return HttpResponse(result)
    return JsonResponse({'code': 201, 'message': result}, status=201)


def average(request, pro_ID, module_ID):
    get_m = module.objects.all()
    pro_Name = professors.objects.get(pro_ID=pro_ID).pro_Name
    temp = 0
    num = 0
    tempName = ""
    ID_id = 0
    for i in get_m:
        if i.module_ID == module_ID:
            tempName = i.module_Name
            get_score = module_pro_score.objects.filter(pro_Name_id=pro_ID,ID_id=i.ID)
            #print("i.ID:"+str(i.ID))
            for k in get_score:
                temp += k.score
                num += 1
                #print("k.score"+str(k.score))
    moduleName = tempName + " (" + module_ID + ")"

    a_rating = round(temp / num)
    print(moduleName + str(a_rating))
    # return HttpResponse("The rating of " + pro_Name+" (" + pro_ID + ") in "+moduleName + " is "+str(a_rating))
    return JsonResponse({'code': 201,
                         'message': "The rating of " + pro_Name + " (" + pro_ID + ") in " + moduleName + " is " + str(
                             a_rating)}, status=201)
