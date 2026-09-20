import json
import os

# 1. 讀取 raw.txt 數據
raw_file_path = os.path.join('data', 'raw.txt')
data_points = []

with open(raw_file_path, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#') or line.startswith('Year'):
            continue
        year, pop = line.split(',')
        data_points.append({
            'year': int(year),
            'population': float(pop)
        })

# 排序數據
data_points.sort(key=lambda x: x['year'])

# 2. 計算平均值、總成長率、CAGR
populations = [p['population'] for p in data_points]
avg_population = round(sum(populations) / len(populations), 2)

start_year = data_points[0]['year']
end_year = data_points[-1]['year']
start_pop = data_points[0]['population']
end_pop = data_points[-1]['population']

total_growth_rate = round(((end_pop - start_pop) / start_pop) * 100, 2)
n_years = end_year - start_year
cagr = round((((end_pop / start_pop) ** (1 / n_years)) - 1) * 100, 2)

# 3. 整理成 JSON 格式
result = {
    'summary': {
        'avg_population_billion': avg_population,
        'total_growth_rate_percent': total_growth_rate,
        'cagr_percent': cagr,
        'start_year': start_year,
        'end_year': end_year
    },
    'data': data_points
}

# 4. 輸出至 data/cleaned.json
output_path = os.path.join('data', 'cleaned.json')
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

print("資料清理與計算成功！輸出檔案至 data/cleaned.json")
