class Employee:
    def __init__(self, name, salary):
        # public member
        self.name = name
        # private member
        # not accessible outside of a class
        self._salary = salary

    def show(self):
        print("Name is", self.name, "and salary is", self._salary)

# Membuat objek dari kelas Employee
emp = Employee("Jessa", 4000)

# Memanggil metode show untuk menampilkan informasi
emp.show()

# Mengakses _salary dari luar kelas (meskipun seharusnya tidak disarankan)
print(emp._salary)
