import csv


def promocodegenerator(name, data):  # функция создаёт промокод для товара {promo}
    return list(name.split()[0])[0] + list(name.split()[0])[1] + data.split('.')[0] + list(name.split()[-1])[-1] + \
           list(name.split()[-1])[
               -2] + data.split('.')[1]


f = open('products.csv', 'r', encoding='utf-8-sig')
reader = csv.DictReader(f, delimiter=';')
file = open('product_promo.csv', 'w', encoding='utf-8-sig')
writer = csv.writer(file)
writer.writerow(['Category', 'product', 'Date', 'Price per unit', 'Count', 'Promocode'])
for line in reader:
    promo = promocodegenerator(line['product'], line['Date'])
    writer.writerow([line['Category'], line['product'], line['Date'], line['Price per unit'], line['Count'], promo])
