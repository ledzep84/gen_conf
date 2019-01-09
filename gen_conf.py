###Read file and each line###
file = open('C:/Users/YOUR_OWN_PATH_TO_FOLDER/input.txt', 'r')
line = file.read().splitlines()

#Counter on number of lines
i=0
ctr = len(line)



#######Start################
###Write to File Function###
def writeToFile(int, desc):
 filewrite = open('C:/Users/YOUR_OWN_PATH_TO_FOLDER/config_out.txt', 'a+')


 ###Multiple line template##
 template = """
!=====================================!

show run {intvar}


configure terminal
{intvar}
{descvar}
end


show run {intvar}


""".format(intvar=int, descvar=desc)
 

 filewrite.write(template)
 
 filewrite.close()

###Write to File Function###
#######End##################



###Call function writeToFile###
while i < ctr:
 writeToFile(line[i], line[i+1])
 i += 2


file.close()

