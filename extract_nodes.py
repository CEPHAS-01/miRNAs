#File to extract node pairs [edge] for graph construction
#Working!
import sys

infile = sys.argv[1]
outfile = sys.argv[2]


'''class prof_object:

        def __init__(self,id,start,end,value):
                self.id = id
                self.start = start
                self.end = end
                self.value = value
'''

masterList = {} #create an empty dictionary

outHandle = open(outfile,'w')

with open(infile) as f:
        for eachLine in f:
                elems = eachLine.split("\t")                            # split each element
                ID = elems[2]                                           # extract only the ID
                value = elems[12].strip(' \t\r\n')                      # extract the value which contain all the genes and feature
                targets = value.split("&")                              # split if more than one gene
                target_list = []                                        # declare the list to hold all the gene elements
                if (len(targets) == 2):                                 # a check to ensure that the elements are two, for one gene only. more than one gene will be 4 or more
                        #target_list.append(value)
                        #this is where you get the node and target
                        outHandle.write(ID + "\t" + targets[0] + "\t" + targets[1] + "\n")
                elif (len(targets) > 2):
                        #target_list = []
                        #check that the number of elements is even
                        if((len(targets) % 2) == 0):                                    # a check to ensure that the elements are even - they have to be even
#                               print(str(len(targets) % 2) + " " + str(targets))
                                for element in range(0,len(targets),2):
                                        key = str(targets[element]) + "\t" + str(targets[element+1])
                                        #target_list.append(key)
                                        outHandle.write(ID + "\t" + key + "\n")
                        else:
                                print("There is a likely error! - Elements not even")
                elif (len(targets) == 1):
                outHandle.write(ID + "\t" + value + "\n")
                else:
                        print("")

