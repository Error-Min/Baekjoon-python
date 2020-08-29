a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

ad = a + d
ae = a + e
bd = b + d
be = b + e
cd = c + d
ce = c + e

if ad > bd and bd < cd:
    bd = bd - 50
elif ad < bd and ad < cd:
    ad = ad - 50
elif ad > cd and cd < bd:
    cd = cd - 50

if ae > be and be < ce:
    be = be - 50
elif ae < be and ae < ce:
    ae = ae - 50
elif ae > ce and ce < be:
    ce = ce - 50

if ad < ae and ad < be and ad < ce:
    print(ad)
elif ae < ad and ae < be and ae < ce:
    print(ae)
elif bd < be and bd < ae and bd < ce:
    print(bd)
elif be < bd and be < ae and be < ce:
    print(be)
elif cd < ce and cd < be and cd < ae:
    print(cd)
elif ce < cd and ce < be and ce < ae:
    print(ce)






