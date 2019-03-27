import random
capitals={"Washington":"Olympia","Oregon":"Salem",
                    "California":"Sacramento","Ohio":"Columbus",
                    "Nebraska":"Lincoln","Colorado":"Denver",
                    "Michigan":"Lansing","Massachusetts":"Boston",
                    "Florida":"Tallahassee","Texas":"Austin",
                    "Oklahoma":"Oklahoma City","Hawaii":"Honolulu",
                    "Alaska":"Juneau","Utah":"Salt Lake City",
                    "New Mexico":"Santa Fe","North Dakota":"Bismarck",
                    "South Dakota":"Pierre","West Virginia":"Charleston",
                    "Virginia":"Richmond","New Jersey":"Trenton",
                    "Minnesota":"Saint Paul","Illinois":"Springfield",
                    "Indiana":"Indianapolis","Kentucky":"Frankfort",
                    "Tennessee":"Nashville","Georgia":"Atlanta",
                    "Alabama":"Montgomery","Mississippi":"Jackson",
                    "North Carolina":"Raleigh","South Carolina":"Columbia",
                    "Maine":"Augusta","Vermont":"Montpelier",
                    "New Hampshire":"Concord","Connecticut":"Hartford",
                    "Rhode Island":"Providence","Wyoming":"Cheyenne",
                    "Montana":"Helena","Kansas":"Topeka",
                    "Iowa":"Des Moines","Pennsylvania":"Harrisburg",
                    "Maryland":"Annapolis","Missouri":"Jefferson City",
                    "Arizona":"Phoenix","Nevada":"Carson City",
                    "New York":"Albany","Wisconsin":"Madison",
                    "Delaware":"Dover","Idaho":"Boise",
                    "Arkansas":"Little Rock","Louisiana":"Baton Rouge"}
for quizNum in range(35):
	quizFile = open('capitalsquiz%s.txt' %(quizNum+1),'w')
	answerKeyFile = open('capitalsquiz_answers%s.txt' %(quizNum+1),'w')
	quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
	quizFile.write((' ' * 20)+'state capitals Quiz (Form %s)' %(quizNum+1))
	quizFile.write('\n\n')
	states = list(capitals.keys())
	random.shuffle(states)
	for questionNum in range(50):
		correctAnswer = capitals[states[questionNum]]
		wrongAnswers = list(capitals.values())
		del wrongAnswers [wrongAnswers.index(correctAnswer)]
		wrongAnswers = random.sample(wrongAnswers,3)
		answerOptions = wrongAnswers + [correctAnswer]
		random.shuffle(answerOptions)
		quizFile.write('%s. What is the capital of %s?\n'%(questionNum +1,states[questionNum]))
		for i in range(4):
			quizFile.write('    %s.%s\n'%('ABCD'[i],answerOptions[i]))
		quizFile.write('\n')
		answerKeyFile.write('%s.%s\n'%(questionNum +1,'ABCD'[answerOptions.index(correctAnswer)]))	
quizFile.close()
answerKeyFile.close()
