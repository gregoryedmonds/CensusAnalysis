import matplotlib.pyplot as plt
from operator import itemgetter

# set variable as file name
TYPE_EDU = '2016Census_G15_AUS.csv'

# open file and read
with open(TYPE_EDU, 'r') as file:
    contents = file.read()

# split file contents into two lists
lines = contents.splitlines()
edu_type = lines[0].split(',')[1:] # removes beginning ABS code cell heading
num_strings = lines[1].split(',')[1:] # removes beginning ABS code cell value

# numbers in list (2) are strings, convert to ints
num_people = []
for stringdata in num_strings:
    num_people.append(int(stringdata))

# remove grand total headings and values in both lists
edu_type = edu_type[:-3]
num_people = num_people[:-3]

# slice to get grouped totals of two genders
grouped = slice(2, len(num_people), 3)
edu_type_grouped = edu_type[grouped]
num_people_grouped = num_people[grouped]

# bar plot of grouped totals with subtotals in green
plt.figure(figsize = (12, 8))
bar_grouped = plt.bar(edu_type_grouped, num_people_grouped)

def greenbar(bar_grouped, index):
    bar_grouped[index].set_color('g')

greenbar(bar_grouped, 0)
greenbar(bar_grouped, 4)
greenbar(bar_grouped, 8)
greenbar(bar_grouped, 14)
greenbar(bar_grouped, 20)
greenbar(bar_grouped, 24)
greenbar(bar_grouped, 25)

plt.tick_params(axis='x', labelrotation=90)
plt.xlabel("Type of institution")
plt.ylabel("Number of students")
plt.title("Type of Eductaional Institution Attended (With Subtotals), 2016 Census")
plt.tight_layout()

# pop subtotals
def popper(category):
    ix = edu_type_grouped.index(category)
    edu_type_grouped.pop(ix)
    num_people_grouped.pop(ix)

popper('Infants_Primary_Tot_P')
popper('Secondary_Tot_P')
popper('Tec_Furt_Educ_inst_Tot_P')
popper('Uni_other_Tert_Instit_Tot_P')
popper('Other_type_educ_instit_Tot_P')

# pop type of educational institution not stated
ix = edu_type_grouped.index('Type_educanl_institution_ns_P')
edu_type_grouped.pop(ix)
num_people_grouped.pop(ix)

# sorting pairs using zip
pairs = []
for i in range(len(num_people_grouped)):
    pairs.append((num_people_grouped[i], edu_type_grouped[i]))

pairs = zip(num_people_grouped, edu_type_grouped)
pairs_list = list(pairs)
pairs_list.sort(reverse = True)

# unzipping
sorted_cat = []
sorted_num = []
for i in range(len(num_people_grouped)):
    sorted_cat.append(pairs_list[i][1][:-2]) # clean
    sorted_num.append(pairs_list[i][0])

# new bar plot of only grouped totals, sorted
plt.figure(figsize = (12, 8))
plt.bar(sorted_cat, sorted_num)
plt.tick_params(axis='x', labelrotation=90)
plt.xlabel("Type of institution")
plt.ylabel("Number of students")
plt.title("Type of Eductaional Institution Attended, 2016 Census")
plt.tight_layout()

# pie chart
plt.pie(sorted_num, labels = sorted_cat)
plt.title("Type of educational institution")

# slice to get males
male = slice(0, len(num_people), 3)
edu_type_male = edu_type[male]
num_people_male = num_people[male]

# slice to get females
female = slice(1, len(num_people), 3)
edu_type_female = edu_type[female]
num_people_female = num_people[female]

# plot males and females for infants primary government
plt.figure(figsize = (12, 8))
plt.bar("Males", num_people_male[1])
plt.bar("Females", num_people_female[1])
plt.tick_params(axis='x')
plt.xlabel("Gender")
plt.ylabel("Number of students")
plt.title("Plot A: Infants/Primary School Students in Government Institutions")
plt.tight_layout()

# plot males and females for secondary government
plt.figure(figsize = (12, 8))
plt.bar("Males", num_people_male[5])
plt.bar("Females", num_people_female[5])
plt.tick_params(axis='x')
plt.xlabel("Gender")
plt.ylabel("Number of students")
plt.title("Plot B: Secondary Students in Government Institutions")
plt.tight_layout()

# plot males and females for uni other tert ft
plt.figure(figsize = (12, 8))
plt.bar("Males", num_people_male[15])
plt.bar("Females", num_people_female[15])
plt.tick_params(axis='x')
plt.xlabel("Gender")
plt.ylabel("Number of students")
plt.title("Plot C: Full-time Univeristy/Tertiary Students Between 15-24 Years Old")
plt.tight_layout()

percent_differenceA = round(((num_people_male[1] - num_people_female[1]) / num_people_female[1]) * 100, 3)
percent_differenceB = round(((num_people_male[5] - num_people_female[5]) / num_people_female[5]) * 100, 3)
percent_differenceC = round(((num_people_female[15] - num_people_male[15]) / num_people_male[15]) * 100, 3)

# summary
print("Plot A: there are", percent_differenceA, "percent more males than females enrolled")
print("Plot B: there are", percent_differenceB, "percent more males than females enrolled")
print("Plot C: there are", percent_differenceC, "percent more females than males enrolled")

# read data and split into two lists as before
OCCU = '2016Census_G57A_AUS.csv'
with open(OCCU, 'r') as file:
    contents = file.read()

lines = contents.splitlines()
work_type = lines[0].split(',')[1:] # removes beginning ABS code cell heading
num_strings = lines[1].split(',')[1:]

num_people = []
for stringdata in num_strings:
    num_people.append(int(stringdata))

# store variable with number of male labourers age 15-19
Male_15_to_19_Labourers = work_type[7]
Male_15_to_19_Labourers_Num = num_people[7]

# store variable with number of female labourers age 15-19
Female_15_to_19_Labourers = work_type[107]
Female_15_to_19_Labourers_Num = num_people[107]

# store combination of both groups in new lists
Male_Female_Labourer = []
Male_Female_Labourer_Num = []

Male_Female_Labourer.append("Male Labourers Aged 15 to 19")
Male_Female_Labourer.append("Female Labourers Aged 15 to 19")

Male_Female_Labourer_Num.append(Male_15_to_19_Labourers_Num)
Male_Female_Labourer_Num.append(Female_15_to_19_Labourers_Num)

# summary
print("Male Labourers Aged 15 to 19:", Male_15_to_19_Labourers_Num)
print("Female Labourers Aged 15 to 19:", Female_15_to_19_Labourers_Num)

# pie chart of male and female labourers age 15-19
plt.pie(Male_Female_Labourer_Num, labels = Male_Female_Labourer, autopct='%1.2f%%')

plt.show()