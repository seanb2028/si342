# Sean Beckford
def f1(wts, W):
    return [ f'(~a{i} => w{i} = 0)' for i in range(len(wts)) ]

def f2(wts, W):
    return [ f'(a{i} => w{i} = {x})' for i, x in enumerate(wts) ]

def f3(wts, W):
    return (
        'sum = ' + 
        ('plus(' * (len(wts) - 1)) + 
        "w0" + 
        (",w1" if len(wts) > 1 else "") +
        "".join([ f'),w{i}' for i in range(2, len(wts)) ]) +
        (")" if len(wts) > 1 else "")
    )

def f4(wts, W):
    return (
        ' & '.join(f1(wts, W)) +
        ' & ' +
        ' & '.join(f2(wts, W)) +
        ' & ' + 
        f3(wts, W) +
        f' & sum = {W}'
    )