class Employee():
    def __init__(self, id: int, name: str) -> None:
        self.name = name
        self.id = id
        
    def __str__(self) -> str:
        return f"{self.id} - {self.name}"
    
class HashTable():
    def __init__(self) -> None:
        self.storage = dict()
    
    def hash(self, key: int) -> int:
        return key % 10
    
    def push(self, value: Employee) -> None:
        index = self.hash(value.id)
        
        if index in self.storage:
            self.storage[index].append(value)
        else:
            self.storage[index] = [value]
            
    def search(self, key: int) -> Employee or int:
        index = self.hash(key)
        
        if index in self.storage:
            for employee in self.storage[index]:
                if employee.id == key:
                    return employee
                else:
                    return -1
        
if __name__ == '__main__':
    storage = dict()
    hash_table = HashTable()
    
    for i in range(10):
        hash_table.push(Employee(i, f"Funcionario{i}"))
        
    print(hash_table.search(15))