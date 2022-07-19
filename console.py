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



tag1 = Tag('Groceries', False)
tag_repository.save(tag1)

tag2 = Tag('Transport', True)
tag_repository.save(tag2)

tag3 = Tag('Eating Out', False)
tag_repository.save(tag3)

transaction1 = Transaction('1', 'Weekly shop', '1', 60.00, '2022-07-14')
transaction_repository.save(transaction1)
transaction2 = Transaction('2', 'Train tickets', '2', 20.00, '2022-07-05')
transaction_repository.save(transaction2)
transaction3 = Transaction('3', 'pint', '3', 3.5, '2022-07-02')
transaction_repository.save(transaction3)

budget1 = Budget(100.00)
budget_repository.save(budget1)

pdb.set_trace()