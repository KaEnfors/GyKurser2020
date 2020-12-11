"""
Exempel:

NEXT
7,4,6,3 (1/4)
-> 7 första platsen
-> 7 > 4 byt plats
-> 4,7,6,3
-> 7 andra platsen
-> 7 > 6 byt plats
-> 4,6,7,3
-> tredje platsen, 7
-> 7 > 3 byt plats
-> 4,6,3,7
NEXT
4,6,3,(7) 2/4
-> 4 första platsen
-> 4 > 6 false... inte byta plats
-> 4,6,3,7
-> 6 andra platsen
-> 6 > 3 byt plats
-> 4,3,6,7
-> 6 tredje platsen
-> 6 > 7 false, byt inte
-> 4,3,6,7
NEXT
4,3,(6),(7) 3/4
-> 4 första plats
-> 4 > 3 byt
-> 3,4,6,7
-> 4 andra plats
-> ... byt inte
-> byt inte... 
-> byt inte...

len(lista) -> ger oss längden på listan

byta på två värden:
val1 = 55
val2 = 77
val1, val2 = 55, 77

val1, val2 = val2, val1

tmp = val1
val1 = val2 
val2 = tmp


"""


def bubble_sort(lis):
    sort = lis.copy()

    for i in range(len(sort)):
        # det här händer X antal gånger, en för varje plats i listan...
        
        for j in range(len(sort)-1):
            #
#            print(sort[j], "byt eller inte?")
            print(sort[j], ">", sort[j+1], "?")

            if (sort[j] > sort[j+1]):
                tmp = sort[j]
                sort[j] = sort[j+1]
                sort[j+1] = tmp

    return sort




mylist = [2,6,5,8,9,6,7,5,4,3,6,7,8,6,5,4,3,8,4,1]
#mylist = [2,6,5,8]
mysortedlist = bubble_sort(mylist) # en rads kommentar

print("List   :", mylist)
print("Sorted :", mysortedlist)



