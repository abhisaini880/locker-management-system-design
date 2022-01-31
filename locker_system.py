from enum import Enum
import random, string


class Sizes(Enum):
    small = "small"
    medium = "medium"
    large = "large"


class Lockers:
    def __init__(self):
        self.lockers = {}

    def add_locker(self, locker_id, size):
        if locker_id not in self.lockers.keys():
            self.lockers[locker_id] = {
                "size": size,
                "empty": True,
                "code": None,
            }
        else:
            print(f"Locker with id: {locker_id} already exists !")

        return

    def find_empty_locker(self, locker_size):
        locker_found = False
        for size in Sizes:
            if locker_size == size.value:
                locker_found = True

            if locker_found:
                for locker_id, locker_prop in self.lockers.items():
                    if (
                        locker_prop["size"] == size.value
                        and locker_prop["empty"]
                    ):
                        return locker_id

        return None

    def set_locker_empty(self, locker_id, locker_code):
        if self.lockers[locker_id]["empty"]:
            print("Locker was already empty !")
            return
        else:
            if self.check_code(locker_id, locker_code):
                self.lockers[locker_id]["empty"] = True
                self.lockers[locker_id]["code"] = None
                return True
            else:
                print(f"Incorrect code for locker:{locker_id}")
            return

    def set_locker_full(self, locker_id):
        if self.lockers[locker_id]["empty"]:
            self.lockers[locker_id]["empty"] = False
            locker_code = self.generate_locker_code()
            self.lockers[locker_id]["code"] = locker_code
            return locker_code
        else:
            print("Locker was already full !")
            return

    def generate_locker_code(self):
        return "".join(
            [
                random.choice(string.ascii_letters + string.digits)
                for _ in range(4)
            ]
        )

    def check_code(self, locker_id, locker_code):
        return self.lockers[locker_id]["code"] == locker_code


class Packages:
    def __init__(self):
        self.packages = {}

    def add_package(self, pkg_id, size):
        if pkg_id not in self.packages.keys():
            self.packages[pkg_id] = {
                "size": size,
                "locker_id": None,
            }
        else:
            print(f"Package with id: {pkg_id} already exists !")

    def dispatch_package(self, pkg_id, locker_code=None, lockers=None):
        if pkg_id not in self.packages:
            print(f"No package with pkg_id: {pkg_id}")
        else:
            if lockers:
                locker_id = self.packages[pkg_id]["locker_id"]
                if lockers.set_locker_empty(locker_id, locker_code):
                    del self.packages[pkg_id]
                    print(f"Dispached package : {pkg_id}")
            else:
                del self.packages[pkg_id]
                print(f"Dispached package : {pkg_id}")
        return

    def store_package(self, pkg_id, locker_id, lockers):
        locker_code = lockers.set_locker_full(locker_id)
        if locker_code:
            self.packages[pkg_id]["locker_id"] = locker_id
        return locker_code

    def aling_pkg_with_lockers(self, pkg_id, lockers):
        pkg_size = self.packages[pkg_id]["size"]
        locker_id = lockers.find_empty_locker(pkg_size)
        if locker_id:
            return packages.store_package(pkg_id, locker_id, lockers)
        else:
            return packages.dispatch_package(pkg_id)


if __name__ == "__main__":
    # create lockers
    region_a = Lockers()

    region_a.add_locker("1001", "small")
    region_a.add_locker("1002", "medium")
    region_a.add_locker("1003", "small")
    region_a.add_locker("1004", "large")
    region_a.add_locker("1005", "medium")
    region_a.add_locker("1006", "small")
    region_a.add_locker("1007", "small")
    region_a.add_locker("1008", "medium")
    region_a.add_locker("1009", "large")
    region_a.add_locker("1010", "medium")

    # create packages
    packages = Packages()

    packages.add_package("501", "small")
    locker_code_501 = packages.aling_pkg_with_lockers("501", region_a)

    packages.add_package("502", "medium")
    locker_code_502 = packages.aling_pkg_with_lockers("502", region_a)

    packages.add_package("503", "small")
    locker_code_503 = packages.aling_pkg_with_lockers("503", region_a)

    packages.add_package("504", "medium")
    locker_code_504 = packages.aling_pkg_with_lockers("504", region_a)

    packages.add_package("505", "large")
    locker_code_505 = packages.aling_pkg_with_lockers("505", region_a)

    packages.add_package("506", "medium")
    locker_code_506 = packages.aling_pkg_with_lockers("506", region_a)

    packages.add_package("507", "small")
    locker_code_507 = packages.aling_pkg_with_lockers("507", region_a)

    packages.add_package("508", "large")
    locker_code_508 = packages.aling_pkg_with_lockers("508", region_a)

    packages.add_package("509", "small")
    locker_code_509 = packages.aling_pkg_with_lockers("509", region_a)

    packages.add_package("510", "small")
    locker_code_510 = packages.aling_pkg_with_lockers("510", region_a)

    packages.add_package("511", "small")
    locker_code_511 = packages.aling_pkg_with_lockers("511", region_a)

    # dispatch
    packages.dispatch_package("501", locker_code_501, region_a)

    # check lockers and packages
    print("\n| locker_id | locker_size | is_empty |")
    print("-----------------------------------------")
    for locker_id, locker in region_a.lockers.items():
        print(f"{locker_id} | {locker['size']} | {locker['empty']} |")

    print("\n| pkg_id | pkg_size | locker_id |")
    print("-----------------------------------------")
    for pkg_id, pkg in packages.packages.items():
        print(f"{pkg_id} | {pkg['size']} | {pkg['locker_id']} |")
