import sys

if len(sys.argv)==2:
  script_name=sys.argv[0]
  salary=float(sys.argv[1])
else:
  script_name=sys.argv[0]
  salary=10000

Bonus=salary+(salary*0.10)
Finalsalary=Bonus+salary

print(f"Bonus: {Bonus}\nFinalsalary:{Finalsalary}")
