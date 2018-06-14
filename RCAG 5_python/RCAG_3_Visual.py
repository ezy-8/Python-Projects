#Rubik's cube algorithm generator inspired and adhering strictly to https://solvethecube.com/algorithms (meaning right handed algorithms only)
#always test code on terminal

#Image import using pip + pillow
from PIL import Image

#NOTICE
print "Based on your cube progress and your specific CFOP case, match one of the images and choose the respective algorithm."

#Progress on the cube and F2L, OLL, PLL case initialization
cube_progress = ["F2L", "OLL", "PLL"]
F2L_cases = ["basic case", "corner and edge in top", "corner pointing up, edge in top", "corner in top, edge in middle", "corner in bottom, edge in top", "corner in bottom, edge in middle"]
OLL_cases = ["crosses", "dots", "all corners", "lines", "Ts", "Zs", "big Ls", "Cs", "Ws", "Ps", "squares", "little Ls", "others"]
PLL_cases = ["edges only", "corners only", "edges and corners"]

#Questions on the cube progress (answer1)
print cube_progress[0:]
answer1 = raw_input("What is the progress with your cube solving? ")

#Loading the specific case and CFOP situation
if answer1 == cube_progress[0]:
	print F2L_cases[0:]
	answer2 = raw_input("What is your F2L case? (orientation of corner and edge pieces) ")
elif answer1 == cube_progress[1]:
	print OLL_cases[0:]
	answer3 = raw_input("What is your OLL case? (shape of the yellow layer) ")
elif answer1 == cube_progress[2]:
	print PLL_cases[0:]
	answer4 = raw_input("What is your PLL case? (involves edges and/or corners) ")

#F2L cases (answer2)
if answer2 == F2L_cases[0]:
	F2Lcase0 = Image.open('F2Lcase1.png')
	F2Lcase0.show()
elif answer2 == F2L_cases[1]:
	F2Lcase1 = Image.open('F2Lcase2.png')
	F2Lcase1.show()
elif answer2 == F2L_cases[2]:
	F2Lcase2 = Image.open('F2Lcase3.png')
	F2Lcase2.show()
elif answer2 == F2L_cases[3]:
	F2Lcase3 = Image.open('F2Lcase4.png')
	F2Lcase3.show()
elif answer2 == F2L_cases[4]:
	F2Lcase4 = Image.open('F2Lcase5.png')
	F2Lcase4.show()
elif answer2 == F2L_cases[5]:
	F2Lcase5 = Image.open('F2Lcase6.png')
	F2Lcase5.show()

#OLL cases (answer3)
if answer3 == OLL_cases[0]:
	OLLcase0 = Image.open('crosses.png')
	OLLcase0.show()
elif answer3 == OLL_cases[1]:
	OLLcase1 = Image.open('dots.png')
	OLLcase1.show()
elif answer3 == F2L_cases[2]:
	OLLcase2 = Image.open('all corners.png')
	OLLcase2.show()
elif answer3 == F2L_cases[3]:
	OLLcase3 = Image.open('lines.png')
	OLLcase3.show()
elif answer3 == F2L_cases[4]:
	OLLcase4 = Image.open('Ts.png')
	OLLcase4.show()
elif answer3 == F2L_cases[5]:
	OLLcase5 = Image.open('Zs.png')
	OLLcase5.show()
elif answer3 == OLL_cases[6]:
	OLLcase6 = Image.open('big Ls.png')
	OLLcase6.show()
elif answer3 == F2L_cases[7]:
	OLLcase7 = Image.open('Cs.png')
	OLLcase7.show()
elif answer3 == F2L_cases[8]:
	OLLcase8 = Image.open('Ws.png')
	OLLcase8.show()
elif answer3 == F2L_cases[9]:
	OLLcase9 = Image.open('Ps.png')
	OLLcase9.show()
elif answer3 == F2L_cases[10]:
	OLLcase10 = Image.open('squares.png')
	OLLcase10.show()
elif answer3 == OLL_cases[11]:
	OLLcase11 = Image.open('little Ls.png')
	OLLcase11.show()
elif answer3 == F2L_cases[12]:
	OLLcase12 = Image.open('others.png')
	OLLcase12.show()

#PLL cases (answer4)
if answer4 == PLL_cases[0]:
	PLLcase0 = Image.open('edges only.png')
	PLLcase0.show()
elif answer4 == PLL_cases[1]:
	PLLcase1 = Image.open('corners only.png')
	PLLcase1.show()
elif answer4 == F2L_cases[2]:
	PLLcase2 = Image.open('edges and corners.png')
	PLLcase2.show()