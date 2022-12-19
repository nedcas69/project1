def get_arg(a,x,*args,**kwargs):
    print(a)
    print(x)
    print(args)
    print(kwargs)

get_arg(1,2,3,4,d= 23,b= 33,c= 43)