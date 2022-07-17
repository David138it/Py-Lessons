'''
получить новый список, содержащий: 
строки исходного списка с удаленным первым символом
длины строк исходного списка
только слова длиной не менее пяти символов (включительно)
'''
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [s[1:] for s in keywords]
print(new_keywords)
lengths = [len(i) for i in keywords]
print(lengths)
new_keywords = [s for s in keywords if len(s) >= 5]
print(new_keywords)
