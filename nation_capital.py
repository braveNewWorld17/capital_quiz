import pymysql
'''
create table test.nation_capital (
    nation varchar(32),
    capital varchar(64)
);

insert into test.nation_capital value ("South Korea", "Seoul");
insert into test.nation_capital value ("Japan", "Tokyo");
insert into test.nation_capital value ("England", "London");

'''
def get_nation_capital():
    sc = { }
    conn = pymysql.connect(host='localhost',
                       user='root', password='as920558',
                       db='test', charset='utf8')
    curs = conn.cursor()
    sql = "select nation, capital from nation_capital"
    curs.execute(sql)
    rows = curs.fetchall()
    for row in rows:
        nation = row[0]
        capital = row[1]
        print ("capital = ", capital)
        sc[nation] = capital
    return sc

def get_and_check_answer(nation, real_answer):
    print ("real_answer = ", real_answer)
    user_answer = input("What is the capital of " + nation + "?")
    print ("user_answer = ", user_answer)

    if (real_answer.upper() == user_answer.upper()):
        return True
    else:
        return False

def display_point(point):
    print("You have " + str(point) + " point(s).")

print("Welcome to State Quiz!")
correct = 0

nation_capital = get_nation_capital()

for nation, capital in nation_capital.items():
    if get_and_check_answer(nation, capital):
        correct = correct + 1
        print("Good job!")
    else:
        print("Incorrect. The anwer is " + capital + ".")
    display_point(correct)
