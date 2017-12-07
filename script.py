import mechanize
import webbrowser
import datetime
import re
from selenium import webdriver


#user input part

number_of_problems=input('enter number of problems : ')
#Date=input('enter date1 (MM/DD/YYYY) : ')
starthour=input('enter start hour (according to utc in military time ) : ')
duration = input('enter duration in hours : ')
diff = input('enter difficulty level (1-10) : ')

start = "00"
date1 = ""
difficulty = str(diff)
no =str(number_of_problems)

Date=now = datetime.datetime.now()

date1=str(Date)

if starthour < 10:
	start = "0"+str(starthour)
else :
	start = str(starthour)

end = str(starthour+duration)


day = Date.day
month = Date.month
year = Date.year

day1=""
month1=""


if day<10:
	day1 = "0"+str(day)
else:
	day1 = str(day)

if month<10:
	month1 = "0"+str(month)
else:
	month1 = str(month)

date1=month1+"/"+day1+"/"+str(year)
print "creating contest on : "+date1





# contest creation part


url = "https://a2oj.com/signin"

br = mechanize.Browser()


#br.set_all_readonly(False)
br.set_handle_robots(False) # ignore robots
br.set_handle_refresh(False)

print 'initializing signin'

response = br.open(url)
#print response.read()

'''
for form in br.forms():
    print "Form name:", form.name
    print form
'''
br.select_form(nr=0)
br.set_all_readonly(False)



br["Username"]="your username"
br["Password"]="your password"

res = br.submit()


print 'signin successful'
'''
content = res.read()
with open("mechanize_results.html", "w") as f:
    f.write(content)

webbrowser.open("mechanize_results.html")
'''

url = "https://a2oj.com/createcontest"


br.set_handle_robots(False) # ignore robots
br.set_handle_refresh(False)

response = br.open(url)
#print response.read()

'''
for form in br.forms():
    print "Form name:", form.name
    print form
'''

br.select_form(nr=0)
br.set_all_readonly(False)


now = datetime.datetime.now()

#date1 = "12/07/2017"



br["Name"] = "practice"
br["StartDate"] = date1
br["StartTimeHour"]=["09",]
br["StartTimeMinute"]=["00",]
br["EndDate"]=date1
br["EndTimeHour"]=["10",]
br["EndTimeMinute"]=["00",]
br["BlindDuration"]="0"
br["ContestType"]=["Private",]

res = br.submit()

print 'contest created'

content = res.read()

#print res

'''
for form in br.forms():
    print "Form name:", form.name
    print form
'''
base_url = br.geturl()

# extracting id of the contest created to add random problems 

numbers = re.findall('\d+',base_url);

id = 0

for i in numbers:
	id = i

add_problems_url="https://a2oj.com/randomproblems?ID="

add_problems_url = add_problems_url +str(id)

#print add_problems_url

response = br.open(add_problems_url)


'''
for form in br.forms():
    print "Form name:", form.name
    print form
'''
br.select_form(nr=0)
br.set_all_readonly(False)

br["Judge"]=["CF",]
br["ProblemsCount"]=no
br["DifficultyType"]=["Exact",]
br["DifficultyValue"]=[difficulty,]
br["ExcludeSolved"]=["on"]

res = br.submit()

print 'problems added'

base_url = br.geturl()


register_url = "https://a2oj.com/register?ID="
register_url = register_url+str(id)





print 'now register'

chrome_path = '/usr/bin/google-chrome %s'
webbrowser.get(chrome_path).open(register_url)

'''
br.select_form(name="x")
br["q"] = "python"
res = br.submit()
content = res.read()
with open("mechanize_results.html", "w") as f:
    f.write(content)

webbrowser.open("mechanize_results.html")
'''