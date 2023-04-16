import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.dates as mdate
import mplcyberpunk

data_inicial = '2018-03-01'
data_final = '2023-03-01'

ativo = 'ITUB3.SA'

df = yf.download(ativo, data_inicial, data_final)['Adj Close']

precos_max = df.cummax()
drawdowns = df/precos_max - 1
drawdown_maximo = drawdowns.min()

plt.style.use('cyberpunk')

fig, ax = plt.subplots()

ax.plot(drawdowns)
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
ax.xaxis.set_major_locator(mdate.YearLocator(1))
ax.set_title('ITAÚ (ITUB3)')
ax.set_ylabel('Drawdown')
plt.show()