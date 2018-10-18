st = set()

# adding 
st.add(1) # single
st.add(2) # single
st.update([2, 3, 4]) # multiple
print (st)

# discard() if the item does not exist in the set, it remains unchanged. 
st.discard(2)
st.discard(7) # no error

# But remove() will raise an error in such condition.
# st.remove(7) # error

for item in st:
    print (item)