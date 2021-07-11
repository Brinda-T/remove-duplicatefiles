import csv
import json

def get_data_by_csv_file(filename):
    data_list = []
    fd = open(filename, 'rt')
    fdata = csv.reader(fd)

    for row in fdata:
        data_list.append(row)

    fd.close()
    return(data_list)

def delete_duplicates(data_list):
    n = len(data_list)- 1
    for i in range(1, n):
        j = i + 1
        for j in range(i+1, n):
            try:
                src1 = "".join(data_list[i][4].split())
                src2 = "".join(data_list[i][5].split())
                dst1 = "".join(data_list[j][4].split())
                dst2 = "".join(data_list[j][5].split())
            except IndexError:
                continue
            if(src1 == dst1 or src1 == dst2):
                del(data_list[j])
                n = n - 1
                print(n)
    print(len(data_list))
    return(data_list)
    

def main():
    filename = "stu-data.csv"
    data_list = get_data_by_csv_file(filename)
    print(data_list)
    print("")
    dlist = delete_duplicates(data_list)
    print(dlist)
    
    gdata = []
    for row in dlist:
        
        userdata = ('{}, {}'.format(row[4], row[5]))
        print(userdata)
        gdata.append(userdata)
    
    print(gdata)
    with open("gusers-data.csv", "w") as fd:
        gd = csv.writer(fd, delimiter = '\t')
        for r in gdata:

            gd.writerow(r)

    return
if (__name__ == "__main__"):
    main()
