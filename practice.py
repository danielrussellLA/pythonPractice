# methods
def reverse (x):
    reversed = ''
    for letter in x:
        reversed += letter
    print(reversed)

# reverse method
reverse('lienad');

# console log tricks
name = raw_input('what is your name?')
location = raw_input('where do you live?')
job = raw_input('What is your job?')

print "Ah, so your name is %s, you live in %s, " \
"and your job is %s." % (name, location, job)

# lopps
primes = [2, 3, 5, 7]
for prime in primes:
    print prime
