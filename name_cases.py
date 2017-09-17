#coding=utf-8

first_name = "Ethan"
last_name = "Liu"
full_name = first_name + " " + last_name

print ("Hello "+ full_name + ", would you like to learn some Python today?")

print (full_name.title())
print (full_name.upper())
print (full_name.lower())


name = "Albert Einstein"
print (name + ' once said, "A person who never made a mistake never tried anything new." ')

message = "A person who never made a mistake never tried anything new."
print (name + ' once said, ' + '"'+ message + '"')

great_man = "  Ethan  \n    Liu  \t"
print (great_man)
print (great_man.lstrip())
print (great_man.rstrip())
print (great_man.strip())
# 本例中，Ethan 和 Liu 虽然说用换行符分割开来显示，看起来是两行，但是还是被认作为一个字符串，lstrip, rstirp 和 strip 都只是对Ethan之前和Liu之后对空格进行调整
# 对于Ethan和Liu 之间的空格 视如不见