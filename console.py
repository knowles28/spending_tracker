import pdb
from models.budget import Budget
from models.merchant import Merchant
from models.tag import Tag
from models.budget import Budget
from models.transaction import Transaction
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository
import repositories.budget_repository as budget_repository




merchant1 = Merchant('Sainsburys', False)
merchant_repository.save(merchant1)

merchant2 = Merchant('LNER', False)
merchant_repository.save(merchant2)

merchant3 = Merchant('The Chanter', False)
merchant_repository.save(merchant3)

merchant4 = Merchant('ScotRail', False)
merchant_repository.save(merchant4)

merchant5 = Merchant('Lothian Buses', False)
merchant_repository.save(merchant5)

merchant6 = Merchant('Wings', False)
merchant_repository.save(merchant6)

merchant7 = Merchant('Aldi', False)
merchant_repository.save(merchant7)



tag1 = Tag('Groceries', False)
tag_repository.save(tag1)

tag2 = Tag('Transport', True)
tag_repository.save(tag2)

tag3 = Tag('Eating Out', False)
tag_repository.save(tag3)

transaction1 = Transaction('1', 'quick shop', '1', 18.78, '2022-06-28')
transaction_repository.save(transaction1)
transaction2 = Transaction('2', 'London tickets', '2', 40.00, '2022-06-05')
transaction_repository.save(transaction2)
transaction3 = Transaction('3', 'pint', '3', 3.5, '2022-07-01')
transaction_repository.save(transaction3)

transaction4 = Transaction('4', 'Glasgow train', '2', 20.00, '2022-07-14')
transaction_repository.save(transaction4)
transaction5 = Transaction('5', 'Bus rides', '2', 4.50, '2022-04-15')
transaction_repository.save(transaction5)
transaction6 = Transaction('6', 'spicy dinner', '3', 10.25, '2022-05-30')
transaction_repository.save(transaction6)
transaction7 = Transaction('7', 'Weekly shop', '1', 52.00, '2022-07-10')
transaction_repository.save(transaction7)
transaction8 = Transaction('3', 'happy hour drinks', '3', 14.00, '2022-06-02')
transaction_repository.save(transaction8)



budget1 = Budget(100.00)
budget_repository.save(budget1)

pdb.set_trace()