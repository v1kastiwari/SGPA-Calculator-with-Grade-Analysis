import math

def get_grade_point(num):
    if (num%10) == 0 and num != 100:
        return math.ceil(num / 10) + 1
    return math.ceil(num / 10)


# mrk = []  #markslist
# grd = []  #gradelist

def sgpa(marks):
    grade_marks = [get_grade_point(i) for i in marks]
    crd = [3,3,3,3,3,1,1,2,1]
    for i in range(len(grade_marks)):
        grade_marks[i] = grade_marks[i]*crd[i]
        
    total_points_scored = sum(grade_marks)
    sgpa = total_points_scored/20
    return sgpa
#------------------------------------------------------------------

# mrk = eval(input('Enter marks -> '))
# sgpa(mrk)

# ele = 0
# for i in range(9):
#     ele = get_grade_point(mrk[i])
#     grd.append(ele)
# # print(grd)


