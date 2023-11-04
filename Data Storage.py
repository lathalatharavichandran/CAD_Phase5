import pickle
f=open("data.txt","wb")
dct={"name":"Ravi", "age":23, "Gender":"M","marks":75}
pickle.dump(dct,f)
f.close()

#to read
import pickle
f=open("data.txt","rb")
d=pickle.load(f)
print (d)
f.close()