final_score=int(input('请输入期末成绩：'))
regular_score=int(input('请输入平时成绩：'))
if final_score>90:
    if regular_score>90:
        grade="A+"
    else:
        grade="A"
elif final_score>80:
    if regular_score>85:
        grade="B+"
    else:
        grade="B"
elif final_score>70:
    if regular_score>80:
        grade="C+"
    else:
        grade="C"
else:
    grade='D'
print('成绩为:',grade)