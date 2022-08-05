from faker import Faker
import csv   
import Constant

fake = Faker()

# Load the common nicknames from the file
def loadNicknames() : 

    nicknames = []
    with open(Constant.NICKNAMES_FILE_PATH, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            nicknames.append(row[2])

    return nicknames

# Load the common suffixes from the file
def loadSuffixes():
    suffixes = []

    with open(Constant.SUFFIXES_FILE_PATH, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            suffixes.append(row[0])

    return suffixes

# Load the common prefixes from the file
def loadPrefixes():
    prefixes = []

    with open(Constant.PREFIXES_FILE_PATH, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            prefixes.append(row[0])

    return prefixes


nicknames = loadNicknames()
suffixes = loadSuffixes()
prefixes = loadPrefixes()


# Generate a random username from the common nicknames , prefixes and suffixes by variation
def name(label):

    name = "";
    hasSuffix = fake.random_int(0, 10) >= 5;
    hasPrefix = hasSuffix == False and fake.random_int(0, 10) >= 5;

    if(hasSuffix): 
        suffix = suffixes[fake.random_int(0, len(suffixes) -1)]
        name = suffix.strip()


    index = fake.random_int(0, len(nicknames) -1)
    name = "{}{}".format(name, nicknames[index].strip())
    
    if(hasPrefix): 
        prefix = prefixes[fake.random_int(0, len(prefixes) -1)]
        name = "{}{}".format(name,prefix).strip()


    name = name.lower();
    label.configure(text=name)
