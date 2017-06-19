'''
	Austin Fouch
	CMPS 367 Python Programming
	Homework #5
	homework5.py
		This program asks the user for a input string representing a motif, and then the 
		frequency at which each nucleotide exists in the user's hypothetical genome. The
		program will calculate and print out the probability that a single sequence of the 
		same length is precisely the motif that the user entered. The program will also
		display plots that show:
			1) the probability of finding at least one of the user motifs in sequences 
			ranging from N to 5000, where N = length of the input motif.
			2) 
'''
import re	# regex
import matplotlib.pyplot as plt
import numpy as np
import random

'''
motif_probability()
	This function asks the user to input frequencies for each nucleotide in their motif.
	It will then calculate the probability of a sequence of length N (N = motif length)
	being preciselt the motif entered.
	Returns this probability.
'''
def motif_probability(motif, freqList):
	print("\nMotif: ", motif)
	print("Nucleotide\tFrequency")
	print("\tA\t",freqList[0]*100,"%")
	print("\tT\t",freqList[1]*100,"%")
	print("\tC\t",freqList[2]*100,"%")
	print("\tG\t",freqList[3]*100,"%")
	probability = 1.0
	motif = motif.upper()
	for i in range(0, len(motif)):
		if motif[i] == 'A':
			probability *= freqList[0]
		if motif[i] == 'T':
			probability *= freqList[1]
		if motif[i] == 'C':
			probability *= freqList[2]
		if motif[i] == 'G':
			probability *= freqList[3]
	output = "Probabiltiy of appearing in a sequence N = " + str(len(motif)) + " is "
	output = output + str(probability) + " (" + str(probability*100) + "%)"
	print(output)
	return probability
'''
motif_probability()
'''

'''
plot_proabability()
'''
def plot_proabability(motif, probability):
	plt.xlabel("Sequence Length")
	plt.ylabel("Probability of finding at least one motif")
	x = np.arange(len(motif), 5000)
	y = 1 - (1 - probability) ** x
	title = "Plot of probability of finding at least one\n " + motif.upper()
	title = title + " motif in a sequence of length N to 5000"
	plt.title(title)
	plt.plot(x, y)
	plt.show()
'''
plot_proabability()
'''

'''
gen_monte_carlo()
'''
def gen_monte_carlo(length, freqList):
	tmp = ""
	for c in range(0, length):
		rnd = random.random()
		if rnd < freqList[0]:
			tmp = tmp + 'A'
		elif freqList[0] <= rnd < (freqList[0] + freqList[1]):
			tmp = tmp + 'T'
		elif (freqList[0] + freqList[1]) <= rnd < (freqList[0] + freqList[1] + freqList[2]):
			tmp = tmp + 'C'
		elif rnd >= (freqList[0] + freqList[1] + freqList[2]):
			tmp = tmp + 'G'
	return tmp
'''
gen_monte_carlo()
'''

'''
plot_monte_carlo(motif)
'''
def plot_monte_carlo(motif, freqList):
	avg_100 = calc_avg_found(motif,freqList,100)
	avg_1k = calc_avg_found(motif,freqList,1000)
	avg_2k = calc_avg_found(motif,freqList,2000)
	avg_5k = calc_avg_found(motif,freqList,5000)
	avg_10k = calc_avg_found(motif,freqList,10000)
	plt.xlabel("Sequence Length")
	plt.ylabel("Amount of Times Motif was Found in Sequence")
	x = [100, 1000, 2000, 5000, 10000]
	y = [avg_100, avg_1k, avg_2k, avg_5k, avg_10k]
	title = "Expected number of motifs in sequence of length\n "
	title = title + "N = 100, N = 1000, N = 2000, N = 5000, and N = 10000"
	plt.title(title)
	plt.plot(x, y,'o', markersize=50)
	plt.show()
'''
plot_monte_carlo(motif)
'''

'''
calc_avg_found()
'''
def calc_avg_found(motif, freqList, length):
	for c in range(1, 100):
			tmp = gen_monte_carlo(length, freqList)
			start = 0
			count = 0
			while True:
				i = tmp.find(motif, start)
				if i >= 0:
					start = i + 1
					count += 1
				else:
					break
			count += count/100
	return count
'''
calc_avg_found()
'''

'''
Main
	Asks user for input motif, uses regex to make sure it is a proper motif. Passes this
	motif to functions in order to calculate probability and plot.
'''
while True:
	motif = input("Enter a motif: ").upper()
	# true if input motif contains chars other than atcg
	p = re.compile('[^atcg]', re.IGNORECASE)
	if p.search(motif):
		print("Invalid motif")
	else:
		break

while True:
		try:
			a_freq = float(input("Enter 'A' nucleotide frequency: "))/100
			t_freq = float(input("Enter 'T' nucleotide frequency: "))/100
			c_freq = float(input("Enter 'C' nucleotide frequency: "))/100
			g_freq = float(input("Enter 'G' nucleotide frequency: "))/100
			total_freq = a_freq + t_freq + c_freq +	g_freq
			if total_freq < 1.0 or total_freq > 1.0:
				print("Frequencies did not add up to 100%")
				exit()
			else:
				freqList = [a_freq, t_freq, c_freq, g_freq]
				break
		except ValueError:
			print("Input frequency is not a number")
			continue

probability = motif_probability(motif, freqList)
plot_proabability(motif, probability)
plot_monte_carlo(motif, freqList)
'''
Main
'''