QaysiYol = input("Qaysi yo'lni tanlaysiz?(Ko'k , Qizil , Yashil) : ")

if QaysiYol == "Ko'k" or QaysiYol == "Qizil" or QaysiYol == "Yashil":
    if QaysiYol == "Ko'k":
        print("Siz Ko'k yo'lni tanladingiz")
        yonalish1 = input("Qaysi yo'nalishni tanlaysiz ?")
        if yonalish1 == "Tepaga":
            print("To'g'ri")

            yonalish2 = input("Qaysi yo'nalishni tanlaysiz ?")
            if yonalish2 == "O'nga":
                print("To'g'ri")

                yonalish3 = input("Qaysi yo'nalishni tanlaysiz ?")
                if yonalish3 == "Pastga":
                    print("To'g'ri")

                    yonalish4 = input("Qaysi yo'nalishni tanlaysiz ?")
                    if yonalish4 == "O'nga":
                        print("To'g'ri")

                        print("^^^Yutdingiz^^^")
                    else:
                        print("Yutqazdingiz")
                else:
                    print("Yutqazdingiz")
            else:
                print("Yutqazdingiz")
        else:
            print("Yutqazdingiz")




    elif QaysiYol == "Qizil":
        print("Siz Qizil yo'lni tanladingiz")
        yonalish1 = input("Qaysi yo'nalishni tanlaysiz ?")
        if yonalish1 == "Tepaga":
            print("Tepaga")

            yonalish2 = input("Qaysi yo'nalishni tanlaysiz ?")
            if yonalish2 == "Chapga":
                print("To'g'ri")

                yonalish3 = input("Qaysi yo'nalishni tanlaysiz ?")
                if yonalish3 == "Tepaga":
                    print("To'g'ri")

                    yonalish4 = input("Qaysi yo'nalishni tanlaysiz ?")
                    if yonalish4 == "O'nga":
                        print("To'g'ri")

                        yonalish5 = input("Qaysi yo'nalishni tanlaysiz ?")
                        if yonalish5 == "Tepaga":
                            print("To'g'ri")
                            print("^^^Yutdingiz^^^")
                        else:
                            print("Yutqazdingiz")
                    else:
                        print("Yutqazdingiz")
                else:
                    print("Yutqazdingiz")
            else:
                print("Yutqazdingiz")
        else:
            print("Yutqazdingiz")


    else:
        print("Siz Yashil yo'lni tanladingiz")
        yonalish1 = input("Qaysi yo'nalishni tanlaysiz ?")
        if yonalish1 == "Tepaga":
            print("Tepaga")

            yonalish2 = input("Qaysi yo'nalishni tanlaysiz ?")
            if yonalish2 == "O'nga":
                print("To'g'ri")

                yonalish3 = input("Qaysi yo'nalishni tanlaysiz ?")
                if yonalish3 == "Tepaga":
                    print("To'g'ri")

                    yonalish4 = input("Qaysi yo'nalishni tanlaysiz ?")
                    if yonalish4 == "O'nga":
                        print("Chapga")

                        yonalish5 = input("Qaysi yo'nalishni tanlaysiz ?")
                        if yonalish5 == "Tepaga":
                            print("To'g'ri")

                            yonalish6 = input("Qaysi yo'nalishni tanlaysiz ?")
                            if yonalish6 == "Chapga":
                                print("To'g'ri")
                                print("^^^Yutdingiz^^^")
                            else:
                                print("Yutqazdingiz")
                        else:
                            print("Yutqazdingiz")
                    else:
                        print("Yutqazdingiz")
                else:
                    print("Yutqazdingiz")
            else:
                print("Yutqazdingiz")
        else:
            print("Yutqazdingiz")
else:
    print("Undefined")