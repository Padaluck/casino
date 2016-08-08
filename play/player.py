__author__ = 'wikia'
import copy
from reports.report_generator import report_generator

class player(object):
    """
    Both play and croupier has a state
    play: betting, no more bets
    """

    # bet = {numbers: {x: amount, b: amount, c: amount}, colour: {red: amount, blue: amount} }
    name = ''
    _account = 0
    _bet = {}
    strategy = None

    def __init__(self, player_name, player_account, player_strategy):
        self.reset()
        self.name = player_name
        self._account = player_account
        self.strategy = player_strategy
        self._bet = copy.deepcopy(player_strategy.get_first_bet(self))
        self.account -= self.strategy.get_bet_sum()

    def get_account(self):
        return self._account

    def set_account(self, value):
        self._account = value
        report_generator.log_player_account_change(value, self.account)

    def get_bet(self):
        return self._bet

    def set_bet(self, value):
        self._bet = value
        report_generator.log_player_bet_change(value)

    account = property(get_account, set_account)
    bet = property(get_bet, set_bet)


    def reset(self):
        self.name = ''
        self._account = 0
        self.strategy = None

    def get_next_bet(self):
        self.bet = copy.deepcopy(self.strategy.get_bet(self))
        # update account
        self.account -= self.strategy.get_bet_sum()

    def set_payment(self, payment):
        self.account += payment

    def get_name(self):
        return self.name

    def get_bet(self):
        return self.bet