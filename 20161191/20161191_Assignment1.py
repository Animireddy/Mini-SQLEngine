import re


data = {}


def print_res(inp):
	print ','.join(inp['attr'])
	for row in inp['values']:
		print ','.join([str(x) for x in row])

def get_cols(inp,cols,flag,a_flag,tables,w_flg,w_arr,j_tab,j_col): #
	
	output = {}
	output['attr'] = []
	output['values'] = []
	if flag[2]: # it has aggregate func
		inp = inp[tables[0]]
		output['attr'].append(a_flag+'('+cols[0].lower()+')')
		ind = inp['attr'].index(cols[0].lower()) #finds the given ele in list and find it's position
		temp = []
		print len(w_arr)
		for col in inp['values']: ##inp['values'] = array of values = [[row1],[line2],[row3]]
			if(len(w_arr)==0):
				temp.append(col[ind]) #corresponding ind col in every row
			elif len(w_arr)==3:
				w_op = w_arr[1]
				w_val = int(w_arr[2])
				w_ind = inp['attr'].index(w_arr[0].lower()) #finds the given ele in list and find it's position
				
				if (w_op == '<' and col[w_ind] < w_val) or (w_op == '>' and col[w_ind] > w_val) or (w_op == '=' and col[w_ind] == w_val) or (w_op == '>=' and col[w_ind] >= w_val) or (w_op == '<=' and col[w_ind] <= w_val):
					temp.append(col[ind])
			elif len(w_arr)==7:
				w_op1 = w_arr[1]
				w_val1 = int(w_arr[2])
				w_ind1 = inp['attr'].index(w_arr[0].lower()) 
				w_op2 = w_arr[5]
				w_val2 = int(w_arr[6])
				w_ind2 = inp['attr'].index(w_arr[4].lower()) 
				w_andc = w_arr[3]
				cond1 = 0
				cond2 = 0
				if (w_op1 == '<' and col[w_ind1] < w_val1) or (w_op1 == '>' and col[w_ind1] > w_val1) or (w_op1 == '=' and col[w_ind1] == w_val1) or (w_op1 == '>=' and col[w_ind1] >= w_val1) or (w_op1 == '<=' and col[w_ind1] <= w_val1):
					#temp.append(col[ind])
					cond1 = 1;
				if (w_op2 == '<' and col[w_ind2] < w_val2) or (w_op2 == '>' and col[w_ind2] > w_val2) or (w_op2 == '=' and col[w_ind2] == w_val2) or (w_op2 == '>=' and col[w_ind2] >= w_val2) or (w_op2 == '<=' and col[w_ind2] <= w_val2):
					#temp.append(col[ind])
					cond2 = 1;
				if w_andc == 'AND' or w_andc == 'and':
					if cond1==1 and cond2==1:
						temp.append(col[ind])
				if w_andc == 'OR' or w_andc == 'or':
					if cond1==1 or cond2==1:
						temp.append(col[ind])


		if a_flag == "sum":
			output['values'].append([sum(temp)])
		if a_flag == 'max':
			output['values'].append([max(temp)])
		if a_flag == 'min':
			output['values'].append([min(temp)])
		if a_flag == 'avg':
			output['values'].append([(sum(temp)*1)/len(temp)])
	else:
		if cols[0] == '*' and len(tables) == 1: #where a = 10; w_arr is 3size
			inp = inp[tables[0]]
			temp = []
			#for table in tables:
			for x in inp['attr']:
				temp.append(x) #all attributes are appended in temp
			cols[:] = temp[:]
			output['attr'] += cols[:] #
			###w_cond
			w_op = '/'
			w_ind = -1
			w_val = -1000
			w_ind
			w_val
			if len(w_arr) == 3:
				w_ind = inp['attr'].index(w_arr[0])
				w_op  = w_arr[1]
				w_val = int(w_arr[2])
			elif len(w_arr) == 7:
					# if(len(w_arr[0].split('.'))>1):
					# 	w_ind1 = inp['attr'].index(w_arr[0].split('.')[1].strip())
					# 	w_tab = 
				w_ind1 = inp['attr'].index(w_arr[0]) 
				w_ind2 = inp['attr'].index(w_arr[4]) 
				w_op1  = w_arr[1]
				w_val1 = int(w_arr[2])
				w_op2  = w_arr[5]
				w_val2 = int(w_arr[6])
				w_andc = w_arr[3]
				
				# print w_ind1
				# print w_ind2
				# print w_op1
				# print w_op2
				# print w_val1
				# print w_val2

			for col in inp['values']: #each row in inp['values']
				arr = []
				if len(w_arr) == 3 and ((w_op == '<' and col[w_ind] < w_val) or (w_op == '>' and col[w_ind] > w_val) or (w_op == '=' and col[w_ind] == w_val) or (w_op == '>=' and col[w_ind] >= w_val) or (w_op == '<=' and col[w_ind] <= w_val)):# or len(w_arr)==0:
					for i in range(len(cols)):
						j = inp['attr'].index(cols[i]) #cols = [set of all attributes] = [Att1,Att2,Att3]
						arr.append(col[j]) #1 row of all columns
					if flag[0]:
						if arr not in output['values']: #already there or not
							output['values'].append(arr)
					else:
						output['values'].append(arr)
				elif len(w_arr) == 7:
					flg = 0
					cond1 = 0
					cond2 = 0
					if (w_op1 == '<' and col[w_ind1] < w_val1) or (w_op1 == '>' and col[w_ind1] > w_val1) or (w_op1 == '=' and col[w_ind1] == w_val1) or (w_op1 == '>=' and col[w_ind1] >= w_val1) or (w_op1 == '<=' and col[w_ind1] <= w_val1):
						#temp.append(col[ind])
						cond1 = 1;
					if (w_op2 == '<' and col[w_ind2] < w_val2) or (w_op2 == '>' and col[w_ind2] > w_val2) or (w_op2 == '=' and col[w_ind2] == w_val2) or (w_op2 == '>=' and col[w_ind2] >= w_val2) or (w_op2 == '<=' and col[w_ind2] <= w_val2):
						#temp.append(col[ind])
						cond2 = 1;
					if w_andc == 'AND' or w_andc == 'and':
						if cond1==1 and cond2==1:
							flg=1
					if w_andc == 'OR' or w_andc == 'or':
						if cond1==1 or cond2==1:
							flg=1
					if flg == 1:
						for i in range(len(cols)):
							j = inp['attr'].index(cols[i]) #cols = [set of all attributes] = [Att1,Att2,Att3]
							arr.append(col[j]) #1 row of all columns
						if flag[0]:
							if arr not in output['values']: #already there or not
								output['values'].append(arr)
						else:
							output['values'].append(arr)
				else:
					for i in range(len(cols)):
						j = inp['attr'].index(cols[i]) #cols = [set of all attributes] = [Att1,Att2,Att3]
						arr.append(col[j]) #1 row of all columns
					if flag[0]:
						if arr not in output['values']: #already there or not
							output['values'].append(arr)
					else:
						output['values'].append(arr)


		else: #multiple table with cols
			#for join
			w_ind1 = -1
			w_ind2 = -1
			tab1 = -1
			tab2 = -1
			tab = -1
			#for and or
			w_op1 = '/'
			w_op2 = '/'
			w_and = '/'
			w_val1 = 0
			w_val2 = 0 
			###w_cond
			w_op = '/'
			w_ind = -1
			w_val = -1000
			w_ind
			w_val
			check_arr = []
			check_arr1 = []
			check_arr2 = []
			#####
			if(cols[0]=='*' and len(tables)>1):
				temp = []
				for table in tables:
					for x in inp[table]['attr']:
						temp.append(table + '.' + x)
				cols = temp #
			#####
			if len(w_arr) == 3:
				for l in range(0,len(tables)): #
					if(len(w_arr[0].split('.'))>1):
						if w_arr[0].split('.')[1].strip() in inp[tables[l]]['attr']: #inp[table1][b]
							tab = w_arr[0].split('.')[0].strip() #table1
							w_arr[0] = w_arr[0].split('.')[1].strip()
							w_ind = inp[tables[l]]['attr'].index(w_arr[0])
					else:
						if w_arr[0] in inp[tables[l]]['attr']:
							tab = tables[l]
							w_ind = inp[tables[l]]['attr'].index(w_arr[0])
				w_op  = w_arr[1]
				w_val = int(w_arr[2])
				for row in inp[tab]['values']: 
					check_arr.append(row[w_ind]) 
				

			if len(w_arr) == 7: #2 condn
				for l in range(0,len(tables)): #
					#print len(w_arr[0].split('.'))
					if(len(w_arr[0].split('.'))>1):
						if w_arr[0].split('.')[1].strip() in inp[tables[l]]['attr']: #inp[table1][b]
							tab1 = w_arr[0].split('.')[0].strip() #table1
							w_arr[0] = w_arr[0].split('.')[1].strip()
							w_ind1 = inp[tables[l]]['attr'].index(w_arr[0])
							print w_ind1
					else:
						if w_arr[0] in inp[tables[l]]['attr']:
							tab1 = tables[l]
							w_ind1 = inp[tables[l]]['attr'].index(w_arr[0])

					if(len(w_arr[4].split('.'))>1):
						if w_arr[4].split('.')[1].strip() in inp[tables[l]]['attr']:
							tab2 = w_arr[4].split('.')[0].strip() #tab2
							w_arr[4] = w_arr[4].split('.')[1].strip()
							w_ind2 = inp[tables[l]]['attr'].index(w_arr[4])
					else:
						if w_arr[4] in inp[tables[l]]['attr']:
							tab2 = tables[l]
							w_ind2 = inp[tables[l]]['attr'].index(w_arr[4])
					
				# print tab1
				# print tab2
				# print w_ind1
				# print w_ind2

				for row in inp[tab1]['values']: #call each record and append corresponding col values in each record
					check_arr1.append(row[w_ind1]) ##if col1,col2 are called from table2 table_tmp[table2] = [[1,2],[2,4],...]
				for row in inp[tab2]['values']: 
					check_arr2.append(row[w_ind2]) 
				# print check_arr1
				# print check_arr2

				w_op1 = w_arr[1]
				w_and = w_arr[3]
				w_op2 = w_arr[5]
				w_val1 = int(w_arr[2])
				w_val2 = int(w_arr[6])

			if(len(w_arr))==4:
				tab1 = w_arr[0]
				tab2 = w_arr[2]
				w_ind1 = w_arr[1]
				w_ind2 = w_arr[3]

				w_ind1 = inp[tab1]['attr'].index(w_arr[1])
				w_ind2 = inp[tab2]['attr'].index(w_arr[3])

				for row in inp[tab1]['values']: #call each record and append corresponding col values in each record
					check_arr1.append(row[w_ind1]) ##if col1,col2 are called from table2 table_tmp[table2] = [[1,2],[2,4],...]
				for row in inp[tab2]['values']: 
					check_arr2.append(row[w_ind2])
				

			table_tmp = {}
			
			

			for table in tables: #table2, table1
				table_tmp[table] = []
				for col in cols: # a in table1, d in table2
					if len(col.split('.'))>1:
						if(col.split('.')[1].strip() in inp[table]['attr']):
							if col not in output['attr']:
						 		output['attr'].append(col)
					elif(col in inp[table]['attr']):
						if col not in output['attr']:
						 	output['attr'].append(col)
				
				for row in inp[table]['values']: #call each record and append corresponding col values in each record
					c1 = []
					for col in cols: # a in table1, d in table2
						if len(col.split('.'))>1 and col.split('.')[0].strip() == table:
							col = col.split('.')[1].strip()
						if(col in inp[table]['attr']):
							if col == j_col and j_tab != table:
								pass
							else:
								c1.append(row[inp[table]['attr'].index(col)]) ##if col1,col2 are called from table2 table_tmp[table2] = [[1,2],[2,4],...]
					table_tmp[table].append(c1) #table2 attributes,table1 attributes
			#print table_tmp

			if len(tables) > 1:	 
				output['values'] = []
				
				#{'table2': [[11191], [14421], [5117], [13393], [16116], [5403], [6309], [12262], [10226], [13021]], 'table1': [[922, 158], [640, 773], [775, 85], [-551, 811], [-952, 311], [-354, 646], [-497, 335], [411, 803], [-900, 718], [858, 731]]}
				ind = -1
				for row in table_tmp[tables[0]]: #it has a values but check may be with b
					#w_flg check for table1
					w_app1 = 0
					w_app = 0
					
					ind = ind + 1
					w_join = 0
					if len(w_arr) == 4:
						pass
					elif tab == tables[0] and len(w_arr) == 3 and ((w_op == '<' and check_arr[ind] < w_val) or (w_op == '>' and check_arr[ind] > w_val) or (w_op == '=' and check_arr[ind] == w_val) or (w_op1 == '>=' and check_arr[ind] >= w_val) or (w_op1 == '<=' and check_arr[ind] <= w_val)):
						w_app = 1;
					if tab1 == tables[0] and len(w_arr) == 7 and ((w_op1 == '<' and check_arr1[ind] < w_val1) or (w_op1 == '>' and check_arr1[ind] > w_val1) or (w_op1 == '=' and check_arr1[ind] == w_val1) or (w_op1 == '>=' and check_arr1[ind] >= w_val1) or (w_op1 == '<=' and check_arr1[ind] <= w_val1)):
						w_app1 = 1
					if tab2 == tables[0] and len(w_arr) == 7 and ((w_op2 == '<' and check_arr2[ind] < w_val2) or (w_op2 == '>' and check_arr2[ind] > w_val2) or (w_op2 == '=' and check_arr2[ind] == w_val2) or (w_op2 == '>=' and check_arr2[ind] >= w_val2) or (w_op2 == '<=' and check_arr2[ind] <= w_val2)):
						w_app2 = 1
					arr = row[:] #arr = [1,2] and with this [1,2] all rows of second table 
					for l in range(1,len(tables)): #
						ind1 = 0;
						for row2 in table_tmp[tables[l]]: #it has d values
							w_app2 = 0
							w_join = 0
							
							if len(w_arr) == 4 and check_arr1[ind]==check_arr2[ind1]:
								w_join = 1 
							elif tab == tables[l] and len(w_arr) == 3 and ((w_op == '<' and check_arr[ind1] < w_val) or (w_op == '>' and check_arr[ind1] > w_val) or (w_op == '=' and check_arr[ind1] == w_val) or (w_op1 == '>=' and check_arr[ind1] >= w_val) or (w_op1 == '<=' and check_arr[ind1] <= w_val)):
								w_app = 1;
							if tab1 == tables[l] and len(w_arr) == 7 and ((w_op1 == '<' and check_arr1[ind1] < w_val1) or (w_op1 == '>' and check_arr1[ind1] > w_val1) or (w_op1 == '=' and check_arr1[ind1] == w_val1) or (w_op1 == '>=' and check_arr1[ind1] >= w_val1) or (w_op1 == '<=' and check_arr1[ind1] <= w_val1)):
								w_app1 = 1

							if tab2 == tables[l] and len(w_arr) == 7 and ((w_op2 == '<' and check_arr2[ind1] < w_val2) or (w_op2 == '>' and check_arr2[ind1] > w_val2) or (w_op2 == '=' and check_arr2[ind1] == w_val2) or (w_op2 == '>=' and check_arr2[ind1] >= w_val2) or (w_op2 == '<=' and check_arr2[ind1] <= w_val2)):
								w_app2 = 1

							ind1 = ind1+1
							#w_flg = 1 check for table2 
							arr[:] = row[:] #end of array row append
							#join check row[col1] == row2[col2] if satisfy append else continue if w_flg=2;					
							#append only remaining colms 
							for k in range(len(row2)):
								arr.append(row2[k]) #

							if flag[0]:
								if (((w_and=='AND' or w_and == 'and') and (w_app1 == 1 and w_app2 == 1)) or ((w_and=='OR' or w_and == 'or') and (w_app1 == 1 or w_app2 == 1))) or len(w_arr)==0 or w_app==1 or w_join==1:

									if arr not in output['values']:
									#w_flg for and or => true or false
										output['values'].append(arr)
							else:
								if (((w_and=='AND' or w_and == 'and') and (w_app1 == 1 and w_app2 == 1)) or ((w_and=='OR' or w_and == 'or') and (w_app1 == 1 or w_app2 == 1))) or len(w_arr)==0 or w_app==1 or w_join==1:
									output['values'].append(arr)
							arr = []
			else:
				ind = 0;
				for row in table_tmp[tables[0]]:#[[attr1_vals],[attr2_vals]]
					if (len(w_arr) == 3 and ((w_op == '<' and check_arr[ind] < w_val) or (w_op == '>' and check_arr[ind] > w_val) or (w_op == '=' and check_arr[ind] == w_val) or (w_op1 == '>=' and check_arr[ind] >= w_val) or (w_op1 == '<=' and check_arr[ind] <= w_val))) or len(w_arr)==0:
						if flag[0]:
							if row not in output['values']:
								output['values'].append(row)
						else:
							output['values'].append(row)
					ind = ind + 1

	print_res(output)

def check_cols(cols,tables):
	for col in cols:
		flag = 0
		for table in tables:
			if col.split('.')[:-2:-1] in data[table]['attr']:
				if len(col.split('.')) == 2 and col.split('.')[0] == table:
					flag = 1
		if flag == 0:
			print('Column error')
			return 0
	return 1
def parse_query(query):
	w_flg = 0
	w_arr = []
	flag = [0 for i in range(3)] #array of 3 elements
	a_flag = None
	if  query[:-2:-1] != ';':  #last symbol
		print('Semicolon missing') 
		return
	if re.match('^select.*from.*',query) == 0: #start^ of string must be select(any no.of characters) if doesn't match return 0
		print('Invalid query')
		return	
	query = query.strip(';') # remove leading and trailing characters and print remaining string
	cols = query.split('from')[0] #split based on from and stores in an array
	cols = cols.strip('select').strip()
	if re.match('^distinct.*',cols): 
		flag[0] = 1
		cols = cols.replace('distinct','').strip()

	if re.match('^(sum|max|min|avg)\(.*\)', cols):
		a_flag = cols.split('(')[0].strip()
		flag[2] = 1
		cols = cols.strip(a_flag).strip().strip('()') #strip () and aggregate func
	cols = cols.split(',') #array of cols
	for i in range(len(cols)):
		cols[i] = cols[i].lower().strip()
	j_tab = ''
	j_col = ''
	if len(query.split('where')) > 1:
		wcond = query.split('where')[1].strip() #
		wcond_dot = wcond.split('.')
		if len(wcond_dot)==2:
			c_tab1 = wcond_dot[0].strip()
			wcond = wcond_dot[1].strip()
		wcond1 = wcond.split()
		
		if len(wcond1)==3: #col1,=,10
		#single or join condition
			if(len(re.split('=|\.',wcond)))==4:
				#join
				wcond1 = re.split('=|\.',wcond) #table1,col1,table2,co2
				w_flg = 2 #join  #array of 4 elements
				j_col = wcond1[1].strip()
				for i in range(len(cols)):
					if len(cols[i].split('.'))>1:
						
						if cols[i].split('.')[1].strip() == j_col:
							j_tab = cols[i].split('.')[0].strip()
							

			else:
				w_flg = 1 #normal condn
		elif len(wcond1)==7: #col1,=,10,AND,col2,=,20
		#AND OR operato
			w_flg = 3; #and or

		wcond1 = map(str.strip, wcond1)
		w_arr = wcond1

	if len(cols) == 1: #only 1 col is there
		if cols[0] == '*': 
			flag[1] = 1
	# else:
	# 	for i in range(len(cols)):
	# 		if len(cols[i].split('.'))>1:
	# 			cols[i]=cols[i].split('.')[1].strip()
		
	if flag[2] and len(cols) > 1:					##
		print("list contain Nonaggregated column")  ##
		return	

	tables = query.split('from')[1].split('where')[0].strip() #after from =>A,B where ...... =>before where => A,B
	tables = tables.split(',') #['table1','table2'] => tables
	for table in tables:
		table = table.strip()
		if table not in data:
			print("Invalid-table"+table)
			return			

	####me
	
	
	

	####
	# if re.match('^select.*from.*where.*',query):
	# 	if not flag[1]: #if not *
	# 		
	# 		if check_cols(cols,tables) == 0:
	# 			return
			#pass

	get_cols(data,cols,flag,a_flag,tables,w_flg,w_arr,j_tab,j_col)



file = open('./metadata.txt', 'r')
line = file.readline().strip() #linewise removing leading and trailing spaces
while line:
	if line == "<begin_table>":
		tname = file.readline().strip()  # table name
		data[tname] = {} #data['table1']={}
		data[tname]['attr'] = []
		attr = file.readline().strip()
		while attr != "<end_table>":
			data[tname]['attr'].append(attr.lower()) #{'table1': {'attr': [['a', 'b']]}}
			attr = file.readline()
			attr = attr.strip()
	line = file.readline().strip()

for tname in data:
	data[tname]['values'] = []
	data[tname]['name'] = tname
	f = open('./' + tname + '.csv', 'r') #open table1.csv 
	for line in f:
		arr = [int(field.strip('"')) for field in line.strip().split(',')]
		data[tname]['values'].append(arr) #first [[all A attr values,all B attr values]]
while 1:		
	query = raw_input("query:")
	parse_query(query) 	#takes input