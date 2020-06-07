#initializing name and values for individual box
boxnames = {"a1":" ","a2":" ","a3":" ","b1":" ","b2":" ","b3":" ","c1":" ","c2":" ","c3":" "}

# To find the player's turn
count = 1

# Describtion of the games
def describe():
    print(" TIC TAK TOE ".center(50,"#"),"\n")
    print(f"""\t\t|  a1  |  a2  |  a3  |
            \t-------------------
            \t|  b1  |  b2  |  b3  |
            \t-------------------
            \t|  c1  |  c2  |  c3  |
            
            The player who sequence their symbol first, is the winner of the game!
            
            Give two inputs seperated by space eg: 'a1 x'
            
            Type 'stop' to end the GAME.\n""")

# class for the TikTakToe
class TikTakToe(object):
    
    #constructor of the class
    def __init__(self,userinput):
        self.userinput = userinput.lower()
        self.output = self.display(self.userinput)
        
        # printing the output based on condition
        if self.output is None:
            
            print(f"""\t\t|  {boxnames["a1"]}  |  {boxnames["a2"]}  |  {boxnames["a3"]}  |
            \t-------------------
            \t|  {boxnames["b1"]}  |  {boxnames['b2']}  |  {boxnames['b3']}  |
            \t-------------------
            \t|  {boxnames['c1']}  |  {boxnames['c2']}  |  {boxnames['c3']}  |""")
            
        elif self.output.endswith("wins!"):
            
            print(f"""\t\t|  {boxnames["a1"]}  |  {boxnames["a2"]}  |  {boxnames["a3"]}  |
            \t-------------------
            \t|  {boxnames["b1"]}  |  {boxnames['b2']}  |  {boxnames['b3']}  |
            \t-------------------
            \t|  {boxnames['c1']}  |  {boxnames['c2']}  |  {boxnames['c3']}  |""")
            print(f"\nPlayer {self.output}")
            
        else:
            print(self.output)
    
    # function to check the input characteristics
    def input_check(self,inputcheck):
        splitted = inputcheck.split(" ")
        splittedlength = len(splitted)
        if splittedlength == 2:
            if splitted[0] not in ["a1","a2","a3","b1","b2","b3","c1","c2","c3"] or splitted[1] not in ["x","o"]:
                return f"Incorrect input."
            else:
                if count%2==0 and splitted[1]=="x":
                    return "This is 'o's turn"
                elif (count%2!=0) and (splitted[1]=="o"):
                    return "This is 'x's turn"
                else:
                    return splitted
        else:
            return "Input is missing! (give two input separated by space)"
    
    # assing the symbol to the position
    def assign_fun(self,assign):
        if isinstance(assign,list):
            if boxnames[assign[0]] == " ":
                boxnames[assign[0]]=assign[1]
                return assign
            else:
                return f"place is already filled with {boxnames[assign[0]]}"
        else:
            return assign
    
    # analysing to check the condition for winning
    def analyse_fun(self,analyse):
        if isinstance(analyse,list):
            v1 = {"a1":boxnames["a1"],"b1":boxnames["b1"],"c1":boxnames["c1"]}
            v2 = {"a2":boxnames["a2"],"b2":boxnames["b2"],"c2":boxnames["c2"]}
            v3 = {"a3":boxnames["a3"],"b3":boxnames["b3"],"c3":boxnames["c3"]}
            h1 = {"a1":boxnames["a1"],"a2":boxnames["a2"],"a3":boxnames["a3"]}
            h2 = {"b1":boxnames["b1"],"b2":boxnames["b2"],"b3":boxnames["b3"]}
            h3 = {"c1":boxnames["c1"],"c2":boxnames["c2"],"c3":boxnames["c3"]}
            d1 = {"a1":boxnames["a1"],"b2":boxnames["b2"],"c3":boxnames["c3"]}
            d2 = {"a3":boxnames["a3"],"b2":boxnames["b2"],"c1":boxnames["c1"]}
            paths = [v1,v2,v3,h1,h2,h3,d1,d2]
            selectedpaths = []
            looplength = 0
            
            # for loop to find the path for current position
            for path in paths:
                for key in path.keys():
                    if key == analyse[0]:
                        selectedpaths.append(path)
                    else:
                        pass
                    
            # loop to check whether the sequence is continuous or not
            for selectedpath in selectedpaths:
                for point in selectedpath.keys():
                    if selectedpath[point] != analyse[1]:
                        same = False
                        break
                    else:
                        same = True
                        looplength +=1
                if looplength == 3 and same:
                    break
                else:
                    pass
            if same:
                return f"{analyse[1]} wins!"
            else:
                return analyse
        
        else:
            return analyse
    
    # function to run all the other functions
    def display(self,userinput):
        assignparameter = self.input_check(userinput)
        analyseparameter = self.assign_fun(assignparameter)
        finalresult = self.analyse_fun(analyseparameter)
        if isinstance(finalresult,str):
            return finalresult
        else:
            return None

# calling the describe function
describe()

#loop until the game ends
while True:
    #player name
    if count%2==0:
        playername = 'o'
    else:
        playername = 'x'
    # player input
    userplay = str(input(f"Player '{playername}' : ")).lower()
    if userplay == "stop":
        print("\nThe GAME has been Stopped by the user :(")
        break
    else:
        print("\n")
        obj = TikTakToe(userplay)
        if obj.output is None:
            count += 1
        elif obj.output.endswith("wins!"):
            break
        else:
            pass
    if " " not in list(boxnames.values()):
        print("Tie match")
        break
    else:
        pass
    print("\n")