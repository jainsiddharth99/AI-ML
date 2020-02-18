class graphs:
    graph={}

    def choice(self):
        s=6
        while s!=0:
            print("Enter your choice" )
            print("1: To insert a node")
            print("2: To insert an edge")
            print("3: To delete a node")
            print("4: To delete an edge")
            print("5: To Display the graph")
            print("0: To exit")
            s=int(input(s))
            if s==1:
                self.addnode()

            elif s==2:
                self.addedge()

            elif s==3:
                self.deletenode()

            elif s==4:
                self.delete_edge()

            elif s==5:
                self.displayg()
               
            elif s==0:
                exit(0)

            else:
                pass
           
    def addnode(self):
        print("Enter the new node ")
        node=int(input())
        if node not in self.graph:
            self.graph[node]=[]
            print("Node added")

        else:
            print("node already exists")
        self.choice()


    def displayg(self):
        print("The graph is: ")
        print(self.graph)
        self.choice()


    def addedge(self):
        print("enter the starting vertex: ")
        s=int(input())
        print("enter the ending vertex: ")
        e=int(input())
        if s in self.graph:
            if e in self.graph:
                self.graph[s].append(e)
                print("edge added")
            else:
                print("invalid vertex entered")
        else:
            print("invalid vertex entered")

        self.choice()

    def deletenode(self):
        print("Enter the node to delete ")
        n=int(input())
        if n in self.graph:
            for node in self.graph:
                for neighbour in self.graph[node]:
                    self.graph[node].remove(neighbour)

            self.graph.__delitem__(n)
            self.switch()
            print("node deleted")
        else:
            print("invalid node")
        self.choice()
       

    def delete_edge(self):
        print("enter the starting node: ")
        s=int(input())
        print("enter the ending node")
        e=int(input())
        if e in self.graph[s]:
            self.graph[s].remove(e)
            print("edge deleted")
        else:
            print("no edge found")
        self.choice()

g=graphs()
g.choice()
