#################################

#Ονοματεπώνυμο : Μιχαήλ Πανούσος | Βασίλειος Στεργιόπουλος
#AEM : 16435 | 17084
#Email : michpano@math.auth.gr | stergiop@math.auth.gr 


#################################

#Στην κλάση Cell ορίζουμε objects τύπου Cell ( δηλαδή το κάθε κελί του ταμπλό ).
#Πιο συγκεκριμένα, θέτουμε τιμές στα instance variables value,owner και με τα setters,getters
#έχουμε την δυνατότητα να αλλάξουμε και να ανακτήσουμε τιμές των παραπάνω variables.
#Ο σκοπός τους είναι να χρησιμοποιηθούν στα παρακάτω methods και στο main program


class Cell:
    def __init__(self, value, owner):
        self.value = value
        self.owner = owner

    def getValue(self):
        return self.value

    def getOwner(self):
        return self.owner

    def setValue(self, value):
        self.value = value

    def setOwner(self, owner):
        self.owner = owner


class Proximity21:
    def __init__(self, pid, length_X, length_Y):
        self.pid = pid
        self.length_X = length_X
        self.length_Y = length_Y

    #Σε αυτό το method ορίζουμε τον παίκτη που έχει σειρά να παίξει
    def setPid(self, pid):
        self.pid = pid

    #Σε αυτό το method ορίζουμε τις διαστάσεις του ταμπλό
    def setBoardSize(self, length_X, length_Y):
        self.length_X, self.length_Y = length_X, length_Y

    #Σε αυτό το method ανακτούμε το όνομα του παίκτη/ομάδα που βρίσκεται σε αυτό το πρόγραμμα
    def getPlayerName(self):
        return "Panousos_Stergiopoulos"

    #Σε αυτό το method δεχόμαστε το ταμπλό στην παρούσα κατάσταση ως είσοδο και ψάνχουμε τα κενά γειτονικά
    #των κατειλημμένων κελιών.
    #Στη συνέχεια, θέτουμε το owner ίσο με το pid και έτσι έχουμε τις πιθανές θέσεις που μπορεί να τοποθετηθεί
    #ο ακέραιος που δίνεται σε ένα κελί.Τέλος,επιστρέφουμε τη νέα αυτή τροποποιημένη λίστα.
    #Για να βρούμε τα κενά γειτονικά κάθε κελιού διακρίναμε τις περιπτώσεις ανάλογα με την τρέχουσα θέση
    #του κατειλημμένου κελιού.
    #Βρήκαμε ότι οι εξωτερικές πλευρές του ταμπλό αποτελούν οριακές συνθήκες και χρήζουν δικής τους
    #κατηγοριοποίησης ( πχ. τα άρτια πολλαπλάσια του length_X χωρίς το κελί της τελευταίας σειράς,δηλαδή το 90)
    #ενώ τα κελιά που βρίσκονται στις εσωτερικές πλευρές του ταμπλό έχουν όλα εώς και 6 κενά γειτονικά κελιά
    def findNeighbours(self, Cell_List):
        New_List = []
        for i in range(len(Cell_List)):
            if Cell_List[i].getValue() != 0:

                #Οριακή συνθήκη 1 / MAX 2 γειτονικά
                if i == 0:
                    Index_List1 = [i+1, i+self.length_X]
                    for j in Index_List1:
                        if Cell_List[j].getValue() == 0:
                            Cell_List[j].setOwner(self.pid)
                        New_List.append(Cell_List[j])

                #Οριακή συνθήκη2 / MAX 4 γειτονικά
                elif i < self.length_X-1:
                    Index_List2 = [i-1, i+1, i+self.length_X-1, i+self.length_X]
                    for j in Index_List2:
                        if Cell_List[j].getValue() == 0:
                            Cell_List[j].setOwner(self.pid)
                        New_List.append(Cell_List[j])

                #MAX 3 γειτονικά
                elif i == self.length_X-1:
                    Index_List3 = [i-1, i+self.length_X-1, i+self.length_X]
                    for j in Index_List3:
                        if Cell_List[j].getValue() == 0:
                            Cell_List[j].setOwner(self.pid)
                        New_List.append(Cell_List[j])

                #Οριακή συνθήκη3 / MAX 5 γειτονικά
                elif i in range(self.length_X, self.length_X*(self.length_Y-3) + 1, 2*self.length_X):
                    Index_List4 = [i+1, i-self.length_X, i-self.length_X+1, i+self.length_X, i+self.length_X+1]
                    for j in Index_List4:
                        if Cell_List[j].getValue() == 0:
                            Cell_List[j].setOwner(self.pid)
                        New_List.append(Cell_List[j])

                #Οριακή συνθήκη4 / MAX 3 γειτονικά
                elif i in range(2*self.length_X - 1, (self.length_X-1)*(self.length_Y-2) + 1, 2*self.length_X):
                    Index_List5 = [i-1, i-self.length_X, i+self.length_X]
                    for j in Index_List5:
                        if Cell_List[j].getValue() == 0:
                            Cell_List[j].setOwner(self.pid)
                        New_List.append(Cell_List[j])

                #Οριακή συνθήκη5 / MAX 3 γειτονικά
                elif i in range(2*self.length_X, self.length_X*(self.length_Y-1) + 1, 2*self.length_X):
                    Index_List6 = [i+1, i-self.length_X, i+self.length_X]
                    for j in Index_List6:
                        if Cell_List[j].getValue() == 0:
                            Cell_List[j].setOwner(self.pid)
                        New_List.append(Cell_List[j])

                #Οριακή συνθήκη6 / MAX 5 γειτονικά
                elif i in range(3*self.length_X-1, self.length_X*(self.length_Y-1), 2*self.length_X):
                    Index_List7 = [i-1, i-self.length_X-1, i-self.length_X, i+self.length_X-1, i+self.length_X]
                    for j in Index_List7:
                        if Cell_List[j].getValue() == 0:
                            Cell_List[j].setOwner(self.pid)
                        New_List.append(Cell_List[j])

                #MAX 6 γειτονικά
                elif self.length_X < i < self.length_X*self.length_Y-self.length_X-1:
                    Index_List8 = [i-1, i+1, i-self.length_X, i-self.length_X+1, i+self.length_X, i+self.length_X+1]
                    for j in Index_List8:
                        if Cell_List[j].getValue() == 0:
                            Cell_List[j].setOwner(self.pid)
                        New_List.append(Cell_List[j])

                #Οριακή συνθήκη7 / MAX 4 γειτονικά
                elif self.length_X*(self.length_Y - 1) < i < self.length_X*self.length_Y - 1:
                    Index_List9 = [i-1, i+1, i-self.length_X, i-self.length_X+1]
                    for j in Index_List9:
                        if Cell_List[j].getValue() == 0:
                            Cell_List[j].setOwner(self.pid)
                        New_List.append(Cell_List[j])

                #Οριακή συνθήκη8 / MAX 2 γειτονικά
                else:
                    Index_List10 = [i-1, i-self.length_X]
                    for j in Index_List10:
                        if Cell_List[j].getValue() == 0:
                            Cell_List[j].setOwner(self.pid)
                        New_List.append(Cell_List[j])

            else:
                New_List.append(Cell_List[i])
        return New_List

    #Σε αυτό το method καλούμαστε να τοποθετήσουμε τον ακέραιο k σε ένα κελί.
    #Η είσδοος της είναι ο ακέραιος αυτός και το ταμπλό στην τρέχουσα κατάσταση.
    #Στο πρώτο for loop ( 1η περίτπωση ) παίρνουμε την περίπτωση που το ταμπλό είναι κενό και έτσι γυρνάμε απλά ένα
    #από τα 4 κεντρικά κελιά.
    #Στη 2η περίπτωση επιλέγουμε τα τροποποιημένα κελιά που επιστρέφει η findNeighbours και βάσει αυτών ψάχνουμε τα
    #γειτονικά τους.
    #Για να πάρουμε τους περισσότερους δυνατούς πόντους ψάχνουμε είτε για ένα αντίπαλο κέλι με 0 < value < k είτε για
    #συνδυασμό αυτών και τοποθετούμε τον ακέραιο μας καταλλήλως.
    #Στην περίπτωση που δεν βρούμε καμία συμφέρουσα επιλογή, απλά τον τοποθετόυμε "τυχαία" σε κάποιο ελεύθερο κελί.
    def PlaceTile(self, k, Cell_List):
        for q in range(len(Cell_List)):
            j = 0
            if 0 <= j < len(Cell_List) - 1:
                while Cell_List[q].getValue() == 0:
                    j += 1
                    if j == len(Cell_List) - 1:
                        return self.length_X*(self.length_Y - 1) // 2
        New_List = self.findNeighbours(Cell_List)
        Index_List = []
        for i in range(len(New_List)):
            if New_List[i].getOwner() == self.pid and New_List[i].getValue() == 0:
                Index_List.append(i)
        Value_Neigh_List = []
        for emp in Index_List:
            Neigh_List = self.findMyNeighbours(emp)
            Opp_Neigh_List = []
            for neigh in Neigh_List:
                if New_List[neigh].getOwner() != self.pid and 0 < New_List[neigh].getValue() < k:
                    Opp_Neigh_List.append(neigh)
            if len(Opp_Neigh_List) >= 1:
                Value_Opp_Neigh_List = []
                for val in Opp_Neigh_List:
                    Value_Opp_Neigh_List.append(New_List[val].getValue())
                s = sum(Value_Opp_Neigh_List)
                Value_Neigh_List.append(s)
        if Value_Neigh_List:
            m = max(Value_Neigh_List)
            for ind in Index_List:
                MaxVals_Neigh_List = self.findMyNeighbours(ind)
                Opp_MaxVals_Neigh_List = []
                for neigh in MaxVals_Neigh_List:
                    if New_List[neigh].getOwner() != self.pid and 0 < New_List[neigh].getValue() < k:
                        Opp_MaxVals_Neigh_List.append(neigh)
                if len(Opp_MaxVals_Neigh_List) >= 1:
                    MaxValue_Opp_Neigh_List = []
                    for val in Opp_MaxVals_Neigh_List:
                        MaxValue_Opp_Neigh_List.append(New_List[val].getValue())
                    s1 = sum(MaxValue_Opp_Neigh_List)
                    if m == s1:
                        return ind
        else:
            for j in range(len(Cell_List)):
                if Cell_List[j].getValue() == 0 and Cell_List[j].getOwner() == 0:
                    return j

    #Αυτό το method λειτουργεί παραπλήσια με το findNeighbours,απλά δέχεται ως είσοδο έναν ακέραιο ( δηλαδή το index
    #του κελιού μέσα στη λίστα ) και βρίσκει όλα τα γειτονικά κελιά ( κατειλημμένα και μη ).
    #Η λογική της κατηγοριοποίησης είναι ακριβώς ίδια με αυτήν της findNeighbours.
    def findMyNeighbours(self, n):
        if n == 0:
            Neighbours_List1 = [1, self.length_X]
            return Neighbours_List1
        elif n < self.length_X - 1:
            Neighbours_List2 = [n - 1, n + 1, n + self.length_X - 1, n + self.length_X]
            return Neighbours_List2
        elif n == self.length_X - 1:
            Neighbours_List3 = [n-1, n+self.length_X-1, n+self.length_X]
            return Neighbours_List3
        elif n in range(self.length_X, self.length_X*(self.length_Y-3) + 1, 2*self.length_X):
            Neighbours_List4 = [n+1, n-self.length_X, n-self.length_X+1, n+self.length_X, n+self.length_X+1]
            return Neighbours_List4
        elif n in range(2*self.length_X-1, (self.length_X-1)*(self.length_Y-2) + 1, 2*self.length_X):
            Neighbours_List5 = [n-1, n-self.length_X, n+self.length_X]
            return Neighbours_List5
        elif n in range(2*self.length_X, self.length_X*(self.length_Y-1) + 1, 2*self.length_X):
            Neighbours_List6 = [n+1, n-self.length_X, n+self.length_X]
            return Neighbours_List6
        elif n in range(3*self.length_X- 1, self.length_X*(self.length_Y-1), 2*self.length_X):
            Neighbours_List7 = [n-1, n-self.length_X-1, n-self.length_X, n+self.length_X-1, n+self.length_X]
            return Neighbours_List7
        elif self.length_X < n < self.length_X*self.length_Y-self.length_X-1:
            Neighbours_List8 = [n-1, n+1, n-self.length_X, n-self.length_X+1, n+self.length_X, n+self.length_X+1]
            return Neighbours_List8
        elif self.length_X*(self.length_Y - 1) < n < self.length_X*self.length_Y - 1:
            Neighbours_List9 = [n-1, n+1, n-self.length_X, n-self.length_X+1]
            return Neighbours_List9
        else:
            Neighbours_List10 = [n - 1, n - self.length_X]
            return Neighbours_List10

    #Σε αυτό το method δίνουμε ως είσοδο έναν ακέραιο προς τοποθέτηση και το ταμπλό στην τρέχουσα κατάσταση.
    #Στη συνέχεια τοποθετείται σε ένα κελί σύμφωνα με τα methods PlaceTile,findMyNeighbours
    #Τέλος,εφαρμόζουμε απλά τους κανόνες του παχνιδιού για την απόκτηση ενός κελιού ή μη.
    #Δηλαδή,αν τα γειτονικά κελιά έχουν 0 < value < r,τότε καταλαμβάνονται,αλλάζει το χρώμα τους ( δηλ. ο owner )
    #και γίνεται ίδιο με αυτό του παίκτη που παίζει ( pid ).
    #Αλλιώς,αν τα γειτονικά κελιά είναι του ίδιου χρώματος,τότε αυξάνεται το value τους κατά 1
    #ενώ αν είναι κενά δεν αλλάζει τίποτα.
    #Τελικά, το method επιστρέφει τη νέα κατάσταση του ταμπλό.
    #Το Visualization_List είναι απλά μια οπτικοποίηση του ταμπλό.
    def applyChanges(self, r, Cell_List):
        s = self.PlaceTile(r, Cell_List)
        Neighbours_List = self.findMyNeighbours(s)
        New_List = []
        Visualization_List = []
        for i in range(len(Cell_List)):
            if i in Neighbours_List:
                if Cell_List[i].getOwner() == Cell_List[s].getOwner():
                    Cell_List[i].setValue(Cell_List[i].getValue() + 1)
                    New_List.append(Cell_List[i])
                else:
                    if 0 < Cell_List[i].getValue() < r:
                        Cell_List[i].setOwner(Cell_List[s].getOwner())
                        New_List.append(Cell_List[i])
            else:
                New_List.append(Cell_List[i])
        for j in range(len(New_List)):
            Visualization_List.append(f"cell{New_List[j].getValue(), New_List[j].getOwner()}")
        return New_List, Visualization_List


if __name__ == '__main__':
    c = Cell(0, 0)
    p1 = Proximity21(1, 4, 4)
    Tableau1 = [c for i in range(16)]
    Newlist = []
    print(Tableau1[1])
    Neigh1 = p1.findNeighbours(Tableau1)
    print(Neigh1)
    a1 = p1.PlaceTile(18, Tableau1)
    print(a1)
    MyNeigh1 = p1.findMyNeighbours(a1)
    print(MyNeigh1)
    Tableau2, Tableau2_Vis = p1.applyChanges(18, Tableau1)
    print(Tableau2)
    print(Tableau2_Vis)
    p2 = Proximity21(2, 4, 4)
    a2 = p2.PlaceTile(1, Tableau2)
    print(a2)

