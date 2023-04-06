#!/usr/bin/env python
# coding: utf-8

# In[2]:


def reverse_words(st):
    s_list = list(st.split(' '))
    rev_s = []
    for word in s_list[::-1]:
        rev_s.append(word)
    rev_s = " ".join(rev_s)
        
    print("----------------------Result------------------------")    
    print("[input 문장]")
    print(st)
    print("[output 문장]")
    print(rev_s)
        
if __name__ == '__main__':
    reverse_words("Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth;")
    reverse_words("Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,")

