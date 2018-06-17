def half_array(arr, num, s) :

   if num == arr[0]:

      print("element index is = 0")

   else:

      l = int(len(arr))//2

      if l > 0:
         if num > arr[l]:
            s = s + l
            half_array(arr[l:], num, s)

         elif num < arr[l]:
            half_array(arr[:l], num, s)

         elif num == arr[l]:
            s = s + l
            print("element index is = " + str(s))

      else :
         print("element isn't in this array -1")


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15]

half_array(arr, 11, 0)

half_array(arr, 3, 0)

half_array(arr, 0, 0)

half_array(arr, 15, 0)

half_array(arr, 10, 0)

half_array(arr, 4, 0)

half_array(arr, 5, 0)

half_array(arr, 2, 0)
