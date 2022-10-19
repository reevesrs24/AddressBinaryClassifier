import glob
import random
import string
import csv
import pandas as pd


def main():
    cities = set()
    state_ids = set()
    streets = set()
    units = set()
    postcodes = set()

    df_us_cities = pd.read_csv('csv/cities/uscities.csv')

    for index, row in df_us_cities.iterrows():
        cities.add(row['city_ascii'])
        state_ids.add(row['state_id'])
    
    for name in glob.glob('csv/addresses/*'):
        df = pd.read_csv(name) 
        print(name)

        count = 0
        for index, row in df.iterrows():
            if type(row['STREET']) == str and type(row['NUMBER']) == int:
                s = "{} {}".format(row['NUMBER'], row['STREET'])
                streets.add("{} {}".format(row['NUMBER'], row['STREET']))
            if type(row['UNIT']) == str:
                u = row['UNIT'].split(' ')
                if len(u) <= 2:
                    units.add(row['UNIT'])
            if type(row['CITY']) == str:
                cities.add(row['CITY'])
            if type(row['POSTCODE']) == int:
                postcodes.add(row['POSTCODE'])

            count += 1
            if count == 50000:
                break
            # city = random.choice(cities)
            # state_id = random.choice(state_ids)
            #if type(row['UNIT']) == str:
            # print("{} {} {} {} {}".format(row['STREET'].lower(), row['UNIT'], city, state_id, row['POSTCODE']))

    count = 0
    with open('address_dataset.csv', 'w', newline='', encoding='utf-8') as f:
        # create the csv writer
        header = ['text', 'label']
        writer = csv.writer(f)
        writer.writerow(header)

        cities = list(cities)
        state_ids = list(state_ids)
        streets = list(streets)
        units = list(units)
        postcodes = list(postcodes)

        while count < 100000:
            count += 1
            city = random.choice(cities)
            state = random.choice(state_ids)
            street = random.choice(streets)
            unit = random.choice(units)
            postcode = random.choice(postcodes)

            if count % 10 == 0:
                a = "{} {} {} {} {}".format(street, unit, city, state, postcode)
                writer.writerow([a, 1])
            elif count % 5 == 0:
                a = "{} {} {} {} {}".format(street, street, city, state, postcode)
                writer.writerow([a, 0])
            elif count % 6 == 0:
                a = "{} {} {} {} {} {}".format(street, unit, unit, city, state, postcode)
                writer.writerow([a, 0])

            a = "{} {} {} {}".format(street, city, state, postcode)
            writer.writerow([a, 1])
            

            l = [street, city, state, postcode]

            l.pop(random.randint(0, len(l)-1))

            a = ' '.join([str(x) for x in l])
            writer.writerow([a, 0])

            if count % 10 == 0:
                l = [street, unit, state, postcode]
                a = ' '.join([str(x) for x in l])
                writer.writerow([a, 0])


def create():
    chars = string.ascii_letters + " #.;'?!@#$%^&*()"

    with open('bad_data.csv', 'w', newline='', encoding='utf-8') as f:
        header = ['text', 'label']
        writer = csv.writer(f)
        writer.writerow(header)

        for i in range(25000):
            bad_input = ''.join(random.choice(chars) for _ in range(random.randrange(1, 100)))
            writer.writerow( [bad_input, 0] )




if __name__ == '__main__':
    main()
    create()