import pdb
from models.merchant import Merchant
from models.tag import Tag
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository


merchant1 = Merchant('Sainsburys')
merchant_repository.save(merchant1)

merchant2 = Merchant('Tesco')
merchant_repository.save(merchant2)

merchant3 = Merchant('Coop')
merchant_repository.save(merchant3)



tag1 = Tag('Groceries')
tag_repository.save(tag1)

tag2 = Tag('Entertainment')
tag_repository.save(tag2)

tag3 = Tag('Transport')
tag_repository.save(tag3)