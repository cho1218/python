student1 = {"학번":1000, "이름":"홍길동", "학과":"열공학과"}
student2 = {"학번":1001, "이름":"강감찬", "학과":"체육학과"}
student3 = {"학번":1002, "이름":"이순신", "학과":"물리학과"}
student4 = {"학번":1003, "이름":"신사임당", "학과":"열공학과"}
student_list= []
student_list.append(student1)
student_list.append(student2)   
student_list.append(student3)
student_list.append(student4)

while True :
    print("┌-----------------------------------------------┐")
    print("│   학생관리 프로그램 V1.0 created by 조은주    │")
    print("├-----------------------------------------------┤")
    print("│ 1.전체출력  2.검색  3.신규학생추가    0.종료  │")
    print("└-----------------------------------------------┘")
    number = int(input("명령을 입력해주세요: "))

    if number==1:
        print("┌-----------------------------------------------┐")
        print("│ 전체 학생 목록                                │")
        print("└-----------------------------------------------┘")
        for data in student_list:
            print("학번: %d, 이름: %s, 학과: %s"%(data["학번"], data["이름"], data["학과"]))
        print("== 출력종료 =="); input("계속하려면 엔터키를 누르세요...")

    elif number==2:
        print("┌-----------------------------------------------┐")
        print("│ 검색 종류를 선택하세요.                       │")
        print("├-----------------------------------------------┤")
        print("│ 1.이름검색   2.학과검색                       │")
        print("└-----------------------------------------------┘")
        menu=int(input("검색 메뉴를 선택하세요: "))
        if menu==1:
            student_name_search=input("검색할 이름을 입력하세요. : ")
            for search1 in student_list:
                if search1["이름"]==student_name_search:
                    print("학번 : %d, 이름 : %s, 학과: %s"%(search1["학번"], search1["이름"], search1["학과"]))
            print("== 출력종료 =="); input("계속하려면 엔터키를 누르세요...")
        if menu==2:
            student_class_search=input("검색할 학과를 입력하세요. : ")
            for search2 in student_list:
                if search2["학과"]==student_class_search:
                    print("학번 : %d, 이름 : %s, 학과: %s"%(search2["학번"], search2["이름"], search2["학과"]))
            print("== 출력종료 =="); input("계속하려면 엔터키를 누르세요...")

    elif number==3:
        student_number_add=int(input("학번을 입력해주세요. :"))
        student_name_add=input("이름을 입력해주세요. :")
        student_class_add=input("학과를 입력해주세요. :")
        studentn={}
        studentn["학번"]=student_number_add
        studentn["이름"]=student_name_add
        studentn["학과"]=student_class_add
        student_list.append(studentn)
        print("신규학생이 추가되었습니다.")
        print("== 출력종료 =="); input("계속하려면 엔터키를 누르세요...")

    elif number==0:
        print("┌-----------------------------------------------┐")
        print("│ 프로그램을 종료합니다.                        │")
        print("└-----------------------------------------------┘")
        break
