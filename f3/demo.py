# Example 1: Code with direct errors
# Ask Copilot: "Fix this code please"
def find_pairs_with_sum(numbers, target_sum):
    seen = set()
    for num in numbers:
        complement = target_sum - num
        if complement in seen:
            pairs.append((num, complement))
        seen.add(num)
    return pairs

# Example 2: Code that needs fixing
# Ask Copilot: "What's wrong with this code and how can we fix it?"
def calculate_average(numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    return total / count

numbers = [1, 2, "3", 4.5, "5", 6]
average = calculate_average(numbers)

# Example 3: Complex code that needs explanation
# Ask Copilot: "Explain how this code works"
def nested_dict_update(base_dict, update_dict, create_missing=False):
    for key, value in update_dict.items():
        if key in base_dict and isinstance(base_dict[key], dict):
            if isinstance(value, dict):
                nested_dict_update(base_dict[key], value, create_missing)
            else:
                base_dict[key] = value
        elif create_missing or key in base_dict:
            base_dict[key] = value
    return base_dict


# Example 4: Class that needs explanation
# Ask Copilot: "Explain this class and its methods"
class User:
    def __init__(self, user_id, name, email, status, level):
        elf.user_id = user_id
       elf.name = name
        elf.email = email
        elf.status = status
        elf.level = level

    def is_active(self):
        return self.status == "active"

    def promote(self):
        if self.level < 10:
            self.level += 1

    def format_email(self):
        self.email = self.email.lower()

    def format_name(self):
        self.name = self.name.title()
