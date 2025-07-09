questions = [['who is shah rukh khan?','WWE Wrestler','Actor','Astronaut','Plumber',2],
            ['who is the prime minister of india?','Narendra Modi','Rahul Gandhi','Arvind Kejriwal','Amit Shah',1], 
            ['who is the president of india?','Droupadi Murmu','Ram Nath Kovind','Pranab Mukherjee','A P J Abdul Kalam',1],
            ['who is the president of USA?','Donald Trump','Joe Biden','Barack Obama','George Bush',2],
            ['who is the prime minister of USA?','Donald Trump','Joe Biden','Barack Obama','George Bush',2],
            ['who is the prime minister of UK?','Rishi Sunak','Liz Truss','Boris Johnson','David Cameron',1],
            ['who is the prime minister of Pakistan?','Imran Khan','Shehbaz Sharif','Benazir Bhutto','Nawaz Sharif',2],
            ['who won the 2023 FIFA World Cup?','Argentina','France','Brazil','Germany',1],
            ['who won the 2023 ICC Cricket World Cup?','India','Australia','England','Pakistan',1],
            ['who is the CEO of Tesla?','Elon Musk','Jeff Bezos','Bill Gates','Mark Zuckerberg',1],
            ['who is the CEO of Amazon?','Elon Musk','Jeff Bezos','Bill Gates','Mark Zuckerberg',2]]

prizes = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
i = 0

for question in questions:
    
    print(question[0])
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")
    print(f"d.{question[4]}")

    #check whether the answer is correct or not
    a = int(input("Enter your answer (1 for a/2 for b/3 for c/4 for d): \n"))
    if (question[5] == a):
        print("Correct answer!")
    else:
        print(f"Incorrect answer! The correct answer is {question[5]}.")
        print("Better luck next time!")
        break
    
    print(f"You won {prizes[i]} rupees!")
    i += 1

