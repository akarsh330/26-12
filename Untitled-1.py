q = ['1. what is the capital of india ?',
     '2.what is the national animal of india',
     '3.what is the national flower of india',
     '4.what is the national sports of india',
     '5.what is the currency of india']
ans = ['delhi','tiger','lotus','hockey','rupee']
for x in q:
    print(x)
    user_ans = input('enter answer:').lower
    if user_ans in ans:
        correct_ans =+ 1
        print('correct answer')
    else:
        wrong_ans =+1
        print('wrong ans')
print('percentage',((correct_answer/(correct_ans+wrong_ans) )*100))
