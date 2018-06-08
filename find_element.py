def half_array(arr, num, s) :

   l = int(len(arr))//2
   print("l=" + str(l) )

   if l > 0:
      if num > arr[l]:
         print (arr[l:])
         s = s + l
         print("s=" + str(s))
         half_array(arr[l:], num, s)
      elif num < arr[l]:
         print (arr[:l])
         half_array(arr[:l], num, s)
      elif num == arr[l]:
         s = s + l
         print("index = " + str(s))
   else :
      print(-1)

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15]

num = 9

print("num = " + str(num))

s = 0

f = half_array(arr, num, s)

print(arr[9])
