def answer(xs):
    if len(xs) >= 2:
        mostPos = 0
        mostNeg = 0
        nextNeg = 1
        for i in xrange(len(xs) - 1, -1, -1):
            if xs[i] > xs[mostPos]:
                mostPos = i
            elif xs[i] < xs[mostNeg]:
                mostNeg = i
            elif xs[i] < xs[nextNeg]:
                nextNeg = i
        if xs[mostPos] > 0:
            newList = xs[:]
            del newList[mostPos]
            result = answer(newList)
            if int(result) <= 0:
                result = "1"
            return stringMultiply([str(xs[mostPos]), result])
        elif xs[mostNeg] < 0 and xs[nextNeg] < 0 and mostNeg != nextNeg:
            newList = [element for i, element in enumerate(xs) if i not in [mostNeg, nextNeg]]
            result = answer(newList)
            if int(result) <= 0:
                result = "1"
            return stringMultiply([str(xs[mostNeg]), str(xs[nextNeg]), result])
        else:
            return "0"
    return str(xs[0])

#assumes xm is string list of length 2 or greater
def stringMultiply(xm):
    addNums = []
    count = 0
    isNegative = (xm[0] == "-" and xm[1] != "-") or (xm[1] == "-" and xm[0] != "-")
    first = xm[0][::-1].replace("-", "")
    second = xm[1][::-1].replace("-", "")
    for i in first:
        addNums.append("0" * count)
        remNum = 0
        for j in second:
            toAdd = int(i) * int(j) + remNum
            if toAdd >= 10:
                addNums[count] += str(toAdd % 10)
                remNum = toAdd // 10
            else:
                addNums[count] += str(toAdd)
                remNum = 0
        if remNum != 0:
            addNums[count] += str(remNum)[::-1]
        addNums[count] = addNums[count][::-1]
        count += 1
    result = stringAdd(addNums)
    toReturn = ""
    if isNegative:
        toReturn = "-"
    if len(xm) > 2:
        toReturn += stringMultiply([result] + xm[2:])
    else:
        toReturn += result  
    return toReturn

#assumes only positive numbers
def stringAdd(xa):
    result = ""
    shouldContinue = True
    i = 0
    rem = 0
    while shouldContinue:
        shouldContinue = False
        total = rem
        for num in xa:
            if len(num) > i:
                total += int(num[len(num) - 1 - i])
                shouldContinue = True
        if shouldContinue:
            result += str(total % 10)
            if total >= 10:
                rem = total // 10
            else:
                rem = 0
            i += 1
    if rem != 0:
        result += str(rem)[::-1]
    return result[::-1]

# print answer([1000] * 50)
# print answer([2,-3,1,0,-5])
# print answer([-2, -3, 4, -5])