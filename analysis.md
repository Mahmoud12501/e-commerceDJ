profile
    -user[one to one]->[username ,f_name,l_name,email]
    -email
    -img
    -Contact Numbers
    -Delivery Address 

Contact Numbers:
    -user (forgin key)
    -number
    -type_number

Delivery Address:
    -user (forgin key)
    -country
    -city
    -region
    -street
    -note


order:
 -code
 -user
 -status[recieved,processed,shipped,delivered]
 -Order Time
 -Delivery Time

order_detail:
    -order
    -proudct
    -quantiy
    -total

    