from selenium import webdriver

browser = webdriver.Firefox()

browser.get("https://fantasy.premierleague.com/leagues/1528826/standings/c")

table_loc = '//table[@class="Table-ziussd-1 fHBHIK"]/tbody/tr[@class="StandingsRow-fwk48s-0"]/td/a[@class="Link-a4a9pd-1 cA-DQBw"]/strong'

players = browser.find_elements_by_xpath(table_loc)

emp_list = []

for player in players:
    emp_list.append(player.text)


pts_loc = '//table[@class="Table-ziussd-1 fHBHIK"]/tbody/tr[@class="StandingsRow-fwk48s-0"]/td'

elems = browser.find_elements_by_xpath(pts_loc)


emp_elems = []

for elem in elems:
    emp_elems.append(elem.text)


pts = []
c=2
while c<45:
    pts.append(int(emp_elems[c]))
    c=c+4

# create a dictionary to append the elements of the lists 'emp_list' and 'pts'

player_info = {}

for k in range(0,11):
    player_info[emp_list[k]]=pts[k]
	
# find the winner and print winner's name and the gw points

w = 0
h = pts[0]
while w<11:
    if pts[w]>h:
        h = pts[w]
    w+=1

print("Players", end='   ')
print("Points")
print()

for key, value in player_info.items():
	print(key, end=' ')
	print(":", value)

print()
print()
for key, value in player_info.items():
    if value == h:
        print("GW Winner: ", key)




