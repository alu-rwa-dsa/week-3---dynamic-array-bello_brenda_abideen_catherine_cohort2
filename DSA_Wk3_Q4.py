#Author : Brenda

a_list = dict()

class asso_list:
    def __init__(self):

        print("Welcome")

    def add(self, name, age, major, country):
        a_list["name"] = name
        a_list["age"] = age
        a_list["major"] = major
        a_list["country"] = country
        return a_list

    def a_remove(self, k):
        del a_list[k]
        return a_list

    def a_modify(self, name, major, country):
        a_list.update({"name":name})
        a_list.update({"major": major})
        a_list.update({"country":country})
        return a_list

    def a_lookup(self, i):
        for k in a_list.keys():
            if k == i:
                return "exists"
            else:
                return "not found"


if __name__ == "__main__":
    p = asso_list()

    print(p.add("Brenda", 34, "CS", "KE"))

    print(p.a_remove("age"))

    print(p.a_modify("Gilisho", "CS", "IBT"))

    print(p.a_lookup("name"))



