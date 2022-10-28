import pandas as pd
data = pd.read_csv("Map&box_plot.csv") #global for everone
data_name = pd.read_csv("Provinces Name Thai&Eng.csv") #global for everone
def prepare_data():
	province = data[data['จังหวัด'].notnull()]
	province.to_csv("Map&box_plot_filted.csv",index=False)

def thai_to_eng(thai_name):
	return data_name.loc[data_name['Thai name'] == thai_name]["English name"].values[0]

def edited():
	df = pd.read_csv("Map&box_plot_filted.csv")
	years =  list(df.columns.values[2:])
	province = df['จังหวัด']
	years_ = []
	provinces_ = []
	case_ = []
	for p in province:
		for y in years:
			years_.append(y)
			provinces_.append(p)
			case_var = df.loc[df['จังหวัด'] == p][y].values[0].replace(",","") # (1)search from data fram (2)select only especially year (3)finally, remove "," in the number string form
			case_.append(case_var)
	dir_ = {"years":years_, "provinces":provinces_, "case":case_}
	pd.DataFrame.from_dict(dir_).to_csv("Map&box_plot_edited.csv",index=False)
edited()
