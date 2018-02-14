class Atm:

    def __init__(self , balance , bank_name):
        self.balance = balance
        self.bank_name = bank_name

    def withdraw(self, request):

        result = self.balance

        print "Welcome to " + self.bank_name
        print "Current balance = " + str(self.balance)
        print "======================================="

        if request > self.balance:
            print "SORRY!! Can't give you all this money ! ! ! "
            print "======================================="
            result = self.balance

        elif request <= 0:
            print "SORRY !!! Please request more than 0"
            print "======================================="
            result = self.balance

        else:
            self.balance = self.balance-request

            while request > 0:

                if request >= 100:
                    request -= 100
                    print "give 100"

                elif request >= 50:
                    request -= 50
                    print "give 50"

                elif request >= 10:
                    request -= 10
                    print "give 10"

                elif request >= 5:
                    request -= 5
                    print "give 5"

                elif request < 5:
                    print "give " + str(request)
                    request = 0
            print "======================================="
            return self.balance

        return result

