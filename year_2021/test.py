string = "a/b/c/d"
string = string.split("/")
print(string)
string = "/".join(string)
print(string)

string = "a nebo c"
print((".".join(string.split())).split("."))