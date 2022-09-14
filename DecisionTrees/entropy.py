import math

def getEntropy(data, classes):
    sum_ = 0.00
    totalDataset = len(data)
    counts = {class_:0 for class_ in classes}
    for i in data:
        counts[i] += 1
    prob = {class_:counts[class_]/totalDataset for class_ in counts.keys()}
    numClasses = len(counts.keys())
    sum_ = 0.00
    for class_ in prob:
        try:
            toAdd =  prob[class_]*math.log(prob[class_], numClasses)
            sum_ -= prob[class_]*math.log(prob[class_], numClasses)
        except:
            pass

    entr = 0-sum_
    return entr
