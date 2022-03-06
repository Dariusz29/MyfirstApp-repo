import dictionaries as Dtp
import body as B
import random
levels = ['easy', 'medium', 'hard']
rep_ans = []
for i in range(1, 11):
    rep_ans.append(i)

print('Wall come to next review before next workout\t\n')
print(rep_ans)
print(levels)
print('\nPlease, Enter twice values:\n'
      '\t1. Reps in chest exercise in your last workout\n'
      '\t2. Difficulty level your last workout')

ans1 = input('1. ')
ans2 = input('2. ')

print(Dtp.up_body(ans1, ans2))

B.body("500x300")