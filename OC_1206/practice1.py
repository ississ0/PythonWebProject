def calcMax(number_list):
    max = number_list[0]
    for number in number_list:
        if number > max:
            max = number
        return max
    # return  max(number_list)
def calcMin(number_list):
    return min(number_list)

def calcAvg(number_list):
    sum = 0
    for number in number_list:
        sum = sum + number
    개수 = len(number_list)
    return sum/개수
    # return sum(number_list) / len(number_list)

numbers = input("숫자들을 입력하세요: ")
splited_numbers = numbers.split()
number_list=[]
for number in numbers.split() :
    number_list.append(int(number))

# number_list = map(int, splited_numbers)
# a = map(int, a)

max_result = calcMax(number_list)
min_result = calcMin(number_list)
avg_result = calcAvg(number_list)

print("최댓값 : " + str(max_result))
print("최솟값 : " + str(min_result))
print("평균값 : " + str(avg_result))