import pandas as pd

# 시도별 범죄율 데이터셋
path = "/Users/exn199/PycharmProjects/PythonProject/FastAPIProject/applicationProgrammingDevelopment/Project/bigdataProject/location/location.csv"
loc = pd.DataFrame(pd.read_csv(path, encoding="UTF-8"))

loc.columns = loc.iloc[0]
loc = loc.loc[1:].drop(index=[3]).reset_index(drop=True)

original_cols = list(loc.columns)[:4]
loc_name = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시', '세종특별자치시', '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주특별자치도']

loc.columns = original_cols + loc_name

print(loc.info())
