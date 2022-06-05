
import dddd
whether_exit = "y"



okay = {"01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr", "05": "May", "06": "Jun", "07": "Jul", "08": "Aug", "09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"}
def generate_reference(referencedic, input_date, file_openforwrite):
    okay = {"01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr", "05": "May", "06": "Jun", "07": "Jul", "08": "Aug", "09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"}
    yyyy = int(input_date[0:4])
    mmmm = okay[input_date[4:6]]
    dddd = int(input_date[6:8])
    referencelst = referencedic[yyyy][mmmm][dddd]
    reference = input_date
    if len(referencelst) <= 8:
        reference += "0"
        reference += str(1 + len(referencelst))
    else:
        reference += str(1 + len(referencelst))
    referencelst.append(reference)
    referencedic[yyyy][mmmm][dddd] = referencelst
    file_openforwrite.write("datedic=" + str(referencedic))
    return reference


def display_line(date, crlst, drlst, accountlst, explanation, referenceno):
    print("""----------
The following transaction will be recorded
|   DATE   |    DR     |    CR     | ACC |               COMMENT             | REFERENCE  |""")
    print("| " + date.ljust(8, " ") + " | " + drlst[0].ljust(9, " ") + " | " + crlst[0].ljust(9, " ") + " | " + accountlst[0] + " | " + explanation.ljust(34) + "| " + str(referenceno) + " |")
    for i in range(1, len(crlst)):
        print("|          | " + drlst[i].ljust(9, " ") + " | " + crlst[i].ljust(9, " ") + " | " + accountlst[i] + " | " + " " * 34 + "| " + str(referenceno) + " |")


riqi = str(input("What is the date today? "))
referdic = dddd.datedic
fifi = open("temp_dddd.py", "w")
rno = generate_reference(referdic, riqi, fifi)
fifi.close()

cr_list = []
dr_list = []
acc_list = []
crordr = ""
while crordr != "close":
    crordr = input("dr, cr or close? ")
    if crordr == "cr":
        amount = input("How much for cr? ")
        cr_list.append(str(amount))
        dr_list.append("")
        account = input("Which account? ")
        acc_list.append(str(account))
    elif crordr == "dr":
        amount = input("How much for dr? ")
        dr_list.append(str(amount))
        cr_list.append("")
        account = input("Which account? ")
        acc_list.append(str(account))

el = input("Comment: ")

display_line(riqi, cr_list, dr_list, acc_list, el, rno)

record = input("Press \"y\" to record the transaction: ")
if record == "y":
    fifr = open("temp_dddd.py", "r")
    qq = fifr.readline()
    fifw = open("dddd.py", "w")
    fifw.write(qq)
    fifw.close()
    fifr.close()
    data_write = open("data.csv", "a")
    data_write.write(riqi + "," + str(dr_list[0]) + "," + str(cr_list[0]) + "," + str(acc_list[0]) + "," + el + "," + rno + "\n")
    for i in range(1, len(cr_list)):
        data_write.write("," + str(dr_list[i]) + "," + str(cr_list[i]) + "," + str(acc_list[i]) + ",,\n")
    data_write.close()
    for i in range(len(cr_list)):
        if acc_list[i]=="101":
            fifl=open("101_Cash.csv","a")
            fifl.write(riqi + "," + str(dr_list[i]) + "," + str(cr_list[i]) + "," + str(acc_list[i]) + "," + el + "," + rno + ",\n")
            fifl.close()
        elif acc_list[i]=="102":
            fifl=open("102_RBC_Debit.csv","a")
            fifl.write(riqi + "," + str(dr_list[i]) + "," + str(cr_list[i]) + "," + str(acc_list[i]) + "," + el + "," + rno + ",\n")
            fifl.close()
        elif acc_list[i]=="103":
            fifl=open("103_TD_Debit.csv","a")
            fifl.write(riqi + "," + str(dr_list[i]) + "," + str(cr_list[i]) + "," + str(acc_list[i]) + "," + el + "," + rno + ",\n")
            fifl.close()
        elif acc_list[i]=="104":
            fifl=open("104_BOC_Debit.csv","a")
            fifl.write(riqi + "," + str(dr_list[i]) + "," + str(cr_list[i]) + "," + str(acc_list[i]) + "," + el + "," + rno + ",\n")
            fifl.close()
        elif acc_list[i]=="201":
            fifl=open("201_RBC_Credit.csv","a")
            fifl.write(riqi + "," + str(dr_list[i]) + "," + str(cr_list[i]) + "," + str(acc_list[i]) + "," + el + "," + rno + ",\n")
            fifl.close()
        elif acc_list[i]=="202":
            fifl=open("202_TD_Credit.csv","a")
            fifl.write(riqi + "," + str(dr_list[i]) + "," + str(cr_list[i]) + "," + str(acc_list[i]) + "," + el + "," + rno + ",\n")
            fifl.close()
        elif acc_list[i]=="203":
            fifl=open("203_BOC_Credit.csv","a")
            fifl.write(riqi + "," + str(dr_list[i]) + "," + str(cr_list[i]) + "," + str(acc_list[i]) + "," + el + "," + rno + ",\n")
            fifl.close()
        elif acc_list[i]=="301":
            fifl=open("301_Food_Exp.csv","a")
            fifl.write(riqi + "," + str(dr_list[i]) + "," + str(cr_list[i]) + "," + str(acc_list[i]) + "," + el + "," + rno + ",\n")
            fifl.close()
        elif acc_list[i]=="302":
            fifl=open("302_Living_Exp.csv","a")
            fifl.write(riqi + "," + str(dr_list[i]) + "," + str(cr_list[i]) + "," + str(acc_list[i]) + "," + el + "," + rno + ",\n")
            fifl.close()
        elif acc_list[i]=="303":
            fifl=open("303_Transport_Exp.csv","a")
            fifl.write(riqi + "," + str(dr_list[i]) + "," + str(cr_list[i]) + "," + str(acc_list[i]) + "," + el + "," + rno + ",\n")
            fifl.close()
        elif acc_list[i]=="304":
            fifl=open("304_Study_Exp.csv","a")
            fifl.write(riqi + "," + str(dr_list[i]) + "," + str(cr_list[i]) + "," + str(acc_list[i]) + "," + el + "," + rno + ",\n")
            fifl.close()
        elif acc_list[i]=="310":
            fifl=open("310_Inventory.csv","a")
            fifl.write(riqi + "," + str(dr_list[i]) + "," + str(cr_list[i]) + "," + str(acc_list[i]) + "," + el + "," + rno + ",\n")
            fifl.close()
        elif acc_list[i]=="311":
            fifl=open("311_Other_Exp.csv","a")
            fifl.write(riqi + "," + str(dr_list[i]) + "," + str(cr_list[i]) + "," + str(acc_list[i]) + "," + el + "," + rno + ",\n")
            fifl.close()
        elif acc_list[i]=="401":
            fifl=open("401_Prepaid_Acc.csv","a")
            fifl.write(riqi + "," + str(dr_list[i]) + "," + str(cr_list[i]) + "," + str(acc_list[i]) + "," + el + "," + rno + ",\n")
            fifl.close()
        elif acc_list[i]=="501":
            fifl=open("501_Scholarship.csv","a")
            fifl.write(riqi + "," + str(dr_list[i]) + "," + str(cr_list[i]) + "," + str(acc_list[i]) + "," + el + "," + rno + ",\n")
            fifl.close()
        elif acc_list[i]=="502":
            fifl=open("502_Revenue.csv","a")
            fifl.write(riqi + "," + str(dr_list[i]) + "," + str(cr_list[i]) + "," + str(acc_list[i]) + "," + el + "," + rno + ",\n")
            fifl.close()
        elif acc_list[i]=="999":
            fifl=open("999_Balance.csv","a")
            fifl.write(riqi + "," + str(dr_list[i]) + "," + str(cr_list[i]) + "," + str(acc_list[i]) + "," + el + "," + rno + ",\n")
            fifl.close()
        elif acc_list[i]=="666":
            fifl=open("666_HST.csv","a")
            fifl.write(riqi + "," + str(dr_list[i]) + "," + str(cr_list[i]) + "," + str(acc_list[i]) + "," + el + "," + rno + ",\n")
            fifl.close()


