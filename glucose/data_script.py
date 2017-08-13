import datetime

# week 32 | Aug 7 - Aug 13
template_head = """\

--------

#### week {WEEK} | {START_DAY} - {END_DAY}

<details>
"""

# ##### 2017, Aug 7 --- Mon
template_body = """\


##### {YYYY}, {MM_D_NAME}

|Time | Glucose | Units | Comment|
|-------|------|--------|---------------------------------|"""

template_day_graph_lines = """\
|       |      |        |                                 |"""

template_tail = """\

</details>"""


def generate_string_days_from_WWYYYY(week_nr, year):
    d = str(year) + "-W" + str(week_nr)
    days = []
    day1 = datetime.datetime.strptime(d + "-1", "%Y-W%W-%w")
    for i in range(0, 7):
        days.append(day1 + datetime.timedelta(days=i))

    return days


def compose_chart(week_nr, year, num_chart_entries=5):

    if not week_nr and year:
        print('week and year number are necessary')
        return

    days = generate_string_days_from_WWYYYY(week_nr, year)
    # "%b-%a---%d"  ==== Jul-Mon---31
    sd, ed = days[0], days[-1]
    sd = sd.date().strftime("%b %d")
    ed = ed.date().strftime("%b %d")
    print(template_head.format(WEEK=week_nr, START_DAY=sd, END_DAY=ed))

    for day in days:
        tstr = template_body.format(YYYY=str(year) , MM_D_NAME=day.date().strftime("%b %d --- %a"))
        print(tstr)
        for i in range(num_chart_entries):
            print(template_day_graph_lines)

    print(template_tail)



compose_chart(week_nr=31, year=2017, num_chart_entries=5)