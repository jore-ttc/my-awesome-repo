# Example 1: Code that needs documentation
# Ask Copilot Chat: "Document this code thoroughly"
def process_data(data, threshold, max_iterations):
    results = []
    for i in range(max_iterations):
        filtered = [x for x in data if x > threshold]
        if not filtered:
            break
        normalized = [(x - min(filtered)) / (max(filtered) - min(filtered)) for x in filtered]
        results.extend(normalized)
        threshold *= 1.1
        mean_value = sum(normalized) / len(normalized) if normalized else 0
        results.append(mean_value)
        if len(results) > 1000:
            results = results[:1000]
            break
    results.sort()
    return results


# Example 2: Messy code that needs restructuring
# Ask Copilot Chat: "Restructure this code to make it more readable and maintainable"
def messyCalculation(x,y,z,flag=False):
    if flag==True:
        temp=x+y
        if temp>10:
         result=temp*z
        else:
            if z!=0:
             result=temp/z
            else:
                result=temp
    else:
        if x>y:temp=x-y
        else:temp=y-x
        if z>0:result=temp*z
        else:result=temp
    return result


# Example 3: Code that needs optimization
# Ask Copilot Chat: "Optimize this code for better performance"
def find_duplicates(items):
    duplicates = []
    for i in range(len(items)):
        for j in range(len(items)):
            if i != j and items[i] == items[j] and items[i] not in duplicates:
                duplicates.append(items[i])
    return duplicates


# Example 4: Generate code function
# Ask Copilot Inline chat: "Generate a function that ..."



# Example 5: 