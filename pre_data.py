import pandas as pd
data = pd.read_csv("Map&box_plot.csv") #global for everone
data_name = pd.read_csv("Provinces Name Thai&Eng.csv") #global for everone
data_lat_log = pd.read_csv("lat_log.csv") #global for everone

data_time_series = pd.read_csv("time_series&scatter.csv") #global for everone
###########################################map and box plot#######################################
def prepare_data():
	province = data[data['จังหวัด'].notnull()]
	province.to_csv("Map&box_plot_filted.csv",index=False)

def thai_to_eng(thai_name):
	return data_name.loc[data_name['Thai name'] == thai_name]["English name"].values[0]

def gen_lat_log(pro):
	lat = data_lat_log[ data_lat_log["province"] == pro ]["latitude"]#.values
	lat = lat[lat.notnull()].values[0]
	log = data_lat_log[ data_lat_log["province"] == pro ]["longitude"]#.values
	log = log[log.notnull()].values[0]
	return lat,log

def edited():
	df = pd.read_csv("Map&box_plot_filted.csv")
	years =  list(df.columns.values[2:])
	province = df['จังหวัด']
	years_ = []
	provinces_ = []
	case_ = []
	lat_ =[]
	log_ = []
	for p in province:
		for y in years:
			years_.append(y)
			provinces_.append(p)
			case_var = df.loc[df['จังหวัด'] == p][y].values[0].replace(",","") # (1)search from data fram (2)select only especially year (3)finally, remove "," in the number string form
			case_.append(case_var)
			lat, log = gen_lat_log(p)
			lat_.append(lat)
			log_.append(log)
			
	dir_ = {"years":years_, "provinces":provinces_, "case":case_, "latitude":lat_, "longitude":log_}
	pd.DataFrame.from_dict(dir_).to_csv("Map&box_plot_edited.csv",index=False)



###########################time series&scatter#############################
def prepare_data2():
	df = data_time_series[ data_time_series["ชนิดยาเสพติด"].notnull() ]
	df.to_csv("time_series&scatter_filted.csv",index=False)

def edited2():
	df = pd.read_csv("time_series&scatter_filted.csv")
	years =  list(df.columns.values[2:])
	types = df['ชนิดยาเสพติด']
	years_ = []
	type_ = []
	case_ = []
	for t in types:
		for y in years:
			years_.append(y)
			type_.append(t)
			case_var = df.loc[df['ชนิดยาเสพติด'] == t][y].values[0].replace(",","") # (1)search from data fram (2)select only especially year (3)finally, remove "," in the number string form
			case_.append(case_var)
	dir_ = {"years":years_, "drug types":type_,"case":case_}
	print(dir_)
	pd.DataFrame.from_dict(dir_).to_csv("time_series&scatter_edited.csv",index=False)

def edited3():
	df = pd.read_csv("time_series&scatter_filted.csv")
	years =  list(df.columns.values[2:])
	types = df['ชนิดยาเสพติด']
	years_ = []
	dir_ = {"years":years}
	for t in types:
		for y in years:
			case_var = df.loc[df['ชนิดยาเสพติด'] == t][y].values[0].replace(",","") # (1)search from data fram (2)select only especially year (3)finally, remove "," in the number string form
			try:
				dir_[t].append(case_var)
			except:
				dir_[t] = [case_var]
	print(dir_)
	pd.DataFrame.from_dict(dir_).to_csv("time_series&scatter_edited2.csv",index=False)
edited3()
