import random
Result = [0, 0, 0]
Result[0] = random.randint(1, 9)
Result[1] = random.randint(0, 9);
while Result[0] == Result[1]:
    Result[1] = random.randint(0, 9);
while Result[0] == Result[1] or Result[1] == Result[2]:
    Result[2] = random.randint(0, 9);

print(Result)
count = 0

while True:
    count += 1
    strike = 0
    ball = 0
    Answer = input('3자리 숫자를 입력하세요 => ')
    if Answer == "-1":
        break
    if Answer[0] == str(Result[0]) and Answer[1] == str(Result[1]) and Answer[2] == str(Result[2]):
        print(str(count) + '번째로 맞춤')
        break

    for idx1 in range(0, 3):
        for idx2 in range(0, 3):
            if Answer[idx2] == str(Result[idx1]) and idx1 == idx2:
                strike += 1
            elif str(Result[idx1]) == Answer[idx2] and idx1 != idx2:
                ball += 1

    print(str(strike) + '스트라이크, ' + str(ball) + '볼')
