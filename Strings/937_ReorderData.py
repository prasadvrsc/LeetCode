class Solution(object):

    def reorder_log_files(self, logs):
        digit_logs= []
        letter_logs= []
        for log in logs:
            words = log.split(' ')
            if words[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        letter_logs.sort(key = lambda x: x.split(' ')[0])
        letter_logs.sort(key = lambda x: x.split(' ')[1:])
        letter_logs.extend(digit_logs)
        return letter_logs
    


#Test Case
logs = ["dig1 8 1 5 1","let2 art can","dig2 3 6","let1 own kit dig","let3 art zero"]
print(Solution().reorder_log_files(logs))
