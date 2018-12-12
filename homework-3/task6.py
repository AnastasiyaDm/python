''' Задача-6 (Не обязательно, для тех кто скучает)
You would like to set a password for a bank account. However, there are three restrictions on the format of the password:
1) it has to contain only alphanumerical characters (a−z, A−Z, 0−9);
2) there should be an even number of letters;
3) there should be an odd number of digits.
You are given a string S consisting of N characters. String S can be divided into words by splitting it at,
and removing, the spaces.
The goal is to choose the longest word that is a valid password.
You can assume that if there are K spaces in string S then there are exactly K + 1 words.

For example, given "test 5 a0A pass007 ?xy1", there are five words and three of them are valid passwords: "5", "a0A"
and "pass007".
Thus the longest password is "pass007" and its length is 7.
Note that neither "test" nor "?xy1" is a valid password, because "?" is not an alphanumerical character
and "test" contains an even number of digits (zero). '''
t = input('Enter your password: ').split()

while not t:
    t = input('Enter your password: ').split()


def valid_passwords(text):
    good_passes = []
    if text:
        for i in text:
            if i.isalnum():
                letter_cnt = 0
                digit_cnt = 0
                for x in i:
                    if x.isalpha():
                        letter_cnt += 1
                    else:
                        digit_cnt += 1
                if letter_cnt % 2 == 0 and digit_cnt % 2 != 0:
                    good_passes.append(i)
        return good_passes


def find_pass(good_passes):
    result = ''
    if good_passes:
        longest = max([len(word) for word in good_passes])
        for x in good_passes:
            if len(x) == longest:
                result = '\n'.join([result, x])
        return result
    else:
        return 'No valid password'


print(find_pass(valid_passwords(t)))
