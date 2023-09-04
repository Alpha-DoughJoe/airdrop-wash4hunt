# main.py

import logging
import random
from web3 import Web3

from config import CONFIG
from send import send_transaction
from bridge import bridge_transaction

logging.basicConfig(level=logging.INFO)

def main():
  w3 = Web3(Web3.HTTPProvider(CONFIG['INFURA_ID'])) 

  while True:
    try:
      sender, receiver = random_wallet_pair(CONFIG['WALLETS'])
      amount = random_amount()
      
      if rail == '1INCH':
        send_transaction(sender, receiver, amount)  
      elif rail == 'BRIDGE':
        bridge_transaction(sender, receiver, amount)
        
      time.sleep(random_time())
      
    except Exception as e:
      logging.error(e) 
      
if __name__ == "__main__":
  main()