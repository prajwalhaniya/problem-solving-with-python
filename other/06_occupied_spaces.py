'''
You supervise a parking lot with n parking spaces. Yesterday, you recorded
whether each parking space was occupied by a car or was empty. Today, you
again recorded whether each parking space was occupied by a car or was
empty. Indicate the number of parking spaces that were occupied on both
days.

Input:

The input consists of three lines.
• The first line contains integer n, the number of parking spaces. n is
between 1 and 100.
• The second line contains a string of n characters for yesterday’s information, one character for each parking space. A C indicates an
occupied parking space (C for car), and a . indicates an empty parking space. For example, CC. means that the first two parking spaces
were occupied and the third was empty.
• The third line contains a string of n characters for today’s information, in the same format as the second line.

output:
Output the number of parking spaces that were occupied on both days.
'''

n = int(input())
yesterday = input()
today = input()

occupied = 0

for i in range(len(yesterday)):
    if yesterday[i] == 'C' and today[i] == 'C':
        occupied += 1

print(occupied)