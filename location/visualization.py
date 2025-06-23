import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import platform

from Project.bigdataProject.location.data import loc, loc_name

# 시스템에 맞는 폰트 지정
if platform.system() == 'Darwin':  # macOS
    plt.rc('font', family='AppleGothic')

url = "https://raw.githubusercontent.com/southkorea/southkorea-maps/master/kostat/2013/json/skorea_provinces_geo.json"
gdf = gpd.read_file(url)

total = pd.DataFrame(loc)[loc_name].iloc[0]
pop = pd.DataFrame(loc)[loc_name].iloc[1]

lis = [[n, d, p] for n, d, p in zip(loc_name, total, pop)]
df = pd.DataFrame(lis, columns=['행정구역별(시도)', '범죄발생총건수', '인구수'])

df[['범죄발생총건수']] = df[['범죄발생총건수']].astype(int)
df[['인구수']] = df[['인구수']].astype(int)

fig, ax = plt.subplots(figsize=(12, 6))

def plot_crime_total_by_region_map():
    gdf["total"] = 0

    for name in gdf['name']:
        total = df[df['행정구역별(시도)'] == name]['범죄발생총건수']
        if not total.empty:
            gdf.loc[gdf['name'] == name, 'total'] = total.values[0]

    gdf["total"] = gdf["total"].astype(int)

    fig, ax = plt.subplots(1, 1, figsize=(10, 12))
    gdf.plot(column='total', cmap='OrRd', linewidth=0.8, edgecolor='black', legend=True, ax=ax)

    ax.set_title("시도별 범죄 발생 합계", fontsize=15)
    ax.set_axis_off()
    plt.show()

def plot_crime_total_by_region():
    # 데이터 준비
    x = df['행정구역별(시도)']
    y = df['범죄발생총건수'].astype(int)

    # 시각화

    ax.bar(x, y, width=0.6, edgecolor="white", linewidth=0.7, color='skyblue')

    ax.set_title("시도별 범죄 발생 합계")
    ax.set_ylabel("발생 건수")
    ax.set_xlabel("행정구역(시도)")

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_crime_percent_by_region_map():
    gdf["percent"] = 0
    df['범죄발생비율'] = (df['범죄발생총건수'] / df['인구수'])

    for name in gdf['name']:
        percent = df[df['행정구역별(시도)'] == name]['범죄발생비율']

        if not percent.empty:
            gdf.loc[gdf['name'] == name, 'percent'] = percent.values[0]

    gdf["percent"] = gdf["percent"].astype(float)

    fig, ax = plt.subplots(1, 1, figsize=(10, 12))
    gdf.plot(column='percent', cmap='OrRd', linewidth=0.8, edgecolor='black', legend=True, ax=ax)

    ax.set_title("시도별 인구 10만명당 범죄 발생률", fontsize=15)
    ax.set_axis_off()
    plt.show()

def plot_crime_percent_by_region():
    df['범죄발생비율'] = (df['범죄발생총건수'] / df['인구수'])

    # 데이터 준비
    x = df['행정구역별(시도)']
    y = df['범죄발생비율']

    # 시각화
    ax.bar(x, y, width=0.6, edgecolor="white", linewidth=0.7, color='skyblue')

    ax.set_title("시도별 범죄 발생 합계")
    ax.set_ylabel("발생 건수")
    ax.set_xlabel("행정구역(시도)")

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()