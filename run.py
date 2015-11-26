import sqlite3, csv
import collections
import itertools

class AprioriAlgorithm:
    def __init__(self, minSupport, minConfidence, conn):
        self.conn = conn
        self.minSupport = minSupport
        self.minConfidence = minConfidence
        self.uniqueSets = collections.defaultdict(set)
        self.cols = dict()
        self.totalCount = 1
        self.init()
        self.legend = self.makeLegend()
        self.output = ''

    def makeLegend(self):
        legend = dict()
        with open('Legend.csv','rb') as fin:
            dr = csv.DictReader(fin)
            for row in dr:
                if row['space_id']:
                    legend[int(row['space_id'])] = row['space'].lower()
                if row['type_id']:
                    legend[int(row['type_id'])] = row['type'].lower()
                if row['category_id']:
                    legend[int(row['category_id'])] = row['category'].lower()
        return legend

    def init(self):
        cursor = conn.execute("SELECT * FROM APRIORITEST4")
        for row in cursor:
            self.uniqueSets["space_id"].add(row[0])
            self.cols[row[0]] = "space_id"
            self.uniqueSets["type_id"].add(row[1])
            self.cols[row[1]] = "type_id"
            self.uniqueSets["category_id"].add(row[2])
            self.cols[row[2]] = "category_id"
        cursor = self.conn.execute("SELECT COUNT(*) FROM APRIORITEST4")
        self.totalCount = float([row[0] for row in cursor][0])


    # Getting Support for a particular combination of entries
    def getSupport(self, itemSet):
        col = dict({"space_id":-1, "type_id":-1, "category_id":-1})
        for var in itemSet:
            col[self.cols[var]] = var

        where = ''
        for key in col:
            if col[key] is not -1:
                tmp = key + '=' + `col[key]`
                where = ' AND '.join([where, tmp]) if where is not '' else tmp

        query = "SELECT COUNT(*) FROM APRIORITEST4 WHERE " + where
        cursor = self.conn.execute(query)
        support = [row[0] for row in cursor][0]/self.totalCount
        return support

    def nextIteration(self, Lp):
        size = len(Lp[0]) + 1
        # generated all possible combinations from L(n-1)
        C = [list(val) for val in itertools.combinations(Lp, 2)]

        C = map(lambda a:reduce(lambda x,y:x.union(y), a, set()), C)

        # size check
        C = [val for val in C if len(val) is size]

        # remove duplicate sets
        tmp = list()
        [tmp.append(val) for val in C if val not in tmp]
        C = tmp

        # check no duplicate columns
        C = [s for s in C if len(set([self.cols[val] for val in s])) is size]

        # Prune Step We find all the n-1 length combinations of the items in
        # candidate set. If any of the n-1 length combinations of an item is not a
        # part of L(n-1) then we eliminate that item from the candidate set
        for val in C:
            [C.remove(val) for temp in itertools.combinations(val,len(val)-1) if set(temp) not in Lp]

        # Finding all the large frequency items
        L = [val for val in C if self.getSupport(val) >= self.minSupport]

        return L

    def apriori(self):
        large = list()
        C1 = reduce(lambda a,b:a.union(b), self.uniqueSets.values(), set())
        C1 = map(lambda a:set({a}), C1)
        L1 = [val for val in C1 if self.getSupport(val) >= self.minSupport]
        large = large + L1

        L = self.nextIteration(L1)

        large = large + L

        while len(L) > 0 and len(L[0]) < 3:
            L = self.nextIteration(L)
            large = large + L

        m = dict()
        for a in large:
            m[tuple(a)] = self.getSupport(a)

        self.output += "Frequent Itemsets (Minimum Support: " + `self.minSupport` + ")\n"
        for key in sorted(m, key=m.get, reverse=True):
            self.output += '[' + ', '.join(self.legend[item] for item in key) + ']: Support ->  ' + `m[key]*100` + '%\n'
        self.output += '\n'
        self.getAssociations(m)
        print '\n' + self.output + '\n'
        f = open('output.txt','w')
        f.write(self.output)
        f.close()

    def getAssociations(self, m):
        confDict = dict()
        for s in m:
            if len(s) > 1:
                itemSet = set(s)
                for i in s:
                    item = set({i})
                    diff = itemSet.difference(item)
                    conf = self.getSupport(itemSet)/self.getSupport(diff)
                    if conf >= self.minConfidence:
                        rule = '[' + ', '.join(self.legend[x] for x in diff) + "] => "
                        rule += '[' + ', '.join(self.legend[x] for x in item) + "]"
                        confDict[rule] = conf

        self.output += "Association Rules (Minimum Confidence: " + `minConfidence` + ")\n"
        for key in sorted(confDict, key=confDict.get, reverse=True):
            self.output += key + ": Confidence - " + `confDict[key]*100` + '%\n'


def create_table(conn):
	conn.execute('''CREATE TABLE APRIORITEST4(space_id INT NOT NULL,type_id INT NOT NULL,category_id INT NOT NULL);''')
	print "Table created successfully\n"

def insert_from_csv(conn, fileName):
	with open(fileName,'rb') as fin:
		dr = csv.DictReader(fin)
	 	to_db = [(i['space_id'],i['type_id'],i['category_id']) for i in dr]
	conn.executemany("INSERT INTO APRIORITEST4 (space_id,type_id,category_id) VALUES (?, ?, ?);", to_db)
	conn.commit()

def delete_table(conn):
    conn.execute("DROP TABLE IF EXISTS APRIORITEST4;")
    print "Table deleted successfully\n"

if __name__=="__main__":
    fileName = raw_input('Enter File Name (Integrated-Dataset.csv) : ') or "Integrated-Dataset.csv"
    minSupport = float(raw_input('Enter Minimum Support (0.05 by default) : ') or '0.05')
    minConfidence = float(raw_input('Enter Minimum Confidence (0.5 by default) : ') or '0.5')

    conn = sqlite3.connect('test.db')
    # delete_table(conn)
    create_table(conn)
    insert_from_csv(conn, fileName)
    apriori = AprioriAlgorithm(minSupport, minConfidence, conn)
    apriori.apriori()
    delete_table(conn)
    conn.close()
