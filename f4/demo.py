label = 'start'

while True:
    exec(f'''
if label == "start":
    print("We're stuck in a bad loop...")
    label = "middle"

elif label == "middle":
    print("This is the middle. But it means nothing.")
    label = "end"

elif label == "end":
    print("You thought it would end? Nope.")
    label = "start"
''')
