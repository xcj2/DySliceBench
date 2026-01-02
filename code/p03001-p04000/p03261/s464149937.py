def has_duplicates(words):
    return len(words) != len(set(words))

def words(n):
    words = []
    for i in range(n):
        w = input()
        words.append(w)
    return words

def shiritori(shiritori_words):
    ans = []
    word = shiritori_words[0]
    end_word = word[len(word) -1]
    for j in range(1, len(shiritori_words)):
        word = shiritori_words[j]
        first_word = word[0]
        if has_duplicates(shiritori_words) or end_word != first_word:
            ans.append("No")
        else:
            ans.append("Yes")
        end_word = word[len(word) - 1]
    return ans
            
        

n = int(input())
shiritori_words = words(n)
ans = shiritori(shiritori_words)
if "No" in ans:
    print("No")
else:
    print("Yes")