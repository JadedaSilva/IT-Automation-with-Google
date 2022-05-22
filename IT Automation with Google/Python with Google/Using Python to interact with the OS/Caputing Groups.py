import re
result=re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
<re.Match object; span=(0, 13), match='Lovelace, Ada'>

print(result.groups())
('Lovelace', 'Ada')

>>> print(result[0])
Lovelace, Ada
>>> print(result[1])
Lovelace
>>> print(result[2])
Ada
>>>

import re
def rearrange_name(name):
  result = re.search(r"^(\w*), (\w*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)
