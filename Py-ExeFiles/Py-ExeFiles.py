def sum(a,b):
    result=a+b
    with open("Py-ExeFiles_Result.txt","w",encoding="utf-8") as file:
        file.write(str(result))
def main():
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    sum(a,b)
if __name__== '__main__':
    main()
