import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()

############
from faker import Faker
import random
from proudct.models import Category,Brand,Proudct,ProudctImge

def seek_brand(n):
    fake=Faker()
    imges=['1.png','2.jpg','3.jpg','4.jpg','5.jpg']
    
    for _ in range(n):
        name=fake.name()
        imge=f"Brand/{imges[random.randint(0,4)]}"
        Brand.objects.create(
            name=name,
            img=imge
        )

def seek_category(n):
    fake=Faker()
    imges=['1.jpg','2.jpg']
    
    for _ in range(n):
        name=fake.name()
        imge=f"Category/{imges[random.randint(0,1)]}"
        Category.objects.create(
            name=name,
            img=imge
        )

def seek_proudct(n):
   fake=Faker()
   imges=['1.jpg','2.jpg','3.jpg']
   flag_type=['new','sale','feature']

   for _ in range(n):
        name=fake.name()
        imge=f"proudct/{imges[random.randint(0,1)]}"
        sku=random.randint(1,10000)
        flag=flag_type[random.randint(0,2)]
        sub_title=fake.text(max_nb_chars=250)
        describtion=fake.text(max_nb_chars=7000)
        price=round(random.uniform(5,99.99),2)
        imge=f"proudct/{imges[random.randint(0,1)]}"
        
        brand=Brand.objects.get(id=random.randint(1,5))
        category=Category.objects.get(id=random.randint(1,10))
       
        
        Proudct.objects.create(
            name=name,
            img=imge,
            sku=sku,
            flag=flag,
            subtitle=sub_title,
            describtion=describtion,
            price=price,
            category=category,
            brand=brand,
            video="https://youtu.be/ad0HHLldK-c"
            
        )
      
def seek_proudct_img(n):
    fake=Faker()
    imges=['1.jpg','2.jpg','3.jpg']
    for _ in range(n):
        imge=f"ProudctImge/{imges[random.randint(0,2)]}"
        proudct=Proudct.objects.get(id=random.randint(1,1100))
        
        ProudctImge.objects.create(
            proudct=proudct,
            img=imge
            
        )
      
# seek_brand(5)
# seek_category(5)  
# seek_proudct(1000)
seek_proudct_img(1100)