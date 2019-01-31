#Financial application: calculate tips

subtotal, gratuity_rate = eval(input("Enter the subtotal and a gratuity rate:"))

gratuity = gratuity_rate / 100 * subtotal
total = subtotal + gratuity

print("The gratuity is", "%.2f" % gratuity, "and the total is", "%.2f" % total)