#Note:set & frozenset allow only immutable elements
s={10,20,()}
print(s)

s={10,20,[]} #error
print(s)

