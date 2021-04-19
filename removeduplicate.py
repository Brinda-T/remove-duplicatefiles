#import usersdata
import csv
def project(data):
    fd=open(data,"r")
    data=fd.readlines()
    #data1=csv.reader(fd)
    print(len(data))
    for i in range(1,len(data)-1):
        x=(data[i].split(",")[4])
        phone=x.split()
        x1=("".join(phone))
        #print(x1)
        for j in range(i+1,len(data)-1):
            try:
                y=(data[j].split(",")[4])
            except IndexError:
                #print(j)
                continue  
            phonenum=y.split()
            y1=("".join(phonenum))
            
            if(int(x1)==int(y1)):
                yield j
                #print(j)
                
    fd.close
    return data


def remove_duplicate(dup_rows):
    data = "stu-data.csv"
    fd = open(data,"r")
    data = fd.readlines()
    print(dup_rows)
    
    A = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19}
    
    rows = A-dup_rows
    #print(rows)
    list_rows = list(rows)
    print(list_rows)
    print(len(list_rows))
    
     
    for i in range(0,len(list_rows)-1):
        j = list_rows[i]
        #print(j)
        print(data[j])
    
    fd.close
 
 
def main():
    data = "stu-data.csv"
    output=project(data) 
   
    
    set_data = set(output)
    print("Duplicate rows are : ",set_data)
    
    remove_duplicate(set_data) 
    return

if (__name__ == "__main__"):
    main()
