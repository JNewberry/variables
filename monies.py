#John Newberry
#22/09/2014
#currency problem

number = int(input("please enter money: "))
note20s = number // 20
remainder = number % 20
note10s = remainder // 10
remainder = remainder % 10
note5s = remainder // 5
remainder = remainder % 5
coin2s = remainder // 2
remainder = remainder % 2
coin1s = remainder

print("the amount will consist of {0} £20 notes {1} £10 notes {2} £5 notes {3} £2 coins and {4} £1 coins".format(note20s,note10s,note5s,coin2s,coin1s))

      
            
