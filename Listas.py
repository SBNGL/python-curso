
articulos = ['Computadores', 'ipads', 'ipads', 'iphones']

new_articles = articulos.copy()
new_articles.append('Apple')
#new_articles.extend(articulos)
articulos.insert(1, 'xiaomi')
#articulos.clear()

articulos.pop(1)
articulos.remove('iphones')
#print(articulos.index('Computadores'))
#print(articulos.count('ipads'))

print(new_articles)
new_articles.sort()

print(new_articles)
#print(new_articles) 