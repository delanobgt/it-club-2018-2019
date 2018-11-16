def circularArrayRotation(a, k, queries):
    length = len(a)
    answers = []
    for q in queries:
        answers.append( a[(q % length - k % length + length) % length] )
    return answers