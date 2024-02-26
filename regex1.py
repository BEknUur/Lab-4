#1Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re

txt = "abb ab a"

x = re.findall("a{1}d*", txt)
#2Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
txt="ddcmscmkscabbb"
y = re.findall("a.*bb+|abbb+", txt)

#3Write a Python program to find sequences of lowercase letters joined with a underscore.
txt="amakxmkcskcscms"
v=re.findall("[a-z]_+[a-z]+", txt)

#4Write a Python program to find the sequences of one upper case letter followed by lower case letters.
txt="AABBIECNdvndvndv"
c=re.findall("[A-Z]_+[a-z]+",txt)

#5Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
txt="sozaaacjncvbbbbddvabbbd"
d=re.findall("a+.b",txt)

#6Write a Python program to replace all occurrences of space, comma, or dot with a colon.
txt="ffl,vvvv..//.,,.2.z:../,,,"
f=re.sub("[.,]",':',txt)

#7Write a python program to convert snake case string to camel case string.
txt="vddl,vdlv,dv"
g=re.sub(r"_",'',txt)
#8Write a Python program to split a string at uppercase letters.
txt="ADNDCJNcncdjcndcj"
g=re.findall("[A-Z][^A-Z]*",txt)

#9
#Write a Python program to insert spaces between words starting with capital letters.
string="Kbtuisthebest"
h=re.findall("[A-Z][a-z]*",string)

#10Write a Python program to convert a given camel case string to snake case.
string="NCSCNDVN___ddnvJDVDndvdvn"
q=re.sub("[A-Z]",'_',string)

