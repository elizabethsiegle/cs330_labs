import csv
import collections

def main():
    states = {}
    with open('USStates.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        for row in reader:
            states[row[0]] = row[1:]
        most_n_state(states)
        get_results(states)
        print("Is there a path to get from Washington to District of Columbia?")
        Search("Washington", "District of Columbia", states)


#find state with most neighbors    
def most_n_state(states):
    most_n = 0
    for k, v in states.items():
        n_len = len(v)
        if n_len > most_n:
            most_n_state = [k]
            most_n = n_len
        elif most_n == len(v):
            most_n_state.append(k)
        s = ", "
        print("The state(s) with the most neighbors:", s.join(most_n_state))
        print("Most number of neighbors:", most_n)


#find neighbors of input state    
def get_results(states):
    in_state = input("Enter a state: ")
    if in_state in states:
    	neighbors = states[in_state]
    	if len(neighbors) == 1:
       	    print(in_state, "has no neighbors.")
    	else:
            s = ", "
            print(in_state + " has the following neighbors:", s.join(neighbors))
    else:
        print("Could not find any results.")

   	 
#find path from start state to goal state    
def Search(startNode, goalNode, states):
    start = startNode
    goal = goalNode
    visitedStates = []

    OPEN = [start]
    CLOSE = []
    
    while OPEN != []:
    	current = OPEN.pop()
    	visitedStates.append(current)
    	succContainsWoman = []
    	s = ", "
   	 
    	if current == goal:
            print("Yes. To get from Washington to District of Columbia, march as follows:")
            print(s.join(visitedStates))
            return True
    	elif current not in CLOSE:
            CLOSE.append(current)
            successors = states[current] #rest of states
            for u in successors:
            	if u.startswith('W') or u.startswith('O') or u.startswith('M') or u.startswith('A') or u.startswith('N') or u == 'District of Columbia':
                    succContainsWoman.append(u)
                    for s in succContainsWoman:
            	        if s not in visitedStates:
                            OPEN.append(s)       	 

    print ("No. There is no way to get from Washington to District of Columbia.")
    return False


if __name__=="__main__":
	main()

