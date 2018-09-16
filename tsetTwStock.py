import twstock

stock = twstock.Stock('2330')
bfp = twstock.BestFourPoint(stock)

#%%
print ('bfp.best_four_point_to_buy')
print (bfp.best_four_point_to_buy())

print ('bfp.best_four_point_to_sell')
print (bfp.best_four_point_to_sell())

print ('bfp.best_four_point')
print (bfp.best_four_point())
print (stock.moving_average(stock.price,3))
print ('--------')
print (stock.moving_average(stock.price,6))
#print (stock.price[-5:])   # 近五日之收盤價
