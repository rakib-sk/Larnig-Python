''' 3. 🛒 Ecommerce Discount Calculation
User 0 দিলে ইনপুট বন্ধ হবে।
প্রতিটি product price ইনপুট নাও।
Loop ব্যবহার করে:
- মোট দাম
- ১০% ডিসকাউন্ট
- ডিসকাউন্টের পর ফাইনাল দাম'''
products = []

while True:
    product_price = int(input("Enter products price $: "))
    
    products.append(product_price)
    
    if product_price == 0:
        break
    
    
total_price = 0
then_discount_price = 0

i = 0
while i<len(products):
    total_price += products[i] 
    then_discount_price = total_price+(total_price*(10/100))
    
    i += 1
    
print("\nTotal price $: ", total_price)    
print("10% discount prices is $: ", then_discount_price)