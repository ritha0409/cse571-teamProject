
from scipy import stats

# following values for all mazes are taken from the csv file generated by running the searches

bi_time = [0.001063585, 0.004953384, 0, 0, 0, 0, 0.569495678, 0.697319269, 0.074090719, 0.734409809, 0.79213047, 0.033689737, 0.633049011, 0.800085545, 0.106120348, 0.705373526, 0.011103392, 0.005959511, 0.005988836]
a_star_time = [0.002238035, 0.01010561, 0, 0.015596867, 0, 0.015545845, 0.120222569, 0.113588095, 0.01587534, 0.125717402, 0.114273071, 0.00807786, 0.143790007, 0.193585873, 0.019015074, 0.118587494, 0.002009869, 0.002022028, 0.000928164]
bfs_time = [0.003067255, 0.009805441, 0, 0.015736341, 0, 0, 0.126193285, 0.098488331, 0.028856277, 0.178822517, 0.119854212, 0.017157555, 0.147763014, 0.181503534, 0.01695323, 0.112715006, 0.015990496, 0.005980015, 0.004992723]
dfs_time = [0.000997782, 0.004983664, 0, 0.015625238, 0, 0, 0.063598871, 0.078971624, 0.202047825, 0.11803031, 0.104619265, 0.004913568, 0.037802935, 0.090906382, 0.009968996, 0.079654932, 0.002975941, 0.009151697, 0.003988981]

bi_nodes = [184, 606, 41, 449, 39, 10, 602, 620, 45, 583, 637, 22, 502, 621, 91, 584, 41, 36, 31]
a_star_nodes = [221, 549, 49, 535, 53, 14, 604, 513, 66, 488, 459, 38, 399, 618, 55, 491, 49, 44, 39]
bfs_nodes = [269, 620, 170, 682, 92, 15, 633, 551, 89, 517, 476, 71, 509, 645, 91, 531, 170, 159, 153]
dfs_nodes = [146, 390, 85, 806, 59, 15, 382, 434, 610, 358, 421, 26, 166, 333, 53, 371, 85, 205, 69]

bi_corners_time = [0.00404810905456543, 0.026033878326416016, 0.09966683387756348]
a_star_corners_time = [0.0039365291595458984, 0.07496809959411621, 0.9939777851104736]

bi_corners_nodes = [199, 1136, 4380]
a_star_corners_nodes = [275, 1115, 3708]


search_time = ['bfs_time', 'dfs_time', 'a_star_time']
search_nodes = ['bfs_nodes', 'dfs_nodes', 'a_star_nodes']

for i, search in enumerate([bfs_time, dfs_time, a_star_time]):

	t_value, p_value = stats.ttest_ind(a=bi_time, b=search, equal_var=True)

	final_p = float("{:.6f}".format(p_value/2))  

	print('Search: ', search_time[i],' T-value= %f' % float("{:.6f}".format(t_value)), ' p-value= %f' % final_p)

	alpha = 0.05

	if final_p <= alpha:
		print('Benefited by Bidir')
	else:
		print('Not Benefited by Bidir')
	print()


for i, search in enumerate([bfs_nodes, dfs_nodes, a_star_nodes]):

	# t_value,p_value=stats.ttest_ind(a=bi_nodes , b=search, equal_var=True)
	temp = []
	temp.append(bi_nodes[1])
	temp += bi_nodes[6:16]

	temp2 = []
	temp2.append(search[1])
	temp2 += search[6:16]
	
	t_value , p_value = stats.ttest_ind(a=temp, b=temp2, equal_var=True)

	final_p = float("{:.6f}".format(p_value/2)) 

	print('Big Search: ', search_nodes[i],' T-value= %f'%float("{:.6f}".format(t_value)), ' p-value= %f' % final_p)

	alpha = 0.05

	if final_p<=alpha:
		print('Benefited by Bidir')
	else:
		print('Not Benefited by Bidir')
	print()

for i, search in enumerate([bfs_nodes, dfs_nodes, a_star_nodes]):

	# t_value,p_value=stats.ttest_ind(a=bi_nodes , b=search, equal_var=True)
	temp = []
	temp.append(bi_nodes[0])
	temp += bi_nodes[2:6]
	temp += bi_nodes[16:]

	temp2 = []
	temp2.append(search[0])
	temp2 += search[2:6]
	temp2 += search[16:]
	
	t_value,p_value=stats.ttest_ind(a=temp, b=temp2, equal_var=True)

	final_p=float("{:.6f}".format(p_value/2)) 

	print('Small Search: ', search_nodes[i],' T-value= %f'%float("{:.6f}".format(t_value)), ' p-value= %f'%final_p)

	alpha = 0.05

	if final_p<=alpha:
		print('Benefited by Bidir')
	else:
		print('Not Benefited by Bidir')
	print()

t_value,p_value=stats.ttest_ind(a=bi_corners_time, b=a_star_corners_time, equal_var=True)

final_p=float("{:.6f}".format(p_value/2)) 

print('Search: a_star_corners_time',' T-value= %f'%float("{:.6f}".format(t_value)), ' p-value= %f'%final_p)

alpha = 0.05

if final_p<=alpha:
		print('Benefited by Bidir')
else:
	print('Not Benefited by Bidir')
print()


t_value,p_value=stats.ttest_ind(a=bi_corners_nodes, b=a_star_corners_nodes, equal_var=True)

final_p=float("{:.6f}".format(p_value/2)) 

print('Search: a_star_corners_nodes',' T-value= %f'%float("{:.6f}".format(t_value)), ' p-value= %f'%final_p)

alpha = 0.05

if final_p<=alpha:
	print('Benefited by Bidir')
else:
	print('Not Benefited by Bidir')
print()