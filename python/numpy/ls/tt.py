import datetime, re

DATE_PATTERN = re.compile('^\d+\-\d+\-\d+$')

def str_to_date(date):
    if isinstance(date, datetime.date):
        return date
    elif isinstance(date,str) and DATE_PATTERN.match(date):
        return datetime.date(*map(int, date.split('-')))
    raise TypeError


class Person(object):
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        
    @property
    def birthday(self):
        return self._birthday
    
    @birthday.setter
    def birthday(self, birthday):
        self._birthday = str_to_date(birthday)
    
    @property
    def age(self):
        return datetime.date.today() - self.birthday
    
    
    def __str__(self):
        return '%s,%s(%s)'%(self.name,self.birthday, self.age)
    

person = Person('Xiao Ming','1980-10-1')

print(person)
 
person.birthday = '1981-1-2'

print(person)

person.birthday = datetime.date(1979,12,12)

print(person)

# person.birthday = '123456' # raise TypeError

