import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

sns.set(font_scale=1, rc={'text.usetex' : True,
                          'text.latex.preamble': r'\usepackage[charter]{mathdesign}',
                          'font.family':['serif'],
                          'font.size': 10,
                          'figure.dpi': 300},
                          color_codes=True)
sns.set_style('white')

df = pd.read_excel("data_extraction.xls").fillna('None')
df

# publications per year

snow = pd.read_excel("quality_assessment.xlsx", header=None)

snow = snow[[0,2]].iloc[1:,:]
snow[2] = snow[2].astype(int)
snow.columns = ['Article', 'Publication year']


df_year = snow.groupby(['Publication year']).count()
df_year

g = sns.lineplot(

    data=df_year,
    x='Publication year', y='Article', marker="s",
    color='black')

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
# plt.gca().spines['left'].set_visible(False)
# plt.gca().spines['bottom'].set_visible(False)

g.set(xlabel='Year', ylabel='Count')

plt.savefig('pubs.png', dpi=300)

# plt.show()

# latencia
df_label = df.groupby(['Label latency']).count()

# g = sns.catplot(kind='bar',
#     data=df_label,
#     x='Label latency', y='article',
#     color='black')

# g.set(xlabel='Year', ylabel='Count')

# plt.show()

df_label = df.loc[df['Label latency'] == 'Infinite']
df_label

# lista = []

# for i in df_label['Authors']:
#     lista += i.replace('\n',',').split(',')

# print(Counter(lista))

# evolução
df_evolution = df.groupby(['How is concept evolution approached?']).count()
df_evolution

df_evolution = df.loc[df['How is concept evolution approached?'] ==
                      'Concept evolution detection'].sort_values(by='Publication year')
df_evolution


# hierarchy
df_app = df.groupby(['Approach'])['Method name'].apply(list)
df_app[0]

#
df_metrics = df['What are the evaluation methods employed?']

all = []

for i,j in enumerate(df['What are the evaluation methods employed?']):
    new_j = j.lower().replace('\n',',').replace('f1 measure','f1').replace('f-measure','f1')\
            .replace('f1-measure','f1').replace('macro-f1','macro f1').replace('macro-averaged','macro')\
            .replace('micro-averaged','micro').replace('micro-average','micro')\
            .replace('macro-average','macro').replace('micro-f1','micro f1')\
            .replace('example-based ','').replace('f1 score', 'f1')\
            .replace('macro-','macro ').replace('micro-','micro ')\
            .replace('sample-based ','').replace('ex.-based ','')\
            .replace('microf1','micro f1').replace('avepre','average precision')\
            .replace('micf1','micro f1').replace('example-f1','f1')\
            .replace('instance-f1','f1').replace('micro f','micro f1')\
            .replace('macro f1 (f1m)','macro f1').replace('f1 loss','f1')\
            .replace('one error','one-error').replace('avg','average')\
            .replace('f11','f1').replace('average.', 'average')\
            .replace('exact match', 'subset accuracy')\
            .replace('subset-accuracy','subset accuracy')\
            .replace('training','train').replace('testing','test')\
            .replace('logarithmic loss','log-loss')\
            .replace('macro unknown rate','unkrm')\
            .replace('label introduction pattern','lip')\
            .replace('average overall f1 (o-f1)','micro f1')\
            .replace('average per-class f1 (c-f1)','macro f1')\
            .replace('per-class f1 (c-f1)','macro f1')\
            .replace('ap','average precision').replace('maverage','average')\
            .replace('kaverage precisionpa','kappa').replace('𝑘', 'k').replace('micro f1 ', 'micro f1')\
            .replace('number of ', '')
    all += new_j.strip().split(',')

all = Counter(all)

data = pd.DataFrame().from_dict(all, orient='index').reset_index()

data = data.sort_values(by=0, ascending=False)

count = 0

for i,j in enumerate(data[0][17:]):
    count += j

other = data[17:].reset_index(drop=True)

data = data[:18].reset_index(drop=True)
data['index'][17] = 'other'
data[0][17] = count

plt.pie(data[0][::-1], labels=data['index'][::-1], colors=sns.color_palette("viridis"), startangle=-90, wedgeprops=dict(width=0.3))

plt.savefig('metrics.png', dpi=300)

# plt.show()

all

#
other.columns = ['index', 'count']

# sns.scatterplot(x='count', y='index', data=other)

# plt.show()

other

#concept drift

drift = df[df['Patterns of drift detected'] != 'None'].reset_index(drop=True)

patterns = list()

for i in drift['Patterns of drift detected']:
    patterns += i.split(',')

patterns = [i.strip() for i in patterns]

patterns = pd.DataFrame.from_dict(Counter(patterns), orient='index').sort_values(by=0, ascending=False).T

# patterns.columns = ['Não mencionado', 'Abrupto', 'Incremental', 'Gradual', 'Recorrente']

plt.figure(figsize=(10,4))

ax = sns.barplot(
    data=patterns,
    fill=False,
    width=0,
    color='black',
    orient='h'
)

for i in ax.containers:
    ax.bar_label(i, padding=2)

# Customize the plot
# plt.title('Combined Bar and Line Plot')
plt.savefig('drift.png', dpi=300)

# plt.show()

# comparison baselines
baselines = df['Comparison baselines']

all = []

for i in baselines:
    str = i.split('\n')
    all += [x.lower().replace('ml-knn','mlknn')\
        .replace('mlht','ht').replace('mht','ht')\
        .replace('osml-elm','oelm')\
        .replace('mlknn','knn') for x in str]
    # all += str


baselines = pd.DataFrame.from_dict(Counter(all), orient='index').sort_values(by=0, ascending=False)

baselines = baselines[:15].T

baselines.columns = ['ML-KNN', 'CC', 'ECC', 'MHT', 'BR', 'EPS', 'MLSAMPkNN',
    'PS', 'kNNPA', 'RAkEL', 'OELM', 'MLSAMkNN', 'EaBR', 'EBR', 'MLSAkNN']

baselines = baselines.T.reset_index()


plt.pie(baselines[0], labels=baselines['index'], colors=sns.color_palette("grey"), startangle=30, wedgeprops=dict(width=0.3))


# sns.barplot(x=baselines[0], y=baselines['index'])

# plt.show()

# for i in baselines['index']:
#     if i in list(df['Method name']):
#         print(i)

# plt.figure(figsize=(10,4))

# ax = sns.pieplot(
#     data=baselines,
#     fill=False,
#     width=0,
#     color='black',
#     orient='h'
# )

# for i in ax.containers:
#     ax.bar_label(i, padding=2)

plt.savefig('baselines.png', dpi=300)

#datasets
datasets = df['Dataset used']

all = []

for i in datasets:
    str = i.split('\n')
    all += [x.lower() for x in str]
    # all += str


datasets = pd.DataFrame.from_dict(Counter(all), orient='index').sort_values(by=0, ascending=False)

datasets = datasets[:15].T

datasets.columns = ['Enron', 'Yeast', 'mediamill', 'Scene', 'Emotions', 'OHSUMED',
    'IMDB', 'Medical', 'Corel5k', 'Slashdot', 'Birds', 'CAL500', '20NG', 'Flags', 'TMC2007']


datasets = datasets.T.reset_index()

plt.pie(datasets[0], labels=datasets['index'], colors=sns.color_palette("grey"), startangle=30, wedgeprops=dict(width=0.3))

plt.savefig('datasets.png', dpi=300)

#
libraries = df['Does it use pre-built libraries?']
libraries = libraries.replace('No', 'No library')

libraries

libraries = pd.DataFrame.from_dict(Counter(libraries), orient='index').sort_values(by=0, ascending=False)

plt.pie(libraries[0], labels=libraries.index, colors=sns.color_palette("gray"), startangle=50, wedgeprops=dict(width=0.3))

plt.savefig('libraries.png', dpi=300)
