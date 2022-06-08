from ast import Lambda
t=input();
print(sorted(t,key=lambda t:(t.isdigit(),t.isdigit() and int(t)%2==0,t.isupper(),t.islower(),t)))
