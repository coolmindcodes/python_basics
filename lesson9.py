# loops

while True:
    print("Hello, loops")
    break # stop

scores = [90,76, 56, 81, 78, 99,54, 78, 34, 65, 78, 45, 23, 56, 89, 89, 45, 67, 45, 68, 77, 76]

# for each loop
for score in scores:
    if score >= 50 and score <=70  and score % 2 == 0:
      print(score)
      
