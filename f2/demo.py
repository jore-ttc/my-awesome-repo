# Example 1: Code that needs documentation
# Ask Copilot Chat: "Document this code thoroughly"
def analyze_time_series(data, window_size, threshold):
    results = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i + window_size]
        avg = sum(window) / window_size
        variance = sum((x - avg) ** 2 for x in window) / window_size
        if variance > threshold:
            peaks = [x for x in window if x > avg + (variance ** 0.5)]
            if peaks:
                results.extend(peaks)
    if results:
        results.sort(reverse=True)
        return results[:100]
    return []


# Example 2: Messy code that needs restructuring
# Ask Copilot Chat: "Restructure this code to make it more readable and maintainable"
def processImage(img,brightness,contrast,apply_filters=False):
    if apply_filters==True:
        temp=img.copy()
        if brightness>0:
         result=temp+brightness
        else:
            if contrast!=0:
             result=temp*contrast
            else:
                result=temp
    else:
        if brightness>contrast:temp=img*brightness
        else:temp=img*contrast
        if apply_filters:result=temp.filter()
        else:result=temp
    return result


# Example 3: Code that needs optimization
# Ask Copilot Chat: "Optimize this code for better performance"
def find_common_elements(list1, list2, list3):
    common = []
    for item1 in list1:
        for item2 in list2:
            for item3 in list3:
                if item1 == item2 and item2 == item3 and item1 not in common:
                    common.append(item1)
    return common


# Example 4: Complex code that needs explanation
# Ask Copilot Chat: "Explain how this code works"
def recursive_merge(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = recursive_merge(result[key], value)
        else:
            result[key] = value
    return result


# Example 5: Code with potential bugs
# Ask Copilot Chat: "What are the potential issues in this code?"
def parse_log_entry(log_line):
    parts = log_line.split('|')
    timestamp = parts[0]
    level = parts[1]
    message = parts[2]
    return {
        'time': timestamp,
        'level': level,
        'message': message,
        'source': parts[3]
    }

