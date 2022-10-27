# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def kaya_equation(pop, gdp, enInt, carbInt, output_type = "CO2"):
    '''
    Computes Kaya Identity using the formula:
    co2 = pop * gdp * enInt * carbInt
    :param pop:
    :param gdp:
    :param enInt:
    :param carbInt:
    :return:
    '''
    if (pop < 0):
        raise ValueError("pop cannot be negative")
    if (gdp < 0):
        raise ValueError("gdp cannot be negative")
    if (enInt < 0):
        raise ValueError("enInt cannot be negative")
    if (carbInt < 0):
        raise ValueError("carbInt cannot be negative")

    co2 = pop * gdp * enInt * carbInt

    if output_type == 'CO2':
        return co2
    else:
        c = co2 / 3.67
        return c




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result = kaya_equation(82.4, 44, 5, 0.05)
    print(result)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
