price: int = 100.1
tax: float = 10

def calc_price_including_tac(price: int, tax: float) -> int :
    return int(price*tax)

if __name__ == '__main__':
    print(f'{calc_price_including_tac(price=price, tax=tax)}円')