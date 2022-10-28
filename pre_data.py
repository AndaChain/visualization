import pandas as pd
data = pd.read_csv("Map&box_plot.csv") #global for everone
data_name = pd.read_csv("Provinces Name Thai&Eng.csv") #global for everone
data_lat_log = pd.read_csv("lat_log.csv") #global for everone
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
edited()
#print( gen_lat_log("บึงกาฬ") )
