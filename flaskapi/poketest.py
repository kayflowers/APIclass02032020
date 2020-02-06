import requests

GenderURL= "https://api.genderize.io?name="

gend = requests.get(f"{GenderURL}Karen")
gend = gend.json
print(gend(['gender'][0]))



