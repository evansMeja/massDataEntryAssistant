def processInitial(s):
    n = 0
    c = 0
    st = 0
    e = 0
    notD = 0
    lD = 0
    lineLength= len(s)
    missingNumber = 0

    sN=0

    ssN=0
    eeN=0
    for i in s:
        if i.isnumeric() and notD == 1:
            lD = 2
            
        if i.isalpha() and notD == 0:
            notD = 1
            lD = 1
            n = 1
            st = c
        else:
            if n == 1 and i.isnumeric():
                if  sN == 0:
                    sN = 1
                    ssN = c
                else:  
                    if lineLength-1 == c:
                        eeN = c
                        break    
                e = c
                break
            else:
                if lineLength-1 == c and lD == 1:
                    missingNumber = 1
                    e = c
                    break           
        c = c + 1
    data = {}
    data['hasPhone'] = False
    nameArray = s[st:e].strip().split()
    if(len(nameArray) == 3):
        data['first_name'] = nameArray[0]
        data['middle_name'] = nameArray[1]
        data['last_name'] = nameArray[2]
    else:
        data['first_name'] = nameArray[0]
        data['middle_name'] = ""
        data['last_name'] = nameArray[1]
    if missingNumber == 0:
        data['hasPhone'] = True
        data['email'] = nameArray[-2].lower() + nameArray[-1].lower() +"@voter.com"
        data['username'] = nameArray[-2].lower() + nameArray[-1].lower() +"@voter.com"
        data['name'] = s[st:e]
        data['phone'] = s[ssN:] 
        return data
    else:
        data['hasPhone'] = False
        data['email'] = nameArray[-1].lower()+"@gmail.com"
        data['username'] = nameArray[-1].lower()+"@gmail.com"
        data['name'] = nameArray[0] + " " + nameArray[1]
        data['phone'] = ""
        return data


ward_obj = ward.objects.get(ward_name="Township")

county_obj = county.objects.get(county_name="Bungoma")

sub_county_obj = sub_county.objects.get(county_code=county_obj,sub_county_code=ward_obj.sub_county_code.sub_county_code)



with open("C:/Users/Admin/Desktop/scrap/data.txt") as d:
    c = d.readlines()

    
c = [x.strip() for x in c]

x=1
for i in c:
    res = processInitial(i)
    
    if res['hasPhone']:
        print("saving "+ res['name'])
    else:
        print("saving "+ res['name'])
    x=x+1

    # new_system_user_obj = User.objects.create_user(username=res['email'],password="123",email=res['email'])
    # new_system_user_obj.first_name = res['first_name']
    # new_system_user_obj.last_name = res['last_name']
    # new_system_user_obj.save()

    # user_obj = user()
    # user_obj.first_name = res['first_name']
    # user_obj.middle_name = res['middle_name']
    # user_obj.last_name = res['last_name']
    # user_obj.phone =res['phone']
    # user_obj.email = res['email']
    # user_obj.priviledge = 0
    # user_obj.system_user_i = unique_user_slug_generator(user_obj)
    # user_obj.status = 1
    # user_obj.verification_code = unique_verification_slug_generator(user_obj)
    # user_obj.user = new_system_user_obj
    # user_obj.save()
    

    # voter_obj = voter()
    # voter_obj.county = county_obj
    # voter_obj.sub_county = sub_county_obj
    # voter_obj.ward = ward_obj
    # voter_obj.user = user_obj
    # voter_obj.voter_id = unique_voter_slug_generator(voter_obj)
    # voter_obj.id_number = 123
    # voter_obj.status = 0
    # voter_obj.save()

    # verification_code = random_string_generator(6)
    # verification_obj = verification()
    # verification_obj.verification_type = 0
    # verification_obj.status=0
    # verification_obj.owner = user_obj
    # verification_obj.value = verification_code
    # verification_obj.save()
