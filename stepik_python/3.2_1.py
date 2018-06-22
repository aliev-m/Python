def f(d,key,value):
    if key in d:
        d[key]+=value
    elif 2*key in d:
        d[2*key] += value
    else:
        d[2*key] = value
