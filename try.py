import requests
# api key     06f23494-33d4-4b72-98eb-d92603df3caa
# email_address = "2003012005@ipec.org.in"
def check(email):
    print(email+"   ",end="")
    api_key = "06f23494-33d4-4b72-98eb-d92603df3caa"
    response = requests.get(
        "https://isitarealemail.com/api/email/validate",
        params = {'email': email},
        headers = {'Authorization': "Bearer " + api_key })
    status = response.json()['status']
    if status == "valid":
        print("email is valid")
    elif status == "invalid":
        print("email is invalid")
    else:
        print("email was unknown")


for i in range(100):
    temp=2003012000+i
    check(f"{temp}@ipec.org.in")