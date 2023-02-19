dicx = {"k1":
        [{"sk":"v1"},
         {"sk":"v2"}]
        }

#valoarea sub-key 1 sk1
print(dicx['k1'][0]['sk'])

print(f"type of dicx['k1] {type(dicx['k1'])}")

#iteram pe fiecare element din lista
for el in dicx['k1']:
    print(el['sk'])