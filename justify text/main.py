# Write an algorithm to justify text.
# E.g. Given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:
#  ["the  quick brown", # 1 extra space on the left
#   "fox  jumps  over", # 2 extra spaces distributed evenly
#   "the   lazy   dog"] # 4 extra spaces distributed evenly

class MySolution:
    def JustifyWordsToTextLines(self, k, words):
        result_lines = []
        cur_line = ""
        cur_line_words_count = 0
        cur_line_words_symbols_count = 0
        unjustified_words_num = 1
        for word in words:
            inc_str = "%s%s" % (" " if len(cur_line)>0 else "", word)
            add_word = len(cur_line)+len(inc_str) <= k  
            if add_word:
                cur_line += inc_str
                cur_line_words_count += 1
                cur_line_words_symbols_count += len(word)
             
            if not add_word or (word == words[-1] and cur_line_words_count > unjustified_words_num):
                # line is full or it's last line with more than 1 word
                # will do justification of cur_line
                rem_spaces_cnt = k-cur_line_words_symbols_count-(cur_line_words_count-1)
                cur_pos = 0
                while rem_spaces_cnt > 0:
                    while (cur_pos < len(cur_line)-1 and cur_line[cur_pos] != " "):
                        cur_pos += 1
                    if (cur_pos == len(cur_line)-1):
                        # reached end of cur_line
                        # need to go from beginning
                        cur_pos = 0
                    else:
                        # have next-to-end of current word position 
                        # will insert a space at this position
                        cur_line = cur_line[:cur_pos] + " " + cur_line[cur_pos:]
                        rem_spaces_cnt -= 1
                        # need to run to next word beginning
                        cur_pos += 2
                        while (cur_pos < len(cur_line)-1 and cur_line[cur_pos] == " "):
                            cur_pos += 1
                        
                result_lines.append(cur_line)
                appended = True
                cur_line = "" if add_word else word
                cur_line_words_count = 0 if add_word else 1
                cur_line_words_symbols_count = 0 if add_word else len(word)

        if cur_line != "":
            result_lines.append(cur_line)
        return result_lines


words = ["the", "quick", "brown", "fox", "jumps", "over", "tha", "lazy", "dog"]
k = 16
lines = MySolution().JustifyWordsToTextLines(k, words)
for line in lines:
    print(line)
