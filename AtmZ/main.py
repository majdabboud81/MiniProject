class Atm:

    def __init__(self , balance , bank_name):
        self.balance = balance
        self.bank_name = bank_name

    def withdraw(self, request):

        result = self.balance
        string = "======================================="
        print ("Welcome to " + self.bank_name)
        print ("Current balance = " + str(self.balance))
        print (string)

        if request > self.balance:
            print ("SORRY!! Can't give you all this money ! ! ! ")
            print (string)
            result = self.balance

        elif request <= 0:
            print ("SORRY !!! Please request more than 0")
            print (string)
            result = self.balance

        else:
            self.balance = self.balance-request

            while request > 0:

                if request >= 100:
                    request -= 100
                    print ("give 100")

                elif request >= 50:
                    request -= 50
                    print ("give 50")

                elif request >= 10:
                    request -= 10
                    print ("give 10")

                elif request >= 5:
                    request -= 5
                    print ("give 5")

                elif request < 5:
                    print ("give " + str(request))
                    request = 0
            print (string)
            return self.balance

        return result

