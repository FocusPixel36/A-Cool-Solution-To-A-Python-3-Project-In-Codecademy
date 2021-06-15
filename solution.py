"""
A-Cool-Solution-To-A-Python-3-Project-In-Codecademy
I went a little creative on this and even added a little menu. I hope you guys like this.
"""

weight = 5.876
premium_shipping = "$125.00"

template = """~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Ground Shipping ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Weight of Package                             Price per Pound       Flat Charge   
2lb or less                                   $1.50                 $20.00
Over 2 lb but less than or equal to 6 lb      $3.00                 $20.00
Over 6 lb but less than or equal to 10 lb     $4.00                 $20.00
Over 10 lb                                    $4.75                 $20.00

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Drone Shipping ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Weight of Package                             Price per Pound       Flat Charge   
2lb or less                                   $4.50                 $0.00
Over 2 lb but less than or equal to 6 lb      $9.00                 $0.00
Over 6 lb but less than or equal to 10 lb     $12.00                 $0.00
Over 10 lb                                    $14.25                 $0.00
"""
print(template)
print("Don't forget! We have premium ground shipping for,",premium_shipping, "\n")

# Ground Shipping
if weight <= 2:
  total = weight * 1.50 + 20.00
  print("Your cost for ground shipping is,",total,"\n")
elif weight > 2 and weight <= 6:
  total = weight * 3.00 + 20.00
  print("Your cost for ground shipping is,",total,"\n")
elif weight > 6 and weight <= 10:
  total = weight * 4.00 + 20.00
  print("Your cost for ground shipping is,",total,"\n")
else:
  total = weight * 4.75 + 20.00
  print("Your cost for ground shipping is,",total,"\n")

# Drone Shipping
if weight <= 2:
  total = weight * 4.50
  print("Your cost for drone shipping is,",total,"\n")
elif weight > 2 and weight <= 6:
  total = weight * 9.00
  print("Your cost for drone shipping is,",total,"\n")
elif weight > 6 and weight <= 10:
  total = weight * 12.00
  print("Your cost for drone shipping is,",total,"\n")
else:
  total = weight * 14.25 + 20.00
  print("Your cost for drone shipping is,",total,"\n")
