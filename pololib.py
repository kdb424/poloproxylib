#!/usr/bin/env python
'''
    Polo proxy library
'''
import os
from time import time
import msgpack as mp
import nanomsg
from mkdir_p import mkdir_p

SOCKPROXY = None
POLOPROXY = None

def return_ticker():
    '''Returns ticker'''
    msg = mp.packb(['return_ticker', []])
    return send(msg)

def return_24h_volume():
    '''Returns 24hr volume'''
    msg = mp.packb(['return_24h_volume', []])
    return send(msg)

def return_currencies():
    '''Returns currences'''
    msg = mp.packb(['return_currencies', []])
    return send(msg)

def return_loan_orders():
    '''Returns loan orders'''
    msg = mp.packb(['return_loan_orders', []])
    return send(msg)


def orderbook(coin, altcoin, rows):
    '''Returns orderbook'''
    msg = mp.packb(['orderbook', [coin, altcoin, rows]])
    return send(msg)


def chart_data(coin, altcoin):
    '''Returns chart data'''
    msg = mp.packb(['chart_data', [coin, altcoin]])
    return send(msg)


def market_trade_hist(coin, altcoin, start=time()-60, end=time()):
    '''Returns market trade history'''
    msg = mp.packb(['market_trade_hist', [coin, altcoin, start, end]])
    return send(msg)


def return_trade_hist(coin, altcoin):
    '''Returns trade history'''
    msg = mp.packb(['return_trade_hist', [coin, altcoin]])
    return send(msg)


def return_balances():
    '''Returns balances'''
    msg = mp.packb(['return_balances', []])
    return send(msg)


def return_avalable_account_balances():
    '''Returns avalable account balances'''
    msg = mp.packb(['return_avalable_account_balances', []])
    return send(msg)


def return_margin_account_summary():
    '''Returns margin account summary'''
    msg = mp.packb(['return_margin_account_summary', []])
    return send(msg)


def return_margin_position():
    '''Returns margin position'''
    msg = mp.packb(['return_margin_position', []])
    return send(msg)


def return_complete_balances():
    '''Returns complete balances'''
    msg = mp.packb(['return_complete_balances', []])
    return send(msg)


def return_deposit_addresses():
    '''Returns deposit addresses'''
    msg = mp.packb(['return_deposit_addresses', []])
    return send(msg)


def open_orders(coin, altcoin):
    '''Returns open trades with currency pair'''
    msg = mp.packb(['open_orders', [coin, altcoin]])
    return send(msg)


def return_deposits_withdraws():
    '''Returns deposit/withdraw history'''
    msg = mp.packb(['return_deposits_withdraws', []])
    return send(msg)


def return_tradable_balances():
    '''Returns tradable balances'''
    msg = mp.packb(['return_tradable_balances', []])
    return send(msg)


def return_active_loans():
    '''Returns active loans'''
    msg = mp.packb(['return_active_loans', []])
    return send(msg)


def return_open_loan_offers():
    '''Returns open loan offers'''
    msg = mp.packb(['return_open_loan_offers', []])
    return send(msg)


def return_fee_info():
    '''Returns fee info'''
    msg = mp.packb(['return_fee_info', []])
    return send(msg)


def return_lending_hist(start=False, end=time(), limit=False):
    '''Returns lending history'''
    msg = mp.packb(['return_lending_hist', [start, end, limit]])
    return send(msg)


def return_order_trades(ordernumber):
    '''Return trade orders'''
    msg = mp.packb(['return_order_trades', [ordernumber]])
    return send(msg)

def create_loan_offer(coin, amt, rate, autoRenew=0, duration=2):
    '''Creates a loan offer'''
    msg = mp.packb(['create_loan_offer', [coin, amt, rate, autoRenew, duration]])
    return send(msg)


def cancel_loan_offer(ordernumber):
    '''Cancels loan offer'''
    msg = mp.packb(['cancel_loan_offer', [ordernumber]])
    return send(msg)


def toggle_auto_renew(ordernumber):
    '''Toggle autoRenew on a loan'''
    msg = mp.packb(['toggle_auto_renew', [ordernumber]])
    return send(msg)


def close_margin_position(coin, altcoin):
    '''Close a margin position'''
    msg = mp.packb(['close_margin_position', [coin, altcoin]])
    return send(msg)

def margin_buy(coin, altcoin, rate, amt, lendingRate=2):
    msg = mp.packb(['margin_buy', [coin, altcoin, rate, amt, lendingRate]])
    return send(msg)


def margin_sell(coin, altcoin, rate, amt, lendingRate=2):
    msg = mp.packb(['margin_sell', [coin, altcoin, rate, amt, lendingRate]])
    return send(msg)


def buy(coin, altcoin, rate, amt, fill_or_kill=False,
        immediate_or_cancel=False, post_only=False):
    '''Buy coins'''
    msg = mp.packb(['buy', [coin, altcoin, str(rate), str(amt),
        fill_or_kill=False, immediate_or_cancel=False, post_only=False]])
    return send(msg)


def sell(coin, altcoin, rate, amt):
    '''Sell coin'''
    msg = mp.packb(['sell', [coin, altcoin, str(rate), str(amt)]])
    return send(msg)


def cancel_order(ordernumber):
    '''Cancels order'''
    msg = mp.packb(['cancel_order', [ordernumber]])
    return send(msg)


def move_order(ordernumber, rate, amt):
    '''Moves order'''
    msg = mp.packb(['move_order', [ordernumber, rate, amt]])
    return send(msg)


def withdraw(coin, amt, address):
    '''Withdraws coin'''
    msg = mp.packb(['withdraw', [coin, amt, address]])
    return send(msg)


def transfer_balance(coin, amt, fromac, toac):
    '''Transfor balance'''
    msg = mp.packb(['transfer_balance', [coin, amt, fromac, toac]])
    return send(msg)


def send(msg):
    '''Sends packet to proxy'''
    SOCKPROXY.send(msg)
    try:
        return mp.unpackb(SOCKPROXY.recv(), use_list=True, encoding='UTF-8')
    except Exception as err:
        print('Server responded in an unexpected way.')


def connect(conf_name='poloniex'):
    '''Connect to poloproxy'''
    global SOCKPROXY
    global POLOPROXY
    # Connect to proxy
    SOCKPROXY = nanomsg.Socket(nanomsg.REQ)
    xdg_runtime_dir = os.environ.get('XDG_RUNTIME_DIR', '/tmp')
    our_runtime_dir = '{}/{}'.format(xdg_runtime_dir, 'krypto')
    mkdir_p(our_runtime_dir)
    POLOPROXY = SOCKPROXY.connect('ipc://{}/proxy'.format(our_runtime_dir))

if __name__ == '__main__':
    pass
