import json

print("Interface status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

with open('work.json') as san:
    date = json.load(san)

request = date["imdata"][0]["l1PhysIf"]["attributes"]["dn"]
speed = date["imdata"][0]["l1PhysIf"]["attributes"]["fecMode"]
mtu = date["imdata"][0]["l1PhysIf"]["attributes"]["mtu"]
print(request, "     ", speed, " ", mtu)
print(request, "     ", speed, " ", mtu)
print(request, "     ", speed, " ", mtu)