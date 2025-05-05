// Example 1: Python to JavaScript Translation
// Ask Copilot Chat: "Help translate this Python code to idiomatic JavaScript"
// Original Python code:
/*
def process_data(data, threshold=0.5, max_iterations=100):
    results = []
    for i in range(max_iterations):
        filtered = [x for x in data if x > threshold]
        if not filtered:
            break
        normalized = [(x - min(filtered)) / (max(filtered) - min(filtered)) for x in filtered]
        results.extend(normalized)
        threshold *= 1.1
    return results
*/

// JavaScript version needs translation of:
// 1. List comprehensions
// 2. extend() method
// 3. Python's range() function
function processData(data, threshold = 0.5, maxIterations = 100) {
    // Ask Copilot Chat: "Complete this JavaScript translation"
}


// Example 2: Translating messy Python code
// Ask Copilot Chat: "Help translate and clean up this Python code in JavaScript"
// Original Python code:
/*
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
*/

function calculateValues(x, y, z, flag = false) {
    // Ask Copilot Chat: "Complete this clean JavaScript translation"
}


// Example 3: Optimizing algorithms across languages
// Ask Copilot Chat: "Help translate and optimize this Python code in JavaScript"
// Original Python code:
/*
def find_duplicates(items):
    duplicates = []
    for i in range(len(items)):
        for j in range(len(items)):
            if i != j and items[i] == items[j] and items[i] not in duplicates:
                duplicates.append(items[i])
    return duplicates
*/

function findDuplicates(items) {
    // Ask Copilot Chat: "Complete this optimized JavaScript version"
}


// Example 4: Data structure differences
// Ask Copilot Chat: "Help handle these Python data structures in JavaScript"
// Topics to cover:
// - Sets vs Arrays
// - Dictionary vs Object
// - List methods vs Array methods
// - Python's None vs JavaScript's null/undefined
function dataStructureExamples() {
    // Python: my_set = {1, 2, 3}
    const mySet = new Set([1, 2, 3]);

    // Python: my_dict = {"key": "value"}
    const myDict = {
        key: "value"
    };

    // Ask Copilot Chat: "Show more JavaScript equivalents of Python data structures"
}


// Example 5: Error handling differences
// Ask Copilot Chat: "Help translate Python error handling to JavaScript"
// Python try/except vs JavaScript try/catch
function errorHandlingExample() {
    // Python:
    /*
    try:
        result = x / y
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except Exception as e:
        print(f"An error occurred: {e}")
    */

    // Ask Copilot Chat: "Complete this JavaScript error handling"
}


// Test data for demonstrations
const sampleData = [1.2, 3.4, 0.5, 2.8, 4.1];
const nestedData = {
    a: [1, 2, {}, 3],
    b: { x: [], y: 4 },
    c: []
};

// You can run these examples and ask Copilot Chat about:
// 1. "What are the key differences between Python and JavaScript for this code?"
// 2. "How can I make this JavaScript code more idiomatic?"
// 3. "What are the performance implications of these translations?"