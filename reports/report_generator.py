from games.roulette import roulette

class report_generator():

    loggingEnabled = True;

    @staticmethod
    def log_game(roll_number):
        if report_generator.loggingEnabled == True:
            print("game: "+ str(roll_number))

    @staticmethod
    def log_result(result):
        print("")
        print("result: "+str(result))

    @staticmethod
    def log_player_account_change(account_delta, account):
        print("account changed of: " + str(account_delta))
        print("account new amount: " + str(account))

    @staticmethod
    def log_player_bet_change(new_bet):
        if report_generator.loggingEnabled == True:
            for bet_type, bet_dict in new_bet.iteritems():
                print("bet type: "+bet_type),
                for bet_target, bet_amount in bet_dict.iteritems():
                    if type(bet_target) == str:
                        print(bet_target+": "+str(bet_amount)),
                    elif type(bet_target) == int:
                        print(str(bet_target)+ ": "+str(bet_amount)),
                print("")
                print("bet multiplier: " + str(roulette.get_multiplier(bet_type)))


    def log_multiplier(multiplier):
        print("multiplier: "+multiplier)

    def log_profit(profit):
        print("profit: "+profit)



    def printReport(self):
        for key, value in self.rolls.iteritems():
            for key2, value2, in value:
                print("roll: "+key2, "result: "+value2["result"], "multiplier "+value2["multiplier"],
                      "profit: "+value2["profit"], "player_account: "+value2["player_account"])