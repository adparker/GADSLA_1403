'''This is a short exercise designed to test your knowledge of basic natural
language processing (NLP) techniques in Python. It is also one of the interview
questions I ask entry-level data science candidates at Whisper.

In each of the parts below, I have provided a function definition (with the
correct arguments but no implementation) and some tests that will pass *if* 
you fill in the correct implementation for each function. If you run this file
 (i.e. run `python nlp_exercise.py` from your shell) and it does not throw
 any errors, then you have finished the exercise!
'''

# Question 1: Normalization and Tokenization

def process_text(text):
    '''FILL IN ANSWER HERE.'''
    
# BEGIN TESTS
assert process_text('Python is SO AWESOME!!!!!! YAy!!!!@ I love programming in python!') == ['python', 'is', 'so', 'awesome', 'yay', 'i', 'love', 'programming', 'in', 'python']
# END TESTS


# Question 2: Count word occurences
def count_words(text):
    '''FILL IN ANSWER HERE.'''

# BEGIN TESTS
assert count_words('Python is SO AWESOME!!!!!! YAy!!!!@ I love programming in python!') == {'yay': 1, 'python': 2, 'is': 1, 'programming': 1, 'i': 1, 'so': 1, 'in': 1, 'love': 1, 'awesome': 1}
# END TESTS

# Question 3: Create a string distance function
def distance(text1, text2):
    '''FILL IN ANSWER HERE.'''

# BEGIN TESTS
assert distance('I love my mom', 'i love my daddy') < distance('I love my mom', 'I am a big boy now')
assert distance('some strings are similar to other strings', 'some strings') > distance('some strings are similar to other strings', 'some strings are similar')
assert distance('i hate hate hate noodles.', 'i hate hate noodles') < distance('i hate hate hate noodles.', 'i hate noodles.')
# END TESTS

print 'All tests passed. Congratulations!'


