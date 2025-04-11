# w, a, r+

# this is reading file.......  (w)
with open('textfile.txt','r') as f:
    data = f.read()
    print(data)



# writing in file or overwrite.....
with open('write.txt','w') as f: # if write.txt is not present then it will create new write.txt file and if write.txt file is present then it will remove all old data .
    write_data = f.write('hello everyone\n shubham here.')


# appedend in my file .. with given data  (a)

with open('write.txt','a') as f: # if there is no file with this name present this will create new file and append data
    append_data = f.write('I am software developer. But want to become AI Engineer\n.')


# reading and writing in file (r+)

with open('write.txt','r+') as f:  # (ye bee file to overwrite krega but jitna text hoga uthna he overwrite krega but if we dont want to overwrite we only want to write from end.)
    f.seek(len(f.read())) # f.seek() --- check cursor position 
    write_in_file = f.write('currently i am working....\n\n')

# reading file.......(r+)  
with open('write.txt','r+') as f:  # (ye bee file to overwrite krega but jitna text hoga uthna he overwrite krega but if we dont want to overwrite we only want to write from end.)
    read_write = f.read()
    print(read_write)


# reading and writing at same time in one to another file...
with open('textfile.txt','r+') as rf:
    with open('write.txt','r+') as wf:
        cur_position = wf.seek(len(wf.read()))
        print(cur_position)
        wf.write((rf.read()))
