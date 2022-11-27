#Function to open file
def open_file(name_file):
    file = 'Data Files/' + name_file + '.txt'
    with open(file,'r') as open_file:
        data = open_file.read()
        data_lines = data.split('\n')
        print('Successfully opened ' + name_file + '.txt.', '\n')
    return data_lines

#Function to analyze data and return incorrect data
def analyzing(data_lines):
    print('_________ ANALYZING _________')
    valid_line = []
    invalid_line = []
    #Exceptions when student'id is wrong or the number of answer is not exactly 25
    for line in data_lines:
        info = line.split(',')
        try:
            if len(info) != 26: raise Exception
            if len(info[0]) != 9: raise ValueError
            if info[0][0] != 'N': raise ValueError
            int(info[0][1:])
        except ValueError:
            print('Invalid line of data: N# is invalid\n'+line)
            invalid_line.append(line)
            continue
        except Exception:
            print('Invalid line of data: does not contain exactly 26 values:\n'+line)
            invalid_line.append(line)
            continue    
        valid_line.append(line)
    if len(invalid_line) == 0:
        print('No errors found!')
    print('__________ REPORT ___________',
            '\nTotal valid lines of data:', len(valid_line),
            '\nTotal invalid lines of data:', len(invalid_line),'\n')
    return valid_line

#Function returning max values and index of them in a list
def find_max(a_list):
    index_skip = []
    result = []
    a = max(a_list)
    times = a_list.count(a)
    if times == 1:
        index_skip.append(a_list.index(a))
    else:
        for i in range(len(a_list)):
            if a_list[i] == a:
                index_skip.append(i)
            else:
                continue
    for i in index_skip:
        result.append('Question '+ str(i+1)+' - '+ str(a_list[i]) + ' students'+' - '+'Rate '+ str("{:.2f}".format(a_list[i]/len(valid_line))))
    return result

#Function to get number of high score (>80) students
def high(a_list):
    count = 0
    for i in a_list:
        if i > 80:
            count += 1
        else:
            continue
    return count

#Function to get median of a list
def median(num_list):
    num_list = sorted(num_list)
    position = len(num_list)//2
    med = num_list[position]
    return med

#Answer
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
answer = answer_key.split(',')

#Creating list score of students in class and 2 of the most skipped question and the most incorrectly answered question
def create_list_score(valid_line):
    skip_list = []
    incorrect_list = []
    for i in range(25):
        skip_list.append(0)
        incorrect_list.append(0)
    list_score = []
    for line in valid_line:
        name = line.split(',')[0]
        info = line.split(',')[1:]
        score = 0
        for i in range(25):
            if info[i] == '':
                score += 0
                skip_list[i] += 1
            elif info[i] == answer[i]:
                score += 4
            else:
                score -= 1
                incorrect_list[i] += 1
        list_score.append(score)
    return list_score, skip_list, incorrect_list


#Function returning more details of the data - mean, median, high scores, etc.
def detail_data(list_score, skip_list, incorrect_list):
    #Get High score
    print('Total student of high scores:', high(list_score))

    #Get Average score
    mean = sum(list_score)/len(list_score)
    print('Mean (average) score:', "{:.2f}".format(mean))

    #Get Highest score
    print('Highest score:', max(list_score))

    #Get Lowest score
    print('Lowest score:', min(list_score))

    #Get Rang of score
    print('Range of scores:', max(list_score)-min(list_score))

    #Get Median of score
    print('Median score:', median(list_score), '\n')

    #Get info of skipping question
    skip_result =''
    for i in find_max(skip_list):
        skip_result = skip_result + '\n'+ i + ', '
    print('Questions that most people skip:', skip_result, '\n')

    #Get info of incorrect question
    incorrect_result =''
    for i in find_max(incorrect_list):
        incorrect_result = incorrect_result + '\n'+ i + ', '
    print('Question that most people answer incorrectly:', incorrect_result, '\n')

#Function creating new .txt result file
def create_txt_file(list_score, valid_line):
    with open(input_file + '_grades.txt', 'w') as output_file:
        for (i, score) in enumerate(list_score):
            output_file.write(valid_line[i][:9] + ',' + str(score) + '\n')
        print('Extracting file', input_file+'_grades.txt', 'successfully!')

#Executing code
input_file = input("Enter a class file to grade (i.e. class1 for class1.txt): ")
data_lines = open_file(input_file)
valid_line = analyzing(data_lines)
list_score, skip_list, incorrect_list = create_list_score(valid_line)
detail_data(list_score, skip_list, incorrect_list)
create_txt_file(list_score, valid_line)