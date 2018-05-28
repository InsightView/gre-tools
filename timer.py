from datetime import datetime
from collections import Counter


timeList = []


def readAnswer():
    answerList = []
    counter = 0
    print("Loading answers...")
    with open("./answer.txt", "r") as file:
        for line in file.readlines():
            line = line.strip()
            if len(line) > 1:
                if line.startswith("section"):
                    answer = []
                    counter = 0
                else:
                    ans = line.split(" ")[1]
                    answer += ans.split("/")
                    counter += 1
                if counter == 2:
                    answerList.append(answer)
    print("Loading section done.", len(answerList))
    return answerList


def quiz(quiz_counter):
    youAnswer = input("{}. ".format(quiz_counter))
    return youAnswer


def correction(results, answerList, timeList):
    correctNum = 0
    resultTableList = []
    answerMark = True
    num = len(results)
    section_num = num//10
    last_num = num*10 - section_num
    answers = []
    for items in answerList[:section_num]:
        answers += items
    answers += answerList[section_num][:last_num]
    print("Your answers | Correct answers | Time")
    for i in range(len(results)):
        item1 = results[i].upper()
        item2 = answers[i].upper()
        if results[i] == "":
            item1 = "null"
        if Counter(item1) == Counter(item2):
            correctNum += 1
            answerMark = True
        else:
            answerMark = False
        resultTable = str(i+1)+":\t"+item1+"\t"+item2+"\t" +str(answerMark)+"\t"+str(timeList[i])[:-7]
        # print(resultTable)
        resultTableList.append(resultTable)
    cor = round(correctNum/len(results), 2)
    totalTime = timeList[0]
    for t in timeList[1:-1]:
        totalTime += t
    for r in resultTableList:
        print(r)
    print("correction:{}/{}".format(correctNum, len(results)))
    print("rates:", cor)
    print("totalTime usage:", str(totalTime)[:-7])


def main():
    answering = True
    section = int(input("Input you section: "))
    answerList = readAnswer()[section-1:]
    results = []
    print("Start input your answer, input 0-9 to exits.")
    quiz_counter = 1
    while answering:
        start = datetime.now()
        results.append(quiz(quiz_counter))
        timeItem = datetime.now() - start
        timeList.append(timeItem)
        quiz_counter += 1
        if results[-1] in [str(x) for x in range(10)]:
            answering = False
            results = results[:-1]
    print("Your answers:", results, len(results))
    correction(results, answerList, timeList)
    # print("Your correction rates:", )


if __name__ == "__main__":
    main()
